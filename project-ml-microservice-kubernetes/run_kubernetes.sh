#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
 dockerpath=project4-docker-udacity

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run project4-docker-udacity  --image=bmailazhagan/$dockerpath --port=80


# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward project4-docker-udacity 8000:80

