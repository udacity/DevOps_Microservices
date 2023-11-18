#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
image_name=udacity-pj4
image_tag=v1.0.0
container_name=udacity-pj4

# Build image and add a descriptive tag
docker build -t $image_name:$image_tag .

# List docker images
docker image list

# Run flask app
docker run --name $container_name -p 8000:80 --rm $image_name:$image_tag

