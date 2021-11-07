#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
<<<<<<< HEAD
docker build --tag=uda4proj:latest .
# Step 2:
# List docker images
docker images
# Step 3:
# Run flask app
docker run -p 8000:80 uda4proj:latest

=======

docker build --tag=udacityproj4 .
# Step 2: 
# List docker images
docker image ls
# Step 3: 
# Run flask app
docker run -p 8000:80 udacityproj4
>>>>>>> fe3540decde906ddffeda2709c21280f2eaad169
