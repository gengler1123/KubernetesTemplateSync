from app import flask_app as app
import os

print("Env Vars")
print(os.environ.get("service-01"))
print(os.environ.get("service-01-api"))

@app.before_first_request
def load_app():
    print("Loading App Before First Request")


from .heartbeat_view import *
from .main_view import *