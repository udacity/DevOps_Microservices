#!/usr/bin/bash

# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`
# Step 1:
# Create dockerpath
dockerpath="$DOCKER_ID/$DOCKER_IMAGE"

# Step 2:  
# Authenticate & tag
docker login --username $DOCKER_ID --password $DOCKER_PASSWD

docker tag $DOCKER_IMAGE $dockerpath

echo "Docker ID and Image: $dockerpath"


# Step 3:
# Push image to a docker repository
docker image push $dockerpath