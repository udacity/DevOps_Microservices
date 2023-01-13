#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=ravi105362/project

# Step 2
# Run the Docker Hub container with kubernetes
kubectl create deployment project --image="$dockerpath:latest"


# Step 3:
# List kubernetes pods
kubectl get pod

# Step 4:
# Forward the container port to a host
kubectl port-forward pod/project-6b67fbf87-996t9 --address 0.0.0.0 80:80
