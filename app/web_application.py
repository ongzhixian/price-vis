from flask import Flask, render_template, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

def index():
    return render_template('index.html')


def ws_api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            message = ws.wait()
            ws.send(message)

def setup_pages(app):
    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/ws", view_func=ws_api)

def api_test():
    return "api test"

def setup_api(app):
    app.add_url_rule("/api/test", view_func=api_test)

def setup_web_application():
    app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='templates')
    setup_api(app)
    setup_pages(app)
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
    