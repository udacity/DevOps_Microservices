#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
# dockerpath=<>
dockerpath="kingoyince/kubeproject:ver1"

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run kubeproject\
    --image=$dockerpath\
    --port=80 --labels app=kubeproject


# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward kubeproject 8000:80

