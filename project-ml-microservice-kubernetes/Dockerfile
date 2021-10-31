FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
WORKDIR /Uda4proj

## Step 2:
# Copy source code to working directory
COPY . app.py /Uda4proj/

## Step 3:
# Install packages from requirements.txt

RUN pip install --no-cache-dir requirements.txt

# hadolint ignore=DL3013

## Step 4:
# Expose port 80

EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]

