from flask import Flask
import logging
from os import environ
from redis import StrictRedis

print("\n")
print(f"SERVICE 01 ENDPOINT: {environ.get('SERVICE_01_ENDPOINT')}")
print(f"SERVICE 02 ENDPOINT: {environ.get('SERVICE_02_ENDPOINT')}")
print(f"REDIS ENDPOINT: {environ.get('REDIS_ENDPOINT')}")

logger = logging.getLogger("__PYTHON_REST_API_TEMPLATE__")

flask_app = Flask("__PYTHON_REST_API_TEMPLATE__")

from .views import *
