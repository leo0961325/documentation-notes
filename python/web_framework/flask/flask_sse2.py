"""
on Windows 10

2018/05/16
https://gist.github.com/fisadev/5860754
https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56

$ pip install Flask==0.12.2
$ set FLASK_APP=sse.py
$ flask run

127.0.0.1:5000/streaming
(會 block 請求)
"""
import time
from flask import Response, Flask

app = Flask(__name__)

@app.route('/streaming')
def stream():
    def event_stream():
        while True:
            time.sleep(1)
            yield 'data: %s\n\n' % '~永~不~斷~線~~ 直到永遠永遠永遠永遠~~~~'

    return Response(event_stream(), mimetype="text/event-stream")
