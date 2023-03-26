#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=ml-kub-project .

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run flask app with logging local and to a file
docker run -p 8000:80 ml-kub-project
# docker run --log-driver local --log-opt max-size=10m --log-opt max-file=3 -p 8000:80 ml-kub-project
