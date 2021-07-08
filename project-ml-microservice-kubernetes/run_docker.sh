#!/usr/bin/env bash
set -
## Complete the following steps to get Docker running locally
NAME="prediction-engine"
TAG=latest
export DOCKER_IMAGE="$NAME:$TAG"
export CONTAINER_NAME="$NAME.$TAG"

# Step 1:
# Build image and add a descriptive tag
docker build . -t "$NAME:$TAG"

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run flask app
docker run --name $CONTAINER_NAME --rm -p 8000:80 $DOCKER_IMAGE
#docker container start "$CONTAINER_NAME"