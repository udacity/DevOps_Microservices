#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
# dockerpath=<>
#list nodes
dockerpath=longtony/api-microservices:v1.0.0

# Step 2
# Run the Docker Hub container with kubernetes
minikube start
kubectl create deploy api-microservice --image=$dockerpath

# Step 3:
# List kubernetes pods
kubectl get nodes

# Step 4:
# Forward the container port to a host
kubectl port-forward pod/api-microservice 8000:80
