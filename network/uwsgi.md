# uwsgi  v2.0.17.1
- 2018/07/17


```py
# 這是一個 遵從 WSGI 的 application
# foobar.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # 這是 Python3
```


```sh
# 預設來講, uWSGI Python Loader 會去找 「Application Function」
# 若有前端程式, 使用 「--http-socket」 代替 「--http」
$ uwsgi --http :9090 --wsgi-file foobar.py
# 見比較圖
```


Client
```sh
$ curl -X GET http://127.0.0.1:9090
Hello World
```

Server
```sh
[pid: 5041|app: 0|req: 4/4] 127.0.0.1 () {28 vars in 288 bytes} [Tue Jul 17 20:23:01 2018] GET / => generated 11 bytes in 0 msecs (HTTP/1.1 200) 1 headers in 44 bytes (1 switches on core 0)
```

Option           | Description
---------------- | --------------
--processes 4    | 4核
--threads 2      | 2緒

```sh
# 4核 && 2緒
$ uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2
# 見比較圖
```

Server
```sh
[pid: 5162|app: 0|req: 1/1] 127.0.0.1 () {28 vars in 288 bytes} [Tue Jul 17 20:46:50 2018] GET / => generated 11 bytes in 0 msecs (HTTP/1.1 200) 1 headers in                               44 bytes (1 switches on core 0)
```

Single vs Multi

![uWSGI Compare](../img/uwsgi_compare.png)




```sh
$ ps aux
# a : 不與 terminal 有關的所有 process
# u : 與 有效使用者 相關的 process
# x : 詳細資訊(通常與 a 一起使用)
#USER     PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
tony      5161  0.0  0.3  48520 12152 pts/10   S+   20:29   0:00 uwsgi --http :9090 --wsgi-file foobar.
tony      5162  0.0  0.3 124832 12160 pts/10   Sl+  20:29   0:00 uwsgi --http :9090 --wsgi-file foobar.
tony      5163  0.0  0.3 124832 12132 pts/10   Sl+  20:29   0:00 uwsgi --http :9090 --wsgi-file foobar.
tony      5164  0.0  0.3 124832 12176 pts/10   Sl+  20:29   0:00 uwsgi --http :9090 --wsgi-file foobar.
tony      5165  0.0  0.3 124832 11864 pts/10   Sl+  20:29   0:00 uwsgi --http :9090 --wsgi-file foobar.
tony      5166  0.0  0.1  48520  6572 pts/10   S+   20:29   0:00 uwsgi --http :9090 --wsgi-file foobar.
...(略)...
```

搭配 Nginx 使用
```conf
location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:3031;      # Pass任何請求到 使用 uwsgi 協議的 3031  port
}
```

Nginx設完後, 將 uWSGI 綁到此端口
```sh
$ uwsgi --socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
```

```sh
$ ps aux
#USER     PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
tony      5161  0.0  0.3  48536 12132 pts/10   S+   21:09   0:00 uwsgi --socket 127.0.0.1:9090 --wsgi-file foobar.py --master --pr
tony      5162  0.0  0.3 124868 11896 pts/10   Sl+  21:09   0:00 uwsgi --socket 127.0.0.1:9090 --wsgi-file foobar.py --master --pr
tony      5163  0.0  0.3 124868 11896 pts/10   Sl+  21:09   0:00 uwsgi --socket 127.0.0.1:9090 --wsgi-file foobar.py --master --pr
tony      5164  0.0  0.3 124868 11896 pts/10   Sl+  21:09   0:00 uwsgi --socket 127.0.0.1:9090 --wsgi-file foobar.py --master --pr
tony      5165  0.0  0.3 124868 11896 pts/10   Sl+  21:09   0:00 uwsgi --socket 127.0.0.1:9090 --wsgi-file foobar.py --master --pr
# 少了一個 process, HTTP router, uwsgi protocol
...(略)...
```


```sh
$ uwsgi --socket 127.0.0.1:3031 --chdir /home/tony/tmp/ --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
# 可用 --chdir 改路徑 
#--wsgi-file 一樣指向 application function
```


```sh
# 直接起 server
# $ uwsgi --http :8000 --chdir /home/tony/bis_emc/bis_emc/ --wsgi-file bis_emc/wsgi.py --master --processes 4 --threads 2 --module q.ini


# 使用 TCP Port Socket
$ uwsgi --socket :8001 --wsgi-file test.py
$ uwsgi --socket :8001 --chdir /home/tony/bis_emc --wsgi-file bis_emc/wsgi.py

# 使用 Unix Socket
### mysite
$ uwsgi --socket bis.sock --wsgi-file  test.py
$ uwsgi --socket bis.sock --chdir /home/tony/mysite --wsgi-file mysite/wsgi.py

### bis_emc
$ uwsgi --socket bis.sock --chdir /home/tony/bis_emc --wsgi-file bis_emc/wsgi.py
$ uwsgi --socket bis.sock --chdir /home/tony/bis_emc --module bis_emc.wsgi

### bis_emc 吃 ini
$ 
```



- 「--http :8000」 : 使用 http 協定, 8000 port
- 「wsgi-file test.py」 : 讀取 test.py 內的 application function (wsgi app)
- 「--module mysite.wsgi」 : 改以載入 wsgi.py 的方式
- 「socket :8001」 : 使用 uwsgi 協定, 8001 port



```conf
# /etc/nginx/sites-available/bis.conf
# 777 root root

upstream django {
    server    unix:///home/tony/bis_emc/bis.sock;       # 以 Unix Socket 的方式連線
    # server    unix:///home/tony/mysite/bis.sock;      # 以 TCP Socket 的方式連線

    # server    127.0.0.1:8000;
}

server {
    listen                  80;                     # 此電腦聆聽 80 port 請求

    server_name             localhost;              # 

    charset                 utf-8;                  # 就... UTF8

    client_max_body_size    75M;                    # 

    access_log              /home/tony/access.log;  # 不解釋
    error_log               /home/tony/error.log;   # 不解釋

    location /static {      # 靜態文件的反代理
        alias       /home/tony/bis_emc/static;      # 靜態文件位置
    }

    location / {    # 除了上面的 「location /xxx」以外的請求, 都來這
        uwsgi_pass          django;                 # 交由 django 這個 upstream來處理, 且此 upstream 為 uwsgi
        include             uwsgi_params;           # /etc/nginx/uwsgi_params  其實我也不懂
    }
}
```

```conf
# /etc/systemd/system/bis.service
# 644 root root

[Unit]

Description=uWSGI instance to serve bis     # 此服務的說明

After=network.target                        # 此服務接續在 network.target 之後啟動


[Service]

User=tony

Group=tony

WorkingDirectory=/home/tony/bis_emc/bis_emc                     # 服務的位置

Environment=/home/tony/.virtualenvs/bis/bin                     # 服務的啟動環境

ExecStart=/home/tony/.virtualenvs/bis/bin/uwsgi --ini bis.ini   # 服務要啟動的目標


[Install]

WantedBy=multi-user.target
```

```ini
# /home/tony/bis_emc/bis.ini
# 664 tony tony

[uwsgi]
master = true           # 忘了
processes = 1           # 1核
threads = 2             # 2緒 (較佳的情況為 threads=processes*2)

chdir = /home/tony/bis_emc/bis_emc      # 專案位置

socket = bis.sock                       # socket位置

wsgi-file = bis_emc/wsgi.py             # WSGI callable

chmod-socket = 664                      # 忘了...

home = /home/tony/.virtualenvs/bis      # Python 虛擬環境位置

vacuum = true                           # Service離開後, 自動清理 Unix Socket

buffer-size = 30000                     # 
```

```s
# /home/tony/bis_emc/
    # 664 tony tony bis.ini
    # 664 tony tony manage.py
    # bis_emc/
        # 664 tony tony settings.py
        # ...
    # ...
```

```py
# settings.py
# ...

# 不知道為什麼需要這樣作
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.124.108']

# ...
```