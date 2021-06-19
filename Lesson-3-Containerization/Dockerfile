FROM python:latest


ENV FLASK_ENV "development"

RUN mkdir /app /app/nlib

COPY ext /app

ADD flask_app/* /app/

ADD nlib/* /app/nlib/

COPY csvcli.py /app

COPY requirements.txt /app

WORKDIR /app

RUN python -m pip install --upgrade pip &&\
    python -m pip install -r requirements.txt 

EXPOSE 5001    

CMD ["python", "web.py"]
                    





