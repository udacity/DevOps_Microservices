#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=ramujai06/udacity-operationalize

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker login -u ramujai06
docker tag operationalize $dockerpath

# Step 3:
# Push image to a docker repository
echo "Docker ID and Image push"
docker push $dockerpath



