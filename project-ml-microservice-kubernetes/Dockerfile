FROM python:3.7.3-stretch

## Step 1:
WORKDIR /app

## Step 2:
# Copy the app to the working directory
COPY . app.py /app/

## Step 3:
# Install all dependencies specified in requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

## Step 4:
EXPOSE 80

## Step 5:
CMD ["python", "app.py"]
