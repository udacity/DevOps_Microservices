#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
# Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified PATH or URL. 
# The Docker build process can access any of the files located in this context.
docker build --tag=housingapp .

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run flask app
# docker run -p <container port>:<host port>
docker run -p 8000:80 housingapp
