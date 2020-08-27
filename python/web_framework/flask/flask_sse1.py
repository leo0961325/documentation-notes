"""
2018/05/16
https://flask-sse.readthedocs.io/en/latest/quickstart.html

$ python --version
Python 3.6.3 :: Anaconda, Inc.

$ pip freezes
Flask==0.12.2
Flask-SSE==0.2.1
gevent==1.2.2
gunicorn==19.8.1
redis==2.10.6

$ gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000
# (不知道為啥... 如果用 Ubuntu 內建的 python3.5 無法正常啟動...)

127.0.0.1:5000/
127.0.0.1:5000/hello
"""
from flask import Flask, render_template
from flask_sse import sse

app = Flask(__name__)
app.debug = True
app.config["REDIS_URL"] = "redis://127.0.0.1"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("flask_sse1.html")

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

if __name__ == '__main__':
    app.run()
