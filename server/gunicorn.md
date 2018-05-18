# [gunicorn](http://gunicorn.org/)
- 純 Python 的 Web Server
- 2018/05/18
- [Does Gunicorn run on Windows(從2013年以後, 好像可以了!?)
](https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- 人稱它為 `Green Unicorn` 綠色獨角獸 (這好像不是很重要...)



# 安裝
如果需要做到異部請求, 那還得額外再安裝類似 `Eventlet` or `Gevent` 等等的異部 worker.
```
pip install greenlet
pip install eventlet
pip install gunicorn eventlet
pip install gevent
pip install gunicorn gevent
```



# 概念
> Gunicorn is a `WSGI HTTP server`. It is best to use Gunicorn behind an `HTTP proxy server`. We strongly advise you to use nginx. ( 好像是建議使用 gunicorn + Nginx )



# 語法

test.py
```py
def app(environ, start_response):
    """ simplest possible application obj"""
    data = 'Hello'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

# gunicorn --workers=2 test:app
```

```sh
# gunicorn <module name>:<web app> --worker-class --bind <host>:<port>
# <web app> 為 WSGI callable
$ gunicorn sse:app --worker-class gevent --bind 0.0.0.0:7777

# gunicorn -w <number> <module>:<web app>
# 或 gunicorn --worker <number> <module>:<web app>
$ gunicorn -w 4 myapp:app
```



# 組態

long name                                | example
---------------------------------------- | ------------------------
* Config                                 | 
--config CONFIG <br> -c CONFIG           | <附註1>
--bind ADDRESS <br> -b ADDRESS           | --bind ['127.0.0.1:8000']
* Worker Processes                       | 
--backlog INT                            | --backlog 2048
--workers INT <br> -w INT                | --workers 2 
--worker-class STRING <br> -k STRING     | --worker-class sync <附註2>
--threads INT                            | --threads 1
--worker-connections INT                 | --worker-connections 1000
--max-requests INT                       | --max-requests 0
--timeout INT <br> -t INT                | --timeout 30
--keep-alive INT                         | --keep-alive 2
* Worker Processes                       | 
--limit-request-line INT                 | --limit-request-line 4096
--limit-request-field_size INT           | --limit-request-field_size 8190
* Debugging                              | 
--reload BOOL                            | --reload False
--reload-engine STRING                   | --reload-engine auto <附註3>
--spew BOOL                              | --spew True
* Server Mechanics                       | 
--preload BOOL                           | preload True
--chdir PATH                             | --chdir /home/docs/source
--daemon BOOL <br> -D BOOL               | --daemon True
--env ENV <br> -e ENV                    | --env a=1
--pid FILE <br> -p FILE                  | 
--worker-tmp-dir DIR PATH                |
--forwarded-allow-ips STRING             | --forwarded-allow-ips 127.0.0.1
* Logging                                | 
--access-logfile FILE                    | --access-logfile -
--disable-redirect-access-to-syslog BOOL | --disable-redirect-access-to-syslog True
--log-level LEVEL                        | --log-level info <附註4>
--logger-class STRING                    | --logger-class gunicorn.glogging.Logger
--log-config FILE                        | --log-config None
--log-syslog-to SYSLOG_ADDR              | --log-syslog-to udp://localhost:514.
--log-syslog BOOL                        | --log-syslog False

- 附註1: [ PATH , file:PATH , python:MODULE_NAME ]
- 附註2: [ 'sync' , 'eventlet' , 'gevent', 'tornado' ]
- 附註3: [ 'auto' , 'poll' , 'inotify' ]
- 附註4: [ 'debug' , 'info' , 'warning' , 'error' , 'critical']


```ini
[server:main]
use = egg:gunicorn#main
host = 192.168.0.1
port = 80
workers = 2
proc_name = brim
```


```nginx
# Nginx本身監聽 80 port, 
server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
# Nginx為反代理伺服器 to a Gunicorn server running on localhost port 8000
```


# 環境變數

```sh
$ GUNICORN_CMD_ARGS="--bind=127.0.0.1 --workers=3" gunicorn app:app
```