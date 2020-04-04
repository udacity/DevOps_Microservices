#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image
docker build --tag=demolocal .
# Step 2: 
# List docker images
docker image ls
# Step 3: 
# Run flask app
docker run -it demolocal bash
