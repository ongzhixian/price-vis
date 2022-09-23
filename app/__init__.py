import os
from flask import Flask

from .websocket import handle_websocket

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='templates')
app.secret_key = os.urandom(24)
app.debug = True

# from app.lifecycle_handlers import *
# from app.websockets import *
from app.pages import *
from app.api import *


def my_app(environ, start_response):
    path = environ["PATH_INFO"]
    if path == "/":
        print("ret1")
        return app(environ, start_response)
    elif path == "/api2":
        print("handle-ws")
        handle_websocket(environ["wsgi.websocket"])
    else:
        print("ret2")
        return app(environ, start_response)