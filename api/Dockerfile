FROM python:2.7.12-alpine

MAINTAINER Gabriel Malet

RUN apk update \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

ADD . /src/
WORKDIR /src

EXPOSE 5000

CMD gunicorn --reload -b 0.0.0.0:5000 app:api
