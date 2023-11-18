
[![lx0612](https://circleci.com/gh/lx0612/DevOps_Microservices.svg?style=svg)](https://app.circleci.com/pipelines/github/lx0612/DevOps_Microservices)

## Project Overview

In this project, you will apply the skills you have acquired in this course to operationalize a Machine Learning Microservice API. 

You are given a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You can read more about the data, which was initially taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing). This project tests your ability to operationalize a Python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

### Project Tasks

Your project goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:
* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction
* Improve the log statements in the source code for this application
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction
* Upload a complete Github repo with CircleCI to indicate that your code has been tested

You can find a detailed [project rubric, here](https://review.udacity.com/#!/rubrics/2576/view).

**The final implementation of the project will showcase your abilities to operationalize production microservices.**

---

## Setup the Environment

* Create a virtualenv with Python 3.7 and activate it. Refer to this link for help on specifying the Python version in the virtualenv. 
```bash
python3 -m pip install --user virtualenv
# You should have Python 3.7 available in your host. 
# Check the Python path using `which python3`
# Use a command similar to this one:
python3 -m virtualenv --python=<path-to-Python3.7> .devops
source .devops/bin/activate
```
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

### Kubernetes Steps

1. **Setup and Configure Docker**
   - Go to the Docker Desktop website at https://www.docker.com/products/docker-desktop/ and follow the instructions to install Docker Desktop.
   - Verify : `docker --version`.

2. **Setup and Configure Kubernetes**
   - For Windows users, the recommended way is to use Docker Desktop. Open Docker Desktop, go to Settings, navigate to Kubernetes, and check "Enable Kubernetes."
   - Verify the Kubernetes configuration by running: `kubectl version --output json`.

3. **Create Flask App in a Container**
   - Build the Docker image for the Flask app using the following command: `docker build --tag udacity-pj4:v1.0.0 .`
   - Run the container with the created image: `docker run -d --rm -p 8000:80 udacity-pj4:v1.0.0`

4. **Deploy Flask App via Kubernetes**
   - Create an environment file `.env` and set variable `DOCKER_PASSWORD=<your-docker-hub-pw>`.
   - run: `source .env`.
   - Export your Docker Hub ID using: `export docker_path=<your-docker-hub-id>`.
   - Log in to Docker Hub to push the image: `echo "$DOCKER_PASSWORD" | docker login --username $docker_path --password-stdin`.
   - Tag and push the Docker image to Docker Hub: `docker image tag udacity-pj4:v1.0.0 $docker_path/udacity-pj4:v1.0.0 && docker image push $docker_path/udacity-pj4:v1.0.0`.
   - Create a Kubernetes deployment: `kubectl create deploy udacity-pj4 --image="$docker_path/udacity-pj4:v1.0.0"`.
   - Check whether the pod is in the READY state: `kubectl get pods`.
   - Wait pods ready, forward the port to access the Flask app locally: `kubectl port-forward deployment.apps/udacity-pj4 8000:80`.
