import logging

from flask import g, render_template, request, session, redirect, abort
from geventwebsocket import WebSocketServer, WebSocketError
from app import app

@app.route('/')
def root_get():
    return render_template('index.html')


# @app.route('/api2')
# def api(ws, a, b):
#     breakpoint()
#     ws = request.environ.get('wsgi.websocket')
#     print("in api2")
#     print(ws)

#     if not ws:
#         abort(400, "Expected WebSocket request")

#     while True:
#         try:
#             message = ws.receive()
#             ws.send("Your message was: {}".format(message))
#         except WebSocketError:
#             # Possibility to execute code when connection is closed
#             break
