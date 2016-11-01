FROM python:2.7.12-alpine

MAINTAINER Gabriel Malet

RUN apk update \
    && apk add bash gcc musl-dev python-dev postgresql-dev \
    && rm -rf /var/cache/apk/*

COPY ./scripts/entrypoint.sh /entrypoint.sh
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /src
ADD . /src/

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]