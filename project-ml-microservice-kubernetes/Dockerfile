FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
<<<<<<< HEAD
WORKDIR /uda4proj

## Step 2:
# Copy source code to working directory
COPY . app.py /uda4proj/
=======
WORKDIR /udacityproj4

## Step 2:
# Copy source code to working directory
COPY . app.py /udacityproj4/
>>>>>>> fe3540decde906ddffeda2709c21280f2eaad169

## Step 3:
# Install packages from requirements.txt

<<<<<<< HEAD

RUN pip install --upgrade pip  &&\
        pip install --no-cache-dir -r  requirements.txt
=======
RUN pip install --no-cache-dir requirements.txt
>>>>>>> fe3540decde906ddffeda2709c21280f2eaad169

# hadolint ignore=DL3013

## Step 4:
# Expose port 80

EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]

