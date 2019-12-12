from app import flask_app as app


@app.before_first_request
def load_app():
    print("Loading App Before First Request")


from .heartbeat_view import *
