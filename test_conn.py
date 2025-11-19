# test_conn.py
import os
import sys
import psycopg2
from urllib.parse import urlparse

# Use DATABASE_URL from environment (set in CI). Fallback to local default.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://test:test@127.0.0.1:5432/testdb"
)

# psycopg2 requires separate args; parse if provided as a URL
def connect_from_url(url: str):
    parsed = urlparse(url)
    # urlparse for postgresql returns scheme 'postgresql' or 'postgres'
    dbname = parsed.path.lstrip("/")
    user = parsed.username
    password = parsed.password
    host = parsed.hostname
    port = parsed.port or 5432
    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

try:
    conn = connect_from_url(DATABASE_URL)
    conn.close()
    print("CONNECT OK")
except Exception as exc:
    print("CONNECT ERROR:", exc)
    # exit non-zero so pytest treats this as a failure
    sys.exit(1)
