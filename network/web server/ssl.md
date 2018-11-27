# SSL - HTTPS

- 2018/11/20
- [SSL For Free](https://www.sslforfree.com/)


# Apache 手動篇

1. DNS 設好 A 紀錄

Name   | Type | Value       | TTL
------ | ---- | ----------- | ---
`FQDN` | A    | (PUBLIC IP) | 60

2. 啟動你的 Web Server, 開防火牆, Permission, SELinux(if Enforcing)
3. 修改你的 `/etc/hosts` (假設為 `demo`)
4. 前往 [SSL For Free](https://www.sslforfree.com/), 填寫 FQDN (`demo.DOMAIN`)
5. Manual Verification
    1. Download File (檔案裏頭一堆看不懂的 `HASH`), 假設該檔名為 Zr2Q7
    2. 放到 Web Server 站台的 {DocumentRoot}/.well-known/acme-challenge/Zr2Q7
    3. 啟動你的 Web Server
    4. 開防火牆, 權限, SELinux(if Enforcing)
    5. 瀏覽器進入你的 Web Server (http://YOUR_FQDN/.well-known/acme-challenge/Zr2Q7), 應該能看到一堆 `HASH`
    6. 點選 `Download SSL Certificate`
        1. 將 Certificate 存成 `xxx.crt`
        2. 將 Private Key 存成 `yyy.key`
        3. 將 CA Bundle 存成 zzz.crt (不知道啥場合用得到它...)
    7. yum install -y mod_ssl
    8. 編輯 `/etc/httpd/conf.d/ssl.conf`
        1. SSLCertificateFile 設定為 `xxx.crt` 的完整路徑
        2. SSLCertificateKeyFile 設定為 `yyy.key` 的完整路徑
    9. 重啟 httpd
    10. https://YOUR_FQDN   新鮮的 https 出爐~

# Apache Letsencrypt

- 2018/11/26
- https://certbot.eff.org/lets-encrypt/centosrhel7-apache

## 1. 安裝
```sh
yum -y install yum-utils
yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional
yum install -y python2-certbot-apache
```

## 2. 設定 apache && hostname && domain

1. DNS  - A record (或使用 /etc/hosts)
2. hostnamectl set-hostname (這好像可以不要用...)
3. 設定 VirtualHost `/etc/httpd/conf.d/vhost.conf`
4. https `yum install mod_ssl`

## 3. vhost

### 3-1. apahce config

```conf
<VirtualHost *:80>
    DocumentRoot    /srv/demo/www
    ServerName      demo.youwillneverknow.com
    ErrorLog        "logs/demo_error_log"
    CustomLog       "logs/demo_access_log" combined
</VirtualHost>
<Directory /srv/demo/www>
    Require all granted
</Directory>

<VirtualHost *:80>
    DocumentRoot    /srv/www/www
    ServerName      www.youwillneverknow.com
    ErrorLog        "logs/www_error_log"
    CustomLog       "logs/www_access_log" combined
</VirtualHost>
<Directory /srv/www/www>
    Require all granted
</Directory>
```

### 3-2. html

```sh
mkdir -p /srv/{demo,www}/www
chmod 2774 -p /srv
chown -R apache /srv

# 在兩資料夾內建立各自的 html
# restart httpd
```

### 3-3. security

1. SELinux
2. firewall
3. Authentication (read && access for apache)

## 4. 設定 letsencrypt

```sh
$# certbot --apache
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator apache, Installer apache
Starting new HTTPS connection (1): acme-v02.api.letsencrypt.org

Which names would you like to activate HTTPS for?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: demo.youwillneverknow.com
2: www.youwillneverknow.com
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel):
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for demo.youwillneverknow.com
http-01 challenge for www.youwillneverknow.com
Waiting for verification...
Cleaning up challenges
Created an SSL vhost at /etc/httpd/conf.d/vhost-le-ssl.conf
Deploying Certificate to VirtualHost /etc/httpd/conf.d/vhost-le-ssl.conf
Created an SSL vhost at /etc/httpd/conf.d/vhost-le-ssl.conf
Deploying Certificate to VirtualHost /etc/httpd/conf.d/vhost-le-ssl.conf

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 1

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations! You have successfully enabled https://demo.youwillneverknow.com and
https://www.youwillneverknow.com

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=demo.youwillneverknow.com
https://www.ssllabs.com/ssltest/analyze.html?d=www.youwillneverknow.com
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/demo.youwillneverknow.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/demo.youwillneverknow.com/privkey.pem
   Your cert will expire on 2019-02-24. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
```

成功!!

## 5. Auto-encrypt

```sh
### 純測試
certbot renew --dry-run

### 手動執行 auto-renew encrypt
certbot renew
```

寫到 crontab 吧~



# Nginx Letsencrypt

## 1. 安裝

```sh
yum -y install yum-utils
yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional
yum install -y python2-certbot-nginx
```

## 2. config

```conf
server {
    listen          80;
    root            /data/www;
    server_name     www.youwillneverknow.com;
    location / {
    }
}


server {
    listen          80;
    server_name     demo.youwillneverknow.com;
    root            /data/demo;
    location / {
    }
}

```


## 3. 資源

```sh
mkdir -p /data/{www,demo}
# Permission
# Owner(nginx)
# 0755
# firewall
# SELinux
# 放資源
```

## 4. letsencrypt

```sh
$# certbot --nginx
# 然後就很簡單了
```

## 5. auto encrypt

```sh
certbot renew --dry-run     # 玩假的
certbot renew               # 玩真的

crontab -e 
0 0,12 * * * python -c 'import random; import time; time.sleep(random.random() * 3600)' && certbot renew 
```


