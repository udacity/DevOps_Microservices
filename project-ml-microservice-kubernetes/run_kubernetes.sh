#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub
image_name=udacity-pj4
image_tag=v1.0.0
deployment_name=udacity-pj4

# Step 1:
# This is your Docker ID/path
docker_path=lx96

echo $docker_path/$image_name:$image_tag
# Step 2
# Run the Docker Hub container with kubernetes
kubectl create deploy $deployment_name --image=$docker_path/$image_name:$image_tag


# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward deployment.apps/$deployment_name --address 0.0.0.0 8000:80


