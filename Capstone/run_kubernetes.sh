#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath="$DOCKER_ID/$DOCKER_IMAGE"

# Step 2
# Run the Docker Hub container with kubernetes
kubectl create deployment micro-ml-dps --image=$dockerpath --port=80 --replicas=3

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
sleep 10s # wait for 10 seconds for PODS to become READY.
kubectl port-forward deployments/micro-ml-dps 8000:80