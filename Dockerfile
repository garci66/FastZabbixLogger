FROM node:alpine as assets

RUN apk add --no-cache git

WORKDIR /usr/src/app

FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache git tzdata

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /usr/src/app/main.py

CMD ["python", "-u", "./main.py"]
