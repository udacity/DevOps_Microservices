#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
dockerpath="ayo32/project4:latest"

# Step 2
kubectl run udacityproject\
#   --generator=run-pod/v1\
    --image=$dockerpath\
    --port=80 --labels app=udacityproject


# Step 3:
kubectl get pods

# Step 4:
kubectl port-forward udacityproject 8000:80

