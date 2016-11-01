#!/bin/bash

while ! nc -z pgsql 5432; do sleep 1; done

gunicorn --reload -c /src/gunicorn/config.py app:api
