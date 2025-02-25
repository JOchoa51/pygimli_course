# Geophysical Analysis Jupyter Notebooks

This repository contains Jupyter Notebook files for various geophysical analysis methods. Each notebook is tailored to perform a specific task related to geophysical data acquisition, processing, and interpretation.

## File Overview

1. **1-HV.ipynb**: Implements the Horizontal-to-Vertical (H/V) spectral ratio analysis, commonly used for seismic site characterization.
2. **2-SEV.ipynb**: Focuses on Vertical Electrical Sounding (SEV) for subsurface resistivity profiling.
3. **3-TRE.ipynb**: Conducts Electrical Resistivity Tomography (TRE) for imaging subsurface structures.
4. **4-TRS.ipynb**: Processes Seismic Refraction Tomography (TRS) data to analyze subsurface velocity layers.
5. **5-GRAV.ipynb**: Analyzes raw gravity data for geophysical surveys.
6. **5.1-BouguerCorrection.ipynb**: Applies Bouguer corrections to gravity data for terrain effects.
7. **5.2-RedPolo.ipynb**: Implements gravity data reduction to the pole for improved interpretation.

## Requirements

- Python 3.x
- Required Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scipy`
  - `geopandas`
  - `seaborn`
  - Additional libraries based on specific notebooks (see comments in each file).

## Installation

**Important**: the use of an independent environment is strongly sugested
1. Clone or download this repository.
2. Install the required libraries using pip:
   ```bash
   pip install numpy pandas matplotlib scipy geopandas seaborn pygimli
   ```

## Usage

1. Open the notebooks in Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Navigate to the desired notebook (e.g., `1-HV.ipynb`) and run the cells sequentially.
3. Follow instructions or modify the parameters in the notebooks for specific datasets.

## Notes

- Ensure that input datasets are correctly formatted and paths are specified in the notebooks.
- Outputs include plots, processed data tables, and insights into subsurface structures.

## Examples

### Running the H/V Analysis (1-HV.ipynb):
1. Provide the seismic data file in the required format.
2. Adjust processing parameters (e.g., frequency ranges).
3. Execute all cells to obtain H/V spectral ratio plots.

### Running the Bouguer Correction (5.1-BouguerCorrection.ipynb):
1. Input raw gravity data with metadata.
2. Specify terrain and density parameters.
3. Execute all cells to generate Bouguer corrected gravity data.

## Contributions

Feel free to suggest improvements or submit pull requests for additional functionality.

## Contact

For questions or support, please contact:  
Jesús Ochoa Contreras  
[ochoacontrerasjesus8@gmail.com](mailto:ochoacontrerasjesus8@gmail.com)
