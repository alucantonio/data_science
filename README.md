# Data Science course materials

This repository contains the course materials of the *Data Science* course for the MSc
in Mechanical Engineering at Aarhus University. 

To download the contents of the repository, use the green button `Code->Download ZIP` in
this page. Then unzip the file into any folder on your hard drive. Please check for
updates regularly and, if needed, download the zip file again and overwrite the contents
of the folder.

## Setting up a Python environment
To run the Python scripts contained in the repository, first you need to create a
[`conda`](https://conda.io/projects/conda/en/latest/index.html) environment. We recommend using
[`mamba`](https://mamba.readthedocs.io/en/latest/) as a package manager.

To install `mamba`, follow the instructions reported on
[this](https://github.com/conda-forge/miniforge#mambaforge) page (you need to run the
commands from a shell).

Then, from the shell enter the directory of the repository and create a new `conda` environment:
```
mamba env create -f environment.yml
```
You can then *activate* the environment
```
mamba activate datascience
```
and run Python scripts within such an environment.

## Using Jupyter notebooks

To edit/run [`jupyter`](https://jupyter.org/) notebooks (*.ipynb), start [`JupyterLab`](https://jupyter.org/)
```
jupyter lab
```
and use the web interface to open notebooks.