<h2 align=center>Mathematical Modeling of the Human Brain: from magnetic resonance images to finite element simulation</h2>
<h3 align=center>Travis Thompson<br>Texas Tech University<br>Department of Mathematics and Statistics</h2>
<p align=center>A docker-enabled virtual environment for the MD Anderson Cancer Center IGCT FEM human brain mesh generation workshop tutorial and open lab. March 5, 2023</p>

## Setting up
This section is a simple guide for those setting up the computing environment for the tutorial.  The first step is, of course, to [install docker](https://docs.docker.com/get-docker/) for your particular operating system.  Then you will need to clone [this repository](https://github.com/travisbthomp/igct-fem-workshop) via one of the commands below.

using git with ssh

> $ git clone git@github.com:travisbthomp/igct-fem-workshop.git

using git with https

> $ git clone https://github.com/travisbthomp/igct-fem-workshop.git

### Building the included docker images

In the repository root directory you will see three subdirectories.  They are

>freesurfer-img\
>svmtk-img\
>runtime-env

The first two directories, ending in -img, contain Dockerfiles for the separate software components of the tutorial that you will need to build.  In each of these directories, there is a file called "buildcommand" that contains the docker build command with the specific image name needed for further script compatibility. You can build the docker container images, from the terminal, as follows

> $ cd freesurfer-img\
> $ source buildcommand\
> $ cd ../svmtk-img\
> $ source buildcommand 

### Getting the FEniCS docker image
FEniCS is used to solve mathematical models. You can retrieve the official (legacy) [FEniCS docker image](https://fenicsproject.org/download/archive/) by executing the following `docker pull` command from a terminal window

> $ docker pull quay.io/fenicsproject/stable:current

### Retrieving the demonstration data
The software in this demo builds meshes from the files generated by a FreeSurfer segmentation.  Since FreeSurfer takes several hours to segment MRI data, users will need to make use of pre-segmented data for this tutorial. 

A shell script is provided that automatically downloads pre-segmented demonstration data (from a [zenodo archive](https://zenodo.org/record/4899120#.Y_rNntLMKXI)), unpacks it and cleans up the local environment.  The directory names to which the files are unpacked are important for the docker run scripts, so please leave these naming conventions untouched.

To download the user data.  Execute the following terminal commands from the root directory of this git repository

> $ cd runtime-env/mri-data\
> $ source getdata



### Visualization
If users are to be able to use the GUI tools, you will need to [download and install paraview](https://www.paraview.org/download/) and [download and install dicombrowser](https://download.xnat.org/dicombrowser/).  GUI functionality is not included in the docker images for this demo and will need to be run locally if it is to be available.

## Starting the tools
After the docker images have been built, the `freesurfer-img` and `svmtk-img` directories can be removed.  The users will execute their commands exclusively from within the directory `runtime-env`.  Let's switch into the runtime directory and see test our docker images.  From the repository root directory type the following command in a terminal window

> $ cd runtime-env

### To start FEniCS
> $ source startfenics

The above will use the `docker run` command located in the `startfenics` shell script file.  This docker run command starts the fenics docker image and creates a shared `runtime-env/fenics` which is also mounted inside the running docker image.

### To start FreeSurfer
> $ source startfreesurfer

The above command uses `docker run` to start the freesurfer docker image.  A shared `runtime-env/freesurfer` directory is created and mounted inside the running docker image as well as the `runtime-env/mri-data` directory.

### To start the SVMTK
> $ source startsvmtk

The above command uses `docker run` to start the svmtk docker image.  A shared `runtime-env/svmtk` directory is created and mounted inside the running docker image.