FROM debian:buster

RUN apt-get update && apt-get install -y \
    bzip2 \
    cmake \
    curl \
    g++ \
    libboost-all-dev \
    libeigen3-dev \
    libgmp3-dev \
    libmpfr-dev \
    xz-utils \
    zlib1g-dev \
    git \
    python3-pip \
    vim


RUN git clone --recursive https://github.com/SVMTK/SVMTK

WORKDIR /SVMTK

RUN python3 -m pip install .

# ----- Other dependencies (for the book code environemnt) ------
RUN pip3 install numpy
RUN pip3 install nibabel

# libhdf5 and libnetcdf are needed by meshio
RUN apt-get install -y libhdf5-serial-dev
RUN apt-get install -y libnetcdf-dev
RUN pip3 install meshio[all]


WORKDIR /home

RUN mkdir svmtk
