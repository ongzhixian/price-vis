import logging
import json
from datetime import datetime

from flask import g, render_template, request, session, redirect

# def handle_websocket(ws):
#     message = ws.receive()
#     if message is not None:
#         message = json.loads(message)

#         r  = "I have received this message from you : %s" % message
#         r += "<br>Glad to be your webserver. %s" % datetime.now()
#         ws.send(json.dumps({'output': r}))


def handle_websocket(ws):
    while True:
        message = ws.receive()
        if message is None:
            break
        else:
            message = json.loads(message)

            r  = "I have received this message from you : %s" % message
            r += "<br>Glad to be your webserver. %s" % datetime.now()
            ws.send(json.dumps({'output': r}))