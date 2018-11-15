# Web Server - Nginx
- [官方 Beginner’s Guide](http://nginx.org/en/docs/beginners_guide.html)



```sh
$ uname -r
3.10.0-693.21.1 el7.x86_64

$ nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips 26 Jan 2017
```



# 組態的最基本寫法

組態檔的撰寫方式, 由一系列的 **directive** 所組成. 而此 **directive** 分為2類:
- `simple directive` : **分號結尾**
- `block directive`  : 會有一組 `{}` 把東西包起來, 而裡面可以含有 `simple directive` 及 `block directive`

最內層的 `block directive` 只會有2種：**http** 及 **event**, 而文件(.conf)內, 不在 `block directive` 裡面的稱為 `main context`

```conf
# 此範疇落於 main context
prop1   aaa
prop2   bbb

# event block directive
events {
    prop8   hhh
}

# http block directive
http {
    # http 內可有多個 server block directive
    server {
        prop3     ccc

        # server 內可有多個 location block directive
        location {
            prop4   ddd
        }

        # server 內可有多個 location block directive
        location {
            prop5   eee
        }
    }

    # http 內可有多個 server block directive
    server {
        prop6   fff
        location {
            prop7 ggg
        }
    }
}
```



# 設定檔

- 設定主檔 : `/etc/nginx/nginx.conf`
- 設定副檔目錄 : `/etc/nginx/nginx.d/*.conf`
- Ubuntu 的設定副檔玩法 :
    - `/etc/nginx/sites-available/*.conf`       設定軟連結到 sites-enabled/xxx.conf
    - `/etc/nginx/sites-enabled/*.conf`         在 nginx.conf 增加引用目錄到此目錄

```conf
user  nginx;                            # worker processes 使用的 user ,group 的 credentials
worker_processes  1;                    # 可設成 auto, 建議設定成 CPU 核心數量, 但可參考 disk driver, load-balance 來設定
error_log  /tmp/nginx/error.log warn;   # Error Log 紀錄位置 及其 Log-Level
pid        /var/run/nginx.pid;          # 就 pid

events {
    worker_connections  1024;           # 一個 worker_process 可建立的連線數(包含 proxied servers 之間的連線, 不僅限於 client 端的連線)
}

http {
    include       /etc/nginx/mime.types;            # 套用 mime 別名檔
    default_type  application/octet-stream;         # (不懂啊~~~)

    # Log Format... 恩! 需要再看
    # 此 log_format 取名為 main
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;    # 存取紀錄, 套用 main 格式
    sendfile        on;                             # 使用 Linux 底層的 aio...(不懂的話就別動它)
    #tcp_nopush     on;                             # sendfile on 的話才能用, 至於它幹嘛我不知道
    keepalive_timeout  65;                          # 連線建立的持續時間
    #gzip       on;                                 # 壓縮 response (假如CPU強大且網路流量相對吃緊的話, 值得這麼作)
    include /etc/nginx/conf.d/default.conf;         # 引入設定副檔 or 目錄
}
```



# 範例

## Static Content - 靜態資源服務

```ini
# 若此設定檔只有此 「server { ... }」, 則此同時稱為 default server
server {
    listen                  80;         # 若為 default server, 此行隱含了 「listen       80 default_server;」
    server_name             localhost;  # Request Http header 為 localhost 者, 套用此 server, 否則找 default server
    client_max_body_size    1024M;      # 

    location / {        # URL pattern: /
        root        /data/www;          # 存取 /data/www/...
    }

    location /hello {   # URL pattern: /hello
        index       index.html index.php;   # 若 index.html 不存在, 重導至 index.php
    }

    location /images/ {     # URL pattern: /images/
        root        /data;                  # 存取 /data/images/...
    }

    location /index {    # URL pattern: /index
        root        e:\wwwroot;         # 若 URL 符合此 location pattern, 則 RootDocument 為 e:\wwwroot
        index       index.html;         # 設定首頁
    }
}
```

- ex: `http://localhost/images/example.png`, 會存取 `/data/images/example.png`
- ex: `http://localhost/some/example.html`, 會存取 `/data/www/some/example.html`


## Proxy Server - 代理模式

### Proxy Server 範例1

- [nginx 基礎設定教學](https://blog.hellojcc.tw/2015/12/07/nginx-beginner-tutorial/)

```ini
server {
    listen          80;     # 把 proxy server 掛在 本地端 80 port
    server_name     _;      # external address

    location / {
        # Nginx設定為 "代理模式" , 代理本地 8000 port, 後便可透過 public network訪問 Flask web app了
        proxy_pass  http://127.0.0.1:8000;
    }
}
```

### Proxy Server 範例2

- [Nginx Beginner Guide](https://nginx.org/en/docs/beginners_guide.html)

```ini
# 代理伺服器 Proxy Server
server {
    location / {    # 其餘則導向 Proxied Server
        proxy_pass  http://localhost:8080;
    }

    # (與下者雷同), Regular Expression 使用 ~ 開頭
    location ~ \.(gif|jpg|png)$ {   # 若請求靜態文件, .gif, .jpg, .png, 從 /data/images/ 去找
        root        /data/images;
    }
    # (與上者雷同)
    # location /images/ { # URL pattern: /images/
    #     root /data;         # 存取 /data/images/...
    # }
}

# 被代理的伺服器 Proxied Server
server {
    listen      8080;           # Redirect 窗口
    root        /data/up1;      # 東西都放在 /data/up1/...

    location / {
        # do something...
    }
}
```


### 不管啥網頁, 都找首頁 範例3

```ini
# 被代理的伺服器 Proxied Server
server {
    listen      80;
    root        /usr/share/nginx/html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```


## Load-Balance - 負載平衡模式
```ini
# 作 Load-balance 到兩個 Node
upstream test {
    server localhost:8080;
    server localhost:8081;
}

server {  
    # 監聽 本地 80 port 的請求
    listen       80;
    server_name  localhost;   

    # request body 上限大小
    client_max_body_size 1024M;

    location / {
        # 代理 localhost:8080
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host:$server_port;
    }
}
```


### weight
設定訪問比重(不同 Server, 效能不一樣)

```ini
upstream test {
    server 192.168.10.10:8080 weight=5; 
    server 192.168.10.11:8080 weight=2;
}
```


### ip_hash
因為上述的 Load-balance, 會有 `登入後, 資料存在 session`, 再發送請求時, 跳到不同 Server的情況(需要重新登入阿), 所以`要限定同 Client, 訪問同 Server` → 製作 `ip_hash`

```ini
upstream test {
    ip_hash;
    server 192.168.10.10:8080 weight=9; # 訪問比重
    server 192.168.10.11:8081 weight=1; # 訪問比重
}
```


# error.log

```conf
# http://blog.51cto.com/chenx1242/1769724

2018/07/19 11:38:03 [notice] 1989#1989: signal process started
# 原本程序已經啟用了, 但又被重新啟用 (非嚴重錯誤)
```

# access.log


# 零碎概念

Nginx支援 `熱啟動`, 所以改完組態檔後, **不用重啟服務**, 重讀組態即可!!
```sh
# 重讀組態
$ nginx -s reload
```
