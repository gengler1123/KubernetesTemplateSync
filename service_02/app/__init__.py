from flask import Flask
import logging

logger = logging.getLogger("__PYTHON_REST_API_TEMPLATE__")


flask_app = Flask("__PYTHON_REST_API_TEMPLATE__")


from .views import *
