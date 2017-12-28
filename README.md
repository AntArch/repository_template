# repository_template

A template repository with structure and publishing artefacts

This repository contains the entire *Land Registration in Scotland workshop*, in the form of Jupyter notebooks.

The book was written and tested with Python. It currently uses python 3.5 (which is the current RoS preferred python environment).

Git update

* git add .
* git commit -m 'insert comment'
* git push -u origin master

## contents

### folder notebooks

Contains the jupyter notebooks.

All figures (except those dynamically generated using code) are stored in the sub-folder *figures*

All automated data profiles (using pandas profiling tool) are stored in the sub-folder *data_profile*

All *powerpoint, pdf* and *markdown* exports of the jupyter-notebooks are stored in the folder *exports*. **You are probably here to look for these**.

### folder tools

This folder contains python scripts that help structure the notebooks and export the notebooks to *powerpoint, pdf* and *markdown*. Ensure your read the README.md file.

### folder website

This doesn't work yet. It should ultimately export all the notebooks as a stand-alone website using pelican. 


## Required Packages

The code in the book was tested with Python.

The packages I used to run the code in the book are listed in [requirements.txt](requirements.txt) (Note that some of these exact version numbers may not be available on your platform: you may have to tweak them for your own use).
To install the requirements using [conda](http://conda.pydata.org), run the following at the command-line:

```
$ conda install --file requirements.txt
```

To create a stand-alone environment named ``LRSW`` with Python 3.5 and all the required package versions, run the following:

```
$ conda create -n LRSW python=3.5 --file requirements.txt
```

You can read more about using conda environments in the [Managing Environments](http://conda.pydata.org/docs/using/envs.html) section of the conda documentation.

## GDAL

There may be some gdal issues :-(. This is due to a badly set up geopandas and gdal library. Run the following to correct this:

> conda install -c conda-forge gdal matplotlib



## License

### Code
The code in this repository, including all code samples in the notebooks listed above, is released under TBC

### Text
The text content of the book is released under TBC

# creating a specification list file for easy(ish) installation

Activate the environment whose libraries you want to copy:

> source activate LRSW

To create this spec list as a file in the current working directory, run:

> conda list --explicit > requirements.txt

**An explicit spec file is not usually cross platform**, and therefore has a comment at the top such as # platform: osx-64 showing the platform where it was created. This platform is the one where this spec file is known to work. On other platforms, the packages specified might not be available or dependencies might be missing for some of the key packages already in the spec.

To use the spec file to create an identical environment on the same machine or another machine:

> conda create --name LRSW --file requirements.txt

To use the spec file to install its listed packages into an existing environment:

> conda install --name <environment name> --file requirements.txt

Conda does not check architecture or dependencies when installing from a spec file. To ensure that the packages work correctly, make sure that the file was created from a working environment, and use it on the same architecture, operating system and platform, such as linux-64 or osx-64.

To create this spec list as a file in the current working directory, run:

> conda list --explicit > requirements.txt

To remove the environment type

> conda remove --name LRSW --all

