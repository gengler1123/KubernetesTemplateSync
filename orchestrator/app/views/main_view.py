from app import flask_app as app
from requests import get
import json
from datetime import datetime
import redis
from os import environ


@app.route("/")
def main_view():
    """

    """
    r1 = get("http://service-01:8000/heartbeat")
    if r1.status_code != 200:
        r1_resp = r1.text
    else:
        r1_resp = r1.json()
    r2 = get("http://service-02:8000/heartbeat")
    if r2.status_code != 200:
        r2_resp = r2.text
    else:
        r2_resp = r2.json()

    try:
        r = redis.StrictRedis(host=environ.get("REDIS_ENDPOINT"))
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
            "redis_values": values
        }
    )