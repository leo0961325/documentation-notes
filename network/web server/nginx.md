# Web Server - Nginx
- [官方 Beginner’s Guide](http://nginx.org/en/docs/beginners_guide.html)
- [nginx 基礎設定教學](https://blog.hellojcc.tw/2015/12/07/nginx-beginner-tutorial/)
- [Nginx應用場景(簡單明瞭的範例)](http://www.raye.wang/2017/02/24/quan-mian-liao-jie-nginxdao-di-neng-zuo-shi-yao/)

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

最內層的 `block directive` 只會有2種：**http** 及 **event**, 稱之為 `main context`

```conf
http {
  server {
    location {}
  }
}
```



# 主要設定檔 /etc/nginx/nginx.conf

```conf
user  nginx;  
worker_processes  1;
error_log  /tmp/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    #tcp_nopush     on;
    keepalive_timeout  65;
    #gzip       on;
    include /etc/nginx/conf.d/default.conf;
}
```



# 範例
## 靜態資源服務

```conf
server {
    listen       80;                                                         
    server_name  localhost;                                               
    client_max_body_size 1024M;

    location / {
        root   e:\wwwroot;  # 若訪問到 url, 則回傳 Host端 e:\wwwroot2 底下的東西
        index  index.html;  # 設定首頁
    }
}
```


最內層的 `block directive` 只會有2種：**http** 及 **event**, 稱之為 `main context` (不懂這句話...)


## 代理模式
```conf
server {
  listen 80;      # 把 proxy server 掛在 本地端 80 port
  server_name _;  # external address

  location / {
    proxy_pass http://127.0.0.1:8000;   # Nginx設定為 "代理模式" , 代理本地 8000 port, 後便可透過 public network訪問 Flask web app了
  }
}
```

## Load-Balance
```conf
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

```conf
upstream test {
    server 192.168.10.10:8080 weight=5; 
    server 192.168.10.11:8080 weight=2;
}
```


### ip_hash
因為上述的 Load-balance, 會有 `登入後, 資料存在 session`, 再發送請求時, 跳到不同 Server的情況(需要重新登入阿), 所以`要限定同 Client, 訪問同 Server` → 製作 `ip_hash`

```conf
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
