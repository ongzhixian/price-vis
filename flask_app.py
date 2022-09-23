import logging

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from app.logger import Logger
from app import my_app


def setup_logging():
    logging.getLogger('pika').setLevel(logging.WARNING)
    logging.getLogger('geventwebsocket').setLevel(logging.INFO)
    log = Logger()
    return log

if __name__ == "__main__":
    log = setup_logging()
    http_server = WSGIServer(('', 5000), my_app, handler_class=WebSocketHandler)
    http_server.serve_forever()
    log.info("Program complete", source="program", event="complete")
