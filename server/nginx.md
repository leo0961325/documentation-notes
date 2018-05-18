# Nginx
- [官方 Beginner’s Guide](http://nginx.org/en/docs/beginners_guide.html)
- [nginx 基礎設定教學](https://blog.hellojcc.tw/2015/12/07/nginx-beginner-tutorial/)



```sh
$ uname -r
3.10.0-693.21.1 el7.x86_64

$ nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips 26 Jan 2017
```



## 主要設定檔 /etc/nginx/nginx.conf

初始內容如下:
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

此組態檔的撰寫方式, 是由一系列的 **directive** 所組成. 而此 **directive** 分為2類:
- simple directive: 分號結尾
- block directive: 會有一組 `{}` 把東西包起來, 而裡面可以含有 `simple directive` 及 `block directive`

ex:
```conf
http {
  # server 一定在 http 裡面
  server {
    # location 一定在 server 裡面
    location {}
  }
}
```


最內層的 `block directive` 只會有2種：**http** 及 **event**, 稱之為 `main context` (不懂這句話...)
