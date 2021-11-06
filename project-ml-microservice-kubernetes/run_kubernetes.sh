#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
# dockerpath=<>
dockerpath=$username/learning

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run house-predictions --image=$dockerpath:latest


# Step 3:
# List kubernetes pods
kubectl get pods --all-namespaces

# Step 4:
# Forward the container port to a host
kubectl port-forward pod/house-predictions 8000:80

# Step 5:
# To get logs use the following command in the shell where you did the prediction
# kubectl logs house-predictions