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
    python3-pip

RUN git clone --recursive https://github.com/SVMTK/SVMTK

WORKDIR /SVMTK

RUN python3 -m pip install .

WORKDIR /home

RUN mkdir svmtk
RUN mkdir svmtk/shared
