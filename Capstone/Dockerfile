FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
RUN mkdir /app
WORKDIR /app
## Step 2:
# Copy source code to working directory
COPY . /app

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN python -m pip install --upgrade pip &&\
    pip install -r requirements.txt

## Step 4:
# Expose port 80
EXPOSE 80

## Step 5:
# Run app.py at container launch
ENV FLASK_ENV="development"
CMD [ "python", "app.py" ]

