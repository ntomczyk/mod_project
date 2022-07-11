# Define the base image
FROM ubuntu:22.04

# Install required packages
RUN apt-get update \
 && apt-get upgrade\
 && apt-get install -y \
    python3-pip \
    python3-setuptools

# Copy this repo to a folder in the Docker container
COPY . /app

# Set the work directory
WORKDIR /app

# Install all the required packages
RUN pip3 install -r requirements.txt \
 && pip3 install .



#FROM python:3.10.0-alpine
#
## Where the project files will be installed and tested inside the container
#COPY . /app/
#WORKDIR /app
#
## Copy the project files to the WORKDIR
#COPY requirements.txt /app
#
## Setup the venv and install pyinstaller
#RUN python -m venv /tmp/venv && \
#    . /tmp/venv/bin/activate && \
#    pip install -r requirements.txt