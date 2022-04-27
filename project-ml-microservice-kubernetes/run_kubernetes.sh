#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=richbm10/my-private-repo

# Step 2
# Run the Docker Hub container with kubernetes
kubectl create deploy ml-microservice --image=$dockerpath:ml-microservice


# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward pod/ml-microservice-7c57bbd5ff-zvmpq --address 0.0.0.0 3000:80
