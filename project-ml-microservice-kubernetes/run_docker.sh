#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=richbm10/my-private-repo:ml-microservice .

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run flask app
docker run -it --publish 3000:80 richbm10/my-private-repo:ml-microservice
