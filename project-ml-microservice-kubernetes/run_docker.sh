#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=microservice .

# Step 2: 
# List docker images
docker images list

# Step 3: 
# Run flask ap
docker run -p 8000:80 microservice