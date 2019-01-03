
```sh
$# docker search nginx
```

# Nginx 簡單測

```sh
$# docker pull nginx

# 首次測試 沒啥問題...
$# docker run -d -p 8080:80 --name webserver nginx
$# docker stop webserver
$# docker rm webserver

# 底下是在 Win10 進入的...
$# run --name webserver -p 8080:80 -v e:\www\.:/usr/share/nginx/html:ro -d nginx
# URL 進去後~~~ YA!
```


# Nginx + Dockerfile

## 法1

```sh
$# docker build f0.dockerfile -t nginxserver

$# docker images
REPOSITORY                 TAG                 IMAGE ID            CREATED              SIZE
nginxserver                latest              b95dcff7947a        About a minute ago   109MB
nginx                      latest              e81eb098537d        11 days ago          109MB

$# docker run --name webserver -d -p 8080:80 nginxserver
```

## 法2
```dockerfile


```

```sh
$# docker build f1.dockerfile -t nginxserver

$# docker images
REPOSITORY                 TAG                 IMAGE ID            CREATED              SIZE
nginxserver                latest              b95dcff7947a        About a minute ago   109MB
nginx                      latest              e81eb098537d        11 days ago          109MB

# 不知道為啥... 明明寫了 EXPOSE 了... 但是上面的指令能 run, 但是 8080 進不去 orz
$# docker run --name webserver -d nginxserver

# 下面就能正常執行orz
$# docker run --name webserver -d -p 8080:80 nginxserver
# 如果要再帶入設定檔的話
# -v /some/nginx.conf:/etc/nginx/nginx.conf:ro
```

