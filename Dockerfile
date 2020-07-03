FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
WORKDIR /code

COPY requirements/base.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

