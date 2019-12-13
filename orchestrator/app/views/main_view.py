from app import flask_app as app
from requests import get
import json
from datetime import datetime
import redis
from os import environ
import psycopg2 as psql


@app.route("/")
def main_view():
    """

    """
    service_01_endpoint = environ.get("SERVICE_01_ENDPOINT", "http://service-01:8000")
    service_02_endpoint = environ.get("SERVICE_02_ENDPOINT", "http://service-02:8000")
    redis_endpoint = environ.get("REDIS_ENDPOINT")
    psql_host = environ.get("PSQL_HOST")
    psql_port = environ.get("PSQL_PORT")
    psql_user = environ.get("PSQL_USER")
    psql_pass = environ.get("PSQL_PASS")

    print(f"""
    {service_01_endpoint}
    {service_02_endpoint}
    {redis_endpoint}
    {psql_host}
    {psql_port}
    {psql_user}
    {psql_pass}
""")

    try:
        conn = psql.connect(
            host=psql_host,
            port=int(psql_port),
            user=psql_user,
            password=psql_pass
        )

        conn.close()
        db_message = "Connection Made"
    except Exception as e:
        db_message = f"Exception: {e}"

    r1 = get(f"{service_01_endpoint}/heartbeat")
    if r1.status_code != 200:
        r1_resp = r1.text
    else:
        r1_resp = r1.json()
    r2 = get(f"{service_02_endpoint}/heartbeat")
    if r2.status_code != 200:
        r2_resp = r2.text
    else:
        r2_resp = r2.json()

    try:
        r = redis.StrictRedis(host=redis_endpoint)
        print("Redis Keys")
        print(r.keys())
        values = r.keys()
    except Exception as e:
        values = f"{e}"

    return json.dumps(
        {
            "timestamp": f"{datetime.now()}",
            "service_01_resp": r1_resp,
            "service_02_resp": r2_resp,
            "redis_values": values,
            "db_message": db_message
        }
    )