import psycopg2
import sys

try:
    conn = psycopg2.connect(
        "host=127.0.0.1 port=5433 user=test password=test dbname=testdb"
    )
    print("CONNECTED OK")
    conn.close()
except Exception as e:
    print("CONNECT ERROR:", type(e).__name__, e)
    sys.exit(1)
