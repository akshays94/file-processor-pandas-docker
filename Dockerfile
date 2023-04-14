FROM python:3.8.1-slim-buster

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app /app

WORKDIR /app
