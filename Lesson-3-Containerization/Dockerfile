FROM python:3.7-alpine

WORKDIR /app

COPY ./flask_app .

COPY . nlib /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip3 install -r requirements.txt
        

# Expose port 80
EXPOSE 80

# Run app.py at container launch
CMD ["python", "web.py"]