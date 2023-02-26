# This dockerfile sets up the main environment for Ubuntu 22.04 
# and the associated software necessary for the Mathematical Modeling of the 
# Human Brain tutorial
FROM freesurfer/freesurfer:7.1.1
COPY license.txt /usr/local/freesurfer/.license

# 
RUN mkdir freesurfer-shared

#Labels
LABEL maintainer="travis.thompson@ttu.edu"
LABEL version="0.1"
LABEL description="Freesurfer image with license for: The book Mathematical Modeling of the Human Brain: from magnetic resonance images to finite element simulation"

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update Ubuntu Software repository
# RUN apt update


