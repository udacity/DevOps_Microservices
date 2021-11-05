#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
# Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified PATH or URL. 
# The Docker build process can access any of the files located in this context.
docker build --tag=housingapp_release_v1 .

# Step 2: 
# List docker images on your local machine.
# Note images ARE NOT containers.  They are the class, where containers
# are the running instances.
# Two ways to call this command `docker images` or `docker image ls`
docker images

# Step 3: 
# Run flask app
# A container run insides of a host machine.  And uses the architecture
# available within the host machine to execute.  However, a container has
# it own file system, networking, dependencies and even it own os.x
# docker run -p <container port>:<host machine port> <image tag or name>
# The -d option say run in detach mode, which means run in the background.
# docker run -d -p <container_port>:<host_port> --name <adding a name to the container> <image tag or name>
docker run -p 8000:80 --name housingapp housingapp_release_v1

# Step 3a
# See if the container is running
# Displays the list of containers running on your machine
# ps stands for processes
# -all says show all containers even if it not running
docker ps -all

# To stop a container used the command: `docker stop <container name or id>`
# To remove a container use the command: `docker rm <container name or id>`
# To restart a container use the command: `docker restart <container name or id>`
# To remove an iamge: `docker rmi <image name or id>`