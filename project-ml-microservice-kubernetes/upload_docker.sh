#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
#dockerpath=<your docker ID/<imagetagname>
dockerpath=$username/latest

# Step 2:  
# Authenticate & tag
# I have an environment variable $username and $password so that I don't save in github
docker login --username $username &&\
    docker image tag project4_housing_predictons $dockerpath

# I have a token on my machine  that allows me to push directly to my repository
# I have also already tag
echo "Docker ID and Image: $dockerpath"

# Step 3:
# Push image to a docker repository
docker image push $dockerpath