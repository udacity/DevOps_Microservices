#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=swapnagondi/app

# Step 2:
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag uda4proj:latest swapnagondi/uda4proj:latest
docker login --username=swapnagondi

# Step 3:
# Push image to a docker repository
docker push swapnagondi/uda4proj:latest
