FROM python:2.7.12-alpine

MAINTAINER Gabriel Malet

RUN apk update \
    && apk add gcc musl-dev python-dev postgresql-dev \
    && rm -rf /var/cache/apk/*

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /src
ADD . /src/

EXPOSE 5000

CMD gunicorn --reload -c /src/gunicorn/config.py app:api
