# Cloud DevOps ND - C4- Microservices at Scale using AWS & Kubernetes - Supporting Material and Project Starter

This repository is associated with Cloud DevOps ND - Course 04 - Microservices at Scale using AWS & Kubernetes. In here, you'll find:

1. Supporting material used in the video demonstration in the course
2. Starting code for a project, in which you can containerize and deploy a machine learning srevice using Kubernetes.

---

Other resources:

- [Using SAM to create Lambda](https://codeolives.com/2019/09/19/vs-code-build-debug-and-deploy-aws-lambda-functions-using-visual-studio-code/)
- [Youtube Video for Local Lambda Creation](https://youtu.be/fEZE3rm8Ma8)

## A. Dependencies

### A.1. Python

[Download and install the python](https://www.python.org/downloads/).

### A.2. Docker Desktop

You would require you to install Docker Desktop to create containers for individual microservices. Refer the following links for instructions

- [macOS](https://docs.docker.com/docker-for-mac/install/),
- [Windows 10 64-bit: Pro, Enterprise, or Education](https://docs.docker.com/docker-for-windows/install/),
- [Windows  10 64-bit Home](https://docs.docker.com/toolbox/toolbox_install_windows/).
- You can find installation instructions for other operating systems at:  <https://docs.docker.com/install/>

### A.3. Kubernetes

You would need to install any one tool for creating a Kubernetes cluster - KubeOne / Minikube / kubectl on top of Docker Desktop:

1. [Install and Set Up kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) directly on top of Docker desktop - For Windows/macOS
2. [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) - For Linux/macOS

### A.4. AWS account to access AWS Lambda

You'll need an [AWS account](https://aws.amazon.com/free/?all-free-tier.&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc) to get started with [AWS Lambda](https://aws.amazon.com/lambda/), which is a serverless computing platform on cloud.  

### A.5. An account with Circle CI

You may sign up on [CircleCI.com](https://circleci.com/signup/) with your GitHub credentials.

---

## B. The Overarching Diagram

![Overview](https://camo.githubusercontent.com/bb29cd924f9eb66730bbf7b0ed069a6ae03d2f1a/68747470733a2f2f757365722d696d616765732e67697468756275736572636f6e74656e742e636f6d2f35383739322f35353335343438332d62616537616638302d353437612d313165392d393930392d6135363231323531303635622e706e67)

---

## C. Tutorials

### C.1. AWS Lambda & Serverless

- [Making Change](https://github.com/udacity/DevOps_Microservices/tree/master/lambda-functions/make-change-tutorial): Create and deploy a serverless lambda function that responds to an input request; this example creates the correct amount of change to make up a value in US dollars.
- [Wikipedia Query](https://github.com/udacity/DevOps_Microservices/tree/master/lambda-functions/wikipedia-query): Deploy a lambda function that responds to an input, wikipedia page query; this example returns the first sentence of a specific wikipedia page upon being queried.

## D. Project Instructions

- [Operationalize a Machine Learning Microservice API](https://github.com/udacity/DevOps_Microservices/tree/master/project-ml-microservice-kubernetes): Deploy a containerized, machine learning application using Kubernetes.

To run any project code, you'll have to set up a virtual environment with the project dependencies. All of the following instructions are to be completed via a terminal/command line prompt.

## E. Create and Activate an Environment

### E.1. Git and version control

These instructions also assume you have `git` installed for working with Github from a terminal window, but if you do not, you can download that first from this [Github installation page](https://www.atlassian.com/git/tutorials/install-git).

**Now, you're ready to create your local environment!**

1. If you haven't already done so, clone the project repository, and navigate to the main project folder.

    ```bash
    git clone https://github.com/udacity/DevOps_Microservices.git
    cd DevOps_Microservices/project-ml-microservice-kubernetes
    ```

2. Create (and activate) a new environment, named `.devops` with Python 3. If prompted to proceed with the install `(Proceed [y]/n)` type y.

    ```bash
    python3 -m venv ~/.devops
    source ~/.devops/bin/activate
    ```

    At this point your command line should look something like: `(.devops) <User>:project-ml-microservice-kubernetes<user>$`. The `(.devops)` indicates that your environment has been activated, and you can proceed with further package installations.

3. Installing dependencies via project `Makefile`. Many of the project dependencies are listed in the file `requirements.txt`; these can be installed using `pip` commands in the provided `Makefile`. While in your project directory, type the following command to install these dependencies.

    ```bash
    make install
    ```

Now most of the `.devops` libraries are available to you. There are a couple of other libraries that we'll be using, which can be downloaded as specified, below.

---

#### E.2. Other Libraries

While you still have your `.devops` environment activated, you will still need to install:

- Docker
- Hadolint
- Kubernetes ([Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) if you want to run Kubernetes locally)

#### E.3. Docker

You will need to use Docker to build and upload a containerized application. If you already have this installed and created a docker account, you may skip this step.

1. You’ll need to [create a free docker account](https://hub.docker.com/signup), where you’ll choose a unique username and link your email to a docker account. **Your username is your unique docker ID.**

2. To install the latest version of docker, choose the Community Edition (CE) for your operating system, [on docker’s installation site](https://docs.docker.com/v17.12/install/). It is also recommended that you install the latest, **stable** release:

3. After installation, you can verify that you’ve successfully installed docker by printing its version in your terminal: `docker --version`

#### E.4. Run Lint Checks

This project also must pass two lint checks; `hadolint` checks the Dockerfile for errors and `pylint` checks the `app.py` source code for errors.

1. Install `hadolint` following the instructions, [on hadolint's page]( https://github.com/hadolint/hadolint):

    **For Mac:**

    ```bash
    brew install hadolint
    ```

    **For Windows:**

    ```bash
    scoop install hadolint
    ```

2. In your terminal, type: `make lint` to run lint checks on the project code. If you haven’t changed any code, all requirements should be satisfied, and you should see a printed statement that rates your code (and prints out any additional comments):

```bash
------------------------------------
Your code has been rated at 10.00/10
```

That's about it! When working with kubernetes, you may need to install some other libraries, but these instructions will set you up with an environment that can build and deploy Docker containers.

To test out hadolint locally, change to directory that has a Dockerfile, and type the following command: `hadolint Dockerfile`. Nothing will happen if there is no error.  If there is errors or warnings then hadolint will print that out.

## Creating a Lambda function

1. `sam init` Creates a new SAM template project locally in your environment.  Make sure you are in the folder in which you like the lambda function to be built.
2. Choose **AWS Quick Start Templates**
3. Choose **ZIP** or Container (ECR)
4. Follow steps in README files for the project
5. To build your lambda function locally type: `sam build`
    - If using a image container, this command will build a local container that you can test on local docker application.
6. To test container on local machine `same local invoke`
7. When you want to deploy your lambda function from your local machine to amazon, use the following command `sam deploy --guided`. However, if using an image container, create a repository within Elastic Container Repository (aka. ECR).  Here is where you can save your containers.

## Makefiles

A file that groups linux commands.  A main benefit to a Makefile is the ability to enforce a convention. If everytime you work a project you follow a few simple steps, it reduces the possibility of errors in building and testing a project. The general idea is that a convention eliminates the need to think about what to do. For every project, there is a common way to install software, a common way to test software and a common way to test and lint software.

A typical Python project can be improved by adding a Makefile with the following steps: make setup, make install, make test, make lint and make all. You can run the entire make file or run sections of the make file. For example:

![Makefile Image](./img/Makefile.png)

*setup*, *install*, *test*, *lint* are command grouping in the makefile. To run, for instance, just the setup commands you would: 1) cd into where the Makefile is located, and 2) type in your terminal `make setup`.  To run all commands you would type `make all`.

### Makefile Creation Recap

Let’s recap the key concepts of creating a Makefile.

- setup: You have seen most of this line before, which is dealing with our Python 3 virtual environment.
- install: This installs the requirements for our environment. In our case, it also install the pytest and pylint libraries used later on in the Makefile.
- test: This is broken into two parts for testing.
  - First, it will use .py files in the tests directory. The -vv flag ensures short test durations are still shown ([Documentation](https://docs.pytest.org/en/latest/usage.html#profiling-test-execution-duration)), while the -cov flag helps to calculate what the test coverage of the code is ([Documentation](https://pypi.org/project/pytest-cov/)) in a given directory.
  - The second line is used to test Jupyter Notebook cells. The --nbval flag makes pytest pay attention to jupyter notebooks ([Documentation](https://nbval.readthedocs.io/en/latest/)).
- lint: This will lint what is in the myrepolib directory, as well as the cli.py and web.py files in our current directory (see video). The --disable=R,C is used to disable the "convention" (C) and "refactor" (R) message classes (see related [Stack Overflow post](https://stackoverflow.com/questions/31907762/pylint-to-show-only-warnings-and-errors)).
- all: You may notice this line looks a little different than the above lines, with the commands on the same line. This will execute our install, lint and test commands.

## Resources

- [Install Pyenv](https://realpython.com/intro-to-pyenv/).  The purpose of **pyenv** is to manage multiple versions of python.  Different python packages (e.g., pandas, scikit-learn, plotly) require a certain version(s) of python to function correctly (assuming underlying structure and code).  Traditionally system packages (i.e. brew for MacOS, apt for Ubuntu Linux, yum for Debian linux) install packages for the whole system, for all users.  As developers, we need different version of python based on what project we are working on. So we need access packages store at the user level and for the situation needed.  Pyenv installs at the users level, and allows you to create virtual environments so you can use different version in different situations.
- [PyPI](https://pypi.orgcl) Python packages that pip can download and install are on this package repository. It is a good place to review to understand the purposes of package, their licenses, and why people use them.
