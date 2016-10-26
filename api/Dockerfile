FROM python:2.7.12-alpine

MAINTAINER Gabriel Malet

RUN apk update \
  && rm -rf /var/cache/apk/*

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /src
ADD . /src/

EXPOSE 5000

CMD gunicorn --reload -b 0.0.0.0:5000 app:api
