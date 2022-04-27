#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
# Reference: https://docs.docker.com/docker-hub/repos/#:~:text=To%20push%20an%20image%20to,docs%2Fbase%3Atesting%20).
dockerpath=richbm10/my-private-repo

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
cat ~/my_password.txt | docker login --username richbm10 --password-stdin

# Step 3:
# Push image to a docker repository
docker push $dockerpath:ml-microservice