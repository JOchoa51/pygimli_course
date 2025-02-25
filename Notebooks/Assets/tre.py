# %% [markdown]
# ![](encabezado.png)
# 

# %% [markdown]
# ---
# 
# # Tomografía de Resistividad Eléctrica (TRE)
# ---

# %%
import numpy as np
import matplotlib.pyplot as plt

import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert

# %% [markdown]
# # Crear el modelo de capas y la anomalía

# %%
world = mt.createWorld(start=[-20,0], 
					   end=[120,-50], 
					#    layers=[-2,-30], 
					   worldMarker=True)
anom1 = mt.createPolygon(verts=[[20,-30],[60,-25],[30,-10]], interpolate='spline', isClosed=True, addNodes=3, marker=4)
# anom1 = mt.createRectangle(start=[20,-25], end=[40,-10], marker=4)
anom = mt.createRectangle(start=[40,-5], end=[60,-20], marker=2)
# anom = mt.createPolygon(verts=[[70,-20],[80,-25],[90,-10]], interpolate='spline', isClosed=True, addNodes=5, marker=5)

geom = world + anom
pg.show(geom)
plt.gcf().set_size_inches(10,7)


# %% [markdown]
# # Generar electrodos

# %% [markdown]
# En el ejemplo se menciona el uso de un arreglo DD, ¿cómo se sabe qué tipo de arreglo es?
# 
# Debido a la experiencia, es conveniente agregar más nodos de refinamiento a una distancia vertical del 10% del espaciado de los electrodos para lograr suficiente precisión numérica, es decir, en (x,-0.1).

# %%
scheme = ert.createData(elecs=np.linspace(-20,120,48), schemeName='slm')
for p in scheme.sensors():
	geom.createNode(p)
	geom.createNode(p - [0,0.1])

# %% [markdown]
# # Generar malla

# %%
mesh = mt.createMesh(geom, quality=34, area=1)
pg.show(mesh)
plt.gcf().set_size_inches(12,9)

# %% [markdown]
# # Mapeo de resistividades

# %%
# [[regionNumber, resistivity], [regionNumber, resistivity], [...]
rhomap = [[1,1000.],
		  [2,200.],
		  [3,500.],
		  [4,50.],
		  [5,1000.]]
pg.show(mesh, data=rhomap, label=pg.unit('res'), showMesh=True, cMap='jet')
plt.gcf().set_size_inches(10,7)


# %% [markdown]
# # Crear la simulación de $\rho_{a}$

# %%
data = ert.simulate(mesh=mesh, scheme=scheme, res=rhomap, noiseLevel=1, noiseAbs=1E-6, seed=1337)

pg.info(np.linalg.norm(data['err']), np.linalg.norm(data['rhoa']))
pg.info('Simulated data', data)
pg.info('The data contains:', data.dataMap().keys())

pg.info('Simulated rhoa (min/max)', min(data['rhoa']), max(data['rhoa']))
pg.info('Selected data noise %(min/max)', min(data['err'])*100, max(data['err'])*100)

# %%
data.remove(data['rhoa'] < 0)
pg.info('Filtered rhoa (min/max)', min(data['rhoa']), max(data['rhoa']))

pg.show(data, cMap='jet')

# %% [markdown]
# # Inversión de $\rho_a$

# %%
mgr = ert.ERTManager(data)
inv = mgr.invert(lam=20, verbose=True)

# %% [markdown]
# ## Profundidad de investigación:
# 
# $$
# F_{ID}(z) = \frac{2}{\pi}\cdot \frac{z}{\left( a^2 + 4z^2 \right)^{1.5}}
# $$

# %%
ax, cb = mgr.showResult(cMap='jet')
pg.show(geom, fillRegion=False, regionMarker=False, ax=plt.gca())
plt.gcf().set_size_inches(10,7)

plt.show()

# %%
mgr.showResultAndFit()
plt.show()


