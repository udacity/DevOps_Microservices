#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build . --tag=udacity_predict

# Step 2: 
docker ps

# Step 3: 
docker run -p 8000:80 udacity_predict