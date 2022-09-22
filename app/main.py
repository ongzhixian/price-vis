import logging

from logger import Logger
from web_application import setup_web_application

def setup_logging():
    logging.getLogger('pika').setLevel(logging.WARNING)
    log = Logger()
    return log

if __name__ == "__main__":
    log = setup_logging()
    web_application = setup_web_application()
    web_application.run(host='0.0.0.0', port=31000, debug=True)
    log.info("Program complete", source="program", event="complete")
