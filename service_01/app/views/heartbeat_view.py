from app import flask_app as app
import json
from datetime import datetime


@app.route("/heartbeat")
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Service_01",
            "timestamp": f"{datetime.now()}"
        }
    )
