# official python 3 image
FROM python:3.7.3-stretch

## Complete Step 1:
# Create a Working Directory
# Sets the working name of the container
# Command: WORKDIR /<directory name on container>
WORKDIR /app

## Complete Step 2:
# Copy source code to working directory
# Command: COPY <source local machine> <destination on container>
COPY ./app.py /app/

## Complete Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
# Note the && allows you to run multiple commands
# I wonder if you could send in a script file?
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

## Complete Step 4:
# Expose port 80

## Complete Step 5:
# Run app.py at container launch
