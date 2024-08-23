# Data Science course materials

This repository contains the course materials of the *Data Science* course for the MSc
in Mechanical Engineering at Aarhus University. 

To download the contents of the repository, use the green button `Code->Download ZIP` in
this page. Then unzip the file into any folder on your hard drive. Please check for
updates regularly and, if needed, download the zip file again and overwrite the contents
of the folder.

## Setting up a Python environment
To run the Python scripts contained in the repository, first you need to create a
[`conda`](https://conda.io/projects/conda/en/latest/index.html) environment. 

_If you already have Anaconda installed on your computer_ please follow these
instructions:

- Open the Anaconda Prompt (Windows)/Terminal (MacOS/Linux) and execute the following commands:
  ```
  conda install -n base conda-libmamba-solver
  conda config --set solver libmamba
  ```
- Then, download the environment.yml from Brightspace and execute
  ```
  conda env create -f environment.yml
  ```
  to create the datascience environment and install all the Python libraries required for this course.
- Activate the new environment to start coding and running the Python scripts/notebooks:
  ```
  conda activate datascience
  ```
  (this step must be done every time you open a new Prompt/Terminal.)

_If you DO NOT have Anaconda already installed on your computer_, we recommend using
[`mamba`](https://mamba.readthedocs.io/en/latest/) as a package manager.

### Windows
- Download the latest `miniforge` installer from
[here](https://github.com/conda-forge/miniforge) (click on the link
`Miniforge-Windows-x86_64`).
- Run the installer and leave the default options during the
installation procedure.
**Warning**: you *cannot* use the default settings (in particular, the installation
path) if your username contains spaces. In this case, open `File Explorer` and create a new
directory *without spaces* (e.g. "mamba") under `C:\`. Then, run the installer and
choose this path as a destination folder. You may also need to move the directory where
you unzipped the contents of this repository in a location such that the path does not
contain spaces. 
- From the *Start* menu, launch the `Miniforge Prompt`.
- Navigate into the directory where you unzipped the contents of this repository.
- Execute the command
    ```
    mamba env create -f environment.yml
    ```
    to create the `datascience` environment and install all the Python libraries required for this
    course. 
- Activate the new environment to start coding and running the Python scripts/notebooks
  contained in this repository:
    ```
    mamba activate datascience
    ```
    (this step must be done every time you open a new `Miniforge Prompt` in order to use
    the scripts of this repository.)

### MacOS / Linux
- Open a terminal (e.g. `Terminal` under MacOS) and execute the following commands to
  download the installer using curl or wget and start the installation, e.g.
```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```
or
```
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```
- From the command prompt, enter the directory where you unzipped the contents of the repository.
- Execute the command
    ```
    mamba env create -f environment.yml
    ```
    to create the `datascience` environment and install all the Python libraries required for this
    course. 
- Activate the new environment to start coding and running the Python scripts/notebooks
  contained in this repository:
    ```
    mamba activate datascience
    ```
    (this step must be done every time you open a new terminal in order to use
    the scripts of this repository.)

## Using Jupyter notebooks

To edit/run [`jupyter`](https://jupyter.org/) notebooks (*.ipynb), start
[`JupyterLab`](https://jupyter.org/) by executing the following command from the command prompt
```
jupyter lab
```
and use the web interface to open notebooks. Press `CTRL+C` while on the prompt to
terminate `JupyterLab`.

## Contacts
Prof. Alessandro Lucantonio (a.lucantonio@mpe.au.dk)