#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=swapnagondi/app

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run uda4proj --image=swapnagondi/uda4proj
# Step 3:
# List kubernetes pods
kubectl get pods 

# Step 4:
# Forward the container port to a host
kubectl port-forward uda4proj 8000:80

