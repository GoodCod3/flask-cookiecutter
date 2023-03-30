FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY code/requirements.txt requirements.txt

COPY . /code

RUN python3.8 -m pip install --upgrade pip

RUN python3.8 -m pip install -r requirements.txt

EXPOSE 5000
