# Ideas para el curso intersemestral 2024-2: _Modelado e inversión de datos geofísicos con python_

Buscando y practicando con PyGIMLi, el proceso es bastante sencillo y creo poder cubrir cada tema con facilidad en 2 horas, y desearía poder explicar un poco de la teoría detrás del método (del geofísico, no del de inversión).

No es difícil instalar, la desventaja es que sólo se puede a través de Anaconda, lo cual puede ser un poco confuso si no se está familiarizado con entornos de desarrollo.

Idealmente, los alumnos tendrán conocimientos al menos básicos del funcionamiento de Python, mínimamente declaración de variables y funcionamiento general de la sintaxis.

Se explicará de manera general el método geofísico, el principio bajo el cual opera, lo que mide, los factores que afectan su resolución y pronfundidad, así como casos para los que no se puede utilizar y sus limitantes. 

Gravimetría y magnetometría se podrían incluir en el mismo día porque se procesan prácticamente igual.
Por el momento, magnetometría está fuera debido a que no he encontrado una manera de incluir un modelado 2D.

Se debe incluir **SEV** en la parte de eléctrica, de hecho, podría ameritar dar SEV un día y TRE en otro

Tal vez añadir hidrogeofísica y permeabilidad hidráulica (no da tiempo ni tengo los conocimientos, pero se menciona por si es del interés de alguno)

# Condiciones
En todos los métodos geofísicos se dará una pequeña sección introductoria donde se cubran los principios teóricos y matemáticos básicos.

Siempre se debe priorizar la velocidad de convergencia en la inversión, y se debe explicar debidamente los parámetros que la afectan.

# Planeación

## Día 1: Tomografía de refracción sísmica
- Modelo de capas horizontal
- Incluir cuerpo intrusivo a manera de explicar la pobre resolución horizontal del método
- Mostrar el trazado de rayos para explicar por qué algunas capas no son visibles
- Mostrar hidden layers con velocidad inferior

## Día 2: Sondeo eléctrico vertical
- Modelo de capas con cavernas o cuerpos intrusivos
- Explicación de la determinación del NAF para fines geotécnicos u otros
- Principio de equivalencia y supresión

## Día 3: Tomografía de resistividad eléctrica
- Modelo de capas horizontales
- Caverna resistiva o conductiva
- Explicación de la determinación de los puntos de atribución y movimiento del arreglo
- Roll-along y slide-along (posible implementación)

## Día 4: Gravimetría
- Modelado de un dique inclinado u otro cuerpo
- Explicación de la ponderación de profundidad
- Problema de la no unicidad
- Probar varios métodos geofísicos en el mismo modelo para correlacionar resultados (sísmico por ejemplo ya que también incluye la densidad del cuerpo)
- Incluir modelado e inversión 3D si es posible (por ahora solamente la generación de anomalías con Blakely)

## Día 5: Cocientes espectrales
- Explicación del método y procesamiento sencillo de una señal de aceleración
- Contempla, además de la sísmica, manejo de datos con NumPy
- Simplificar el proceso para mantener solamente los aspectos esenciales.