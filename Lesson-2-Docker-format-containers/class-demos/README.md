# Overview

[![CircleCI](https://circleci.com/gh/noahgift/udacity-devops-microservices.svg?style=svg&circle-token=644aca8c4c94ca89efb97a97d78a4025468b67cc)](https://circleci.com/gh/noahgift/udacity-devops-microservices)

## udacity-devops-microservices

Udacity devops course on microservices

## Proposed Kubernetes Example Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask scikit-learn app in Container
* Run via kubectl
* Configure cluster and Deploy
* Loadtest and verify auto-scale

## Boston Housing Dataset Pickled model Colab

<https://github.com/noahgift/boston_housing_pickle>

## Makefile

* Runs hadolint Dockerfile
* Uses the config.yml file within a .circleci directory
* In the parent directory, runs make run-circleci-local to simulate what will happen in the remote CircleCI environment
* Uses the CircleCI website (see <https://circleci.com/blog/increase-reliability-in-data-science-and-machine-learning-projects-with-circleci/>) to test remotely
