# libra-run-template

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14317601.svg)](https://doi.org/10.5281/zenodo.14317601)


This repository has the data for the run BABY-1L-1.

## How to reproduce the results

### In Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LIBRA-project/BABY-1L-run-1/HEAD)

### Locally

1. Create a conda environment (requires conda):

```
conda env create -f environment.yml
```

2. Run the notebooks with the created environment `baby_1l_run_1`


## Todo list:
- [x] [Link to Zenodo](https://zenodo.org/)
- [x] Add Zenodo badge with DOI
- [ ] Add general run data to [`data/general.json`](data/general.json)
- [x] Add LSC data to [`data/tritium_detection`](data/tritium_detection)
- [ ] Add neutron detection data to [`data/neutron_detection`](data/neutron_detection)
- [x] Add OpenMC model to [`analysis/neutron`](analysis/neutron)
- [x] Add Tritium model to [`analysis/tritium`](analysis/tritium)
- [ ] Add the right version tags to [`environment.yml`](environment.yml)
- [ ] Add information to the README (info about the run)
- [x] Add [binder](https://mybinder.org/) badge
- [x] Update [CI workflows](.github/workflows)