# [gunicorn](http://gunicorn.org/)
- 純 Python 的 Web Server
- 2018/05/18
- [Does Gunicorn run on Windows(從2013年以後, 好像可以了!?)](https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- [python gunicorn 官方](https://pypi.org/project/gunicorn/)
- [這篇寫得不錯](https://jiayi.space/post/flask-gunicorn-nginx-bu-shu)
- [快餐範例](https://www.jianshu.com/p/fbe8ffd76e5a)
- 人稱它為 `Green Unicorn` 綠色獨角獸 (這好像不是很重要...)

> Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. 
> The Gunicorn server is broadly compatible with various web frameworks, 
> simply implemented, light on server resources, and fairly speedy.

# 安裝
如果需要做到異部請求, 那還得額外再安裝類似 `Eventlet` or `Gevent` 等等的異部 worker.
```
pip install greenlet
pip install eventlet
pip install gunicorn eventlet
pip install gevent
pip install gunicorn gevent
```

# gunicorn

```bash
$# gunicorn --version
gunicorn (version 20.0.4)

$# gunicorn --help
usage: gunicorn [OPTIONS] [APP_MODULE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program''s version number and exit
  -c CONFIG, --config CONFIG
                        The Gunicorn config file. [None]
  -b ADDRESS, --bind ADDRESS
                        The socket to bind. [['127.0.0.1:8000']]
  --backlog INT         The maximum number of pending connections. [2048]
  -w INT, --workers INT
                        The number of worker processes for handling requests.
                        [1]
  -k STRING, --worker-class STRING  # 預設為 sync, 此外還可使用: eventlet / gevent / tornado
                        The type of workers to use. [sync]
  --threads INT         The number of worker threads for handling requests.
                        [1]
  --worker-connections INT  # 只對 eventlet / gevent 有作用
                        The maximum number of simultaneous clients. [1000]
  --max-requests INT    The maximum number of requests a worker will process
                        before restarting. [0]
  --max-requests-jitter INT
                        The maximum jitter to add to the *max_requests*
                        setting. [0]
  -t INT, --timeout INT
                        Workers silent for more than this many seconds are
                        killed and restarted. [30]
  --graceful-timeout INT
                        Timeout for graceful workers restart. [30]
  --keep-alive INT      The number of seconds to wait for requests on a Keep-
                        Alive connection. [2]
  --limit-request-line INT
                        The maximum size of HTTP request line in bytes. [4094]
  --limit-request-fields INT
                        Limit the number of HTTP headers fields in a request.
                        [100]
  --limit-request-field_size INT
                        Limit the allowed size of an HTTP request header
                        field. [8190]
  --reload              Restart workers when code changes. [False]
  --reload-engine STRING
                        The implementation that should be used to power
                        :ref:`reload`. [auto]
  --reload-extra-file FILES
                        Extends :ref:`reload` option to also watch and reload
                        on additional files [[]]
  --spew                Install a trace function that spews every line
                        executed by the server. [False]
  --check-config        Check the configuration. [False]
  --preload             Load application code before the worker processes are
                        forked. [False]
  --no-sendfile         Disables the use of ``sendfile()``. [None]
  --reuse-port          Set the ``SO_REUSEPORT`` flag on the listening socket.
                        [False]
  --chdir CHDIR         Chdir to specified directory before apps loading.
                        [/Users/tony/proj/demo_python/demo_sse]
  -D, --daemon          Daemonize the Gunicorn process. [False]
  -e ENV, --env ENV     Set environment variable (key=value). [[]]
  -p FILE, --pid FILE   A filename to use for the PID file. [None]
  --worker-tmp-dir DIR  A directory to use for the worker heartbeat temporary
                        file. [None]
  -u USER, --user USER  Switch worker processes to run as this user. [501]
  -g GROUP, --group GROUP
                        Switch worker process to run as this group. [20]
  -m INT, --umask INT   A bit mask for the file mode on files written by
                        Gunicorn. [0]
  --initgroups          If true, set the worker process''s group access list
                        with all of the [False]
  --forwarded-allow-ips STRING
                        Front-end''s IPs from which allowed to handle set
                        secure headers. [127.0.0.1]
  --access-logfile FILE
                        The Access log file to write to. [None]
  --disable-redirect-access-to-syslog
                        Disable redirect access logs to syslog. [False]
  --access-logformat STRING
                        The access log format. [%(h)s %(l)s %(u)s %(t)s
                        "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"]
  --error-logfile FILE, --log-file FILE
                        The Error log file to write to. [-]
  --log-level LEVEL     The granularity of Error log outputs. [info]
  --capture-output      Redirect stdout/stderr to specified file in
                        :ref:`errorlog`. [False]
  --logger-class STRING
                        The logger you want to use to log events in Gunicorn.
                        [gunicorn.glogging.Logger]
  --log-config FILE     The log config file to use. [None]
  --log-config-dict LOGCONFIG_DICT
                        The log config dictionary to use, using the standard
                        Python [{}]
  --log-syslog-to SYSLOG_ADDR
                        Address to send syslog messages.
                        [unix:///var/run/syslog]
  --log-syslog          Send *Gunicorn* logs to syslog. [False]
  --log-syslog-prefix SYSLOG_PREFIX
                        Makes Gunicorn use the parameter as program-name in
                        the syslog entries. [None]
  --log-syslog-facility SYSLOG_FACILITY
                        Syslog facility name [user]
  -R, --enable-stdio-inheritance
                        Enable stdio inheritance. [False]
  --statsd-host STATSD_ADDR
                        ``host:port`` of the statsd server to log to. [None]
  --dogstatsd-tags DOGSTATSD_TAGS
                        A comma-delimited list of datadog statsd (dogstatsd)
                        tags to append to statsd metrics. []
  --statsd-prefix STATSD_PREFIX
                        Prefix to use when emitting statsd metrics (a trailing
                        ``.`` is added, []
  -n STRING, --name STRING
                        A base to use with setproctitle for process naming.
                        [None]
  --pythonpath STRING   A comma-separated list of directories to add to the
                        Python path. [None]
  --paste STRING, --paster STRING
                        Load a PasteDeploy config file. The argument may
                        contain a ``#`` [None]
  --proxy-protocol      Enable detect PROXY protocol (PROXY mode). [False]
  --proxy-allow-from PROXY_ALLOW_IPS
                        Front-end''s IPs from which allowed accept proxy
                        requests (comma separate). [127.0.0.1]
  --keyfile FILE        SSL key file [None]
  --certfile FILE       SSL certificate file [None]
  --ssl-version SSL_VERSION
                        SSL version to use. [_SSLMethod.PROTOCOL_TLS]
  --cert-reqs CERT_REQS
                        Whether client certificate is required (see stdlib ssl
                        module''s) [VerifyMode.CERT_NONE]
  --ca-certs FILE       CA certificates file [None]
  --suppress-ragged-eofs
                        Suppress ragged EOFs (see stdlib ssl module''s) [True]
  --do-handshake-on-connect
                        Whether to perform SSL handshake on socket connect
                        (see stdlib ssl module''s) [False]
  --ciphers CIPHERS     SSL Cipher suite to use, in the format of an OpenSSL
                        cipher list. [None]
  --paste-global CONF   Set a PasteDeploy global config variable in
                        ``key=value`` form. [[]]
  --strip-header-spaces
                        Strip spaces present between the header name and the
                        the ``:``. [False]
```



# 概念
> Gunicorn is a `WSGI HTTP server`. It is best to use Gunicorn behind an `HTTP proxy server`. 
> We strongly advise you to use nginx.

基本使用方式
```sh
$ gunicorn [OPTIONS] APP_MODULE

```


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