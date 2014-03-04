import time
from flask import send_file, Response
from web import web_app
import random


@web_app.route('/')
def home():
    return send_file("templates/index.html")


def _stream():
    count = 0
    while True:
        time.sleep(0.3)
        yield """
            retry: 10000\ndata:{"count":%s, "message":%s}\n\n
        """ % (count, '"Random number {}"'.format(random.randrange(999)))
        count += 1

@web_app.route("/stream")
def stream():
    return Response(
        _stream(),
        mimetype='text/event-stream')