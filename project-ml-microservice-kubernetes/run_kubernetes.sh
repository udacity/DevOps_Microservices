#!/usr/bin/env bash

# Parameters for our Kubernetes deployment

username="ewkoch3"
tag="udacity_predict"
podname="udacitypredict"


# Step 1:
# This is the docker ID / path
dockerpath="$username/$tag"

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run $podname\
    --image=$dockerpath\
    --port=80 --labels app=$tag 

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward $podname 8000:80

