#!/bin/bash

# Wait database is online

echo "[DEBUG] > Check database availability"
python - "$DB_CONN_STRING" <<END
import sys, psycopg2, time
from urlparse import urlparse

maxTries = 10

parsed = urlparse(sys.argv[1])
user = parsed.username
password = parsed.password
host = parsed.hostname
port = parsed.port
database = parsed.path.strip('/')

while True:
    try:
        if maxTries == 0:
            sys.exit(0)
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
        break
    except:
        --maxTries
        time.sleep(1)
END
echo "[DEBUG] > Database is ready."

# Apply migrations if needed
echo "[DEBUG] > Apply migrations."
alembic upgrade head

# Launch server
echo "[DEBUG] > Launch server."
gunicorn --reload -c /src/gunicorn/config.py app:api
