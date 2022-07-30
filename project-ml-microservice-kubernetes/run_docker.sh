!/usr/bin/env bash

# Step 1:
sudo docker build -t udacity .

# Step 2: 
docker image ls

# Step 3: 
sudo docker run -p 8000:80 udacity 
