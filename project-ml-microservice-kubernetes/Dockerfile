# syntax=docker/dockerfile:1

FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
# Tells Docker to use this path as the default location for all subsequent commands
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY . app.py /app/

## Step 2a:
# See what files are in the container
RUN ls -lha

## Step 3:
# Install packages from requirements.txt
#hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

## Step 4:
# Expose port 80
EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
