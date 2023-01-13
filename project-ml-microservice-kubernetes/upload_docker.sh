#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=ravi105362/project

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker login --username ravi105362 --password-stdin
docker tag project-4 "$dockerpath:latest"

# Step 3:
# Push image to a docker repository
docker push ravi105362/project:latest
