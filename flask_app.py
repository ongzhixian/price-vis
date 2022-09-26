import logging
import signal

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from app.logger import Logger
from app import my_app

http_server = WSGIServer(('', 5000), my_app, handler_class=WebSocketHandler)

def setup_logging():
    logging.getLogger('pika').setLevel(logging.WARNING)
    logging.getLogger('geventwebsocket').setLevel(logging.INFO)
    log = Logger()
    return log


def signal_handler(signal_number, frame):
    if signal_number == signal.SIGINT \
        or signal_number == signal.SIGTERM:
        http_server.close()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    log = setup_logging()
    log.info("Program start", source="program", event="start")
    http_server.serve_forever()
    log.info("Program complete", source="program", event="complete")
