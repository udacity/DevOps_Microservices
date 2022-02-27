#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

username="ewkoch3"
tag="udacity_predict"

# Step 1:
# Create dockerpath
dockerpath="$username/$tag"

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker login --username=$username
docker tag $tag $dockerpath:latest

# Step 3:
# Push image to a docker repository
docker push "$dockerpath:latest"
