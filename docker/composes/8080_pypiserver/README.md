
# 搭建 pypi-server by compose

- 2020/04/05
- [DockerHub-pypiserver](https://hub.docker.com/r/pypiserver/pypiserver)
- [pypiserver](https://pypiserver.readthedocs.io/en/latest/README.html)

## 架設 PyPI-Server

```bash
### 2020/04/05, stable 的最大版號為 1.3.2
$# docker pull pypiserver/pypiserver:latest

$# ls
data    docker-compose.yml

### 新增帳號密碼
$# touch data/pypi.htpasswd
$# htpasswd -Bb data/pypi.htpasswd user01 password01  # 建立 user && password
# -B, 較為安全的加密方式
# -b, 後面接著給 <file> <user> <password>

$# pypi-server -o -p 28888 -P ./.htaccess /var/private_pypi/packages
```

```bash
$# docker-compose up -d

# OR
$# $# docker run -d \
    --restart always \
    -v $(pwd)/data/:/data/ \
    -v pypiserver:/data/packages \
    -p 28888:8080 \
    --name mypypi \
    pypiserver/pypiserver:latest \
    -P htpasswd packages
```



```

### Step2
$# vim /etc/nginx/conf.d/pypi.conf
# -------------------------------------------
server {
    server_name pypi.tonychoucc.com;
    location / {
        proxy_pass http://localhost:28888;
    }
    return 404;
}
# -------------------------------------------
$# nginx -t
$# nginx -s reload

### Step3
$# vim ~/.pypirc
# -------------------------------------------
[mypypi]
repository:http://127.0.0.1:28888
username:user1
password:password1
# -------------------------------------------

```


## Client 上傳 && 下載 設定

```bash
### 設定這個以後, 將來下載(pip install XXX)的時候也會到這邊找
$# echo 'export PIP_EXTRA_INDEX_URL=http://localhost:28888/simple/' >> ~/.bash_profile

### 設定這個之後, 便可將檔案上傳上去
$# vim ~/.pypirc
[mypypi]
repository:http://127.0.0.1:28888
username:pypi001
password:123

### 上傳
$# twine upload -r mypypi dist/*
Uploading distributions to http://127.0.0.1:28888
Uploading example_pkg-0.1.0-py3-none-any.whl
100%|█████████████████████████████████| 7.63k/7.63k [00:07<00:00, 1.05kB/s]

### 下載
$# pip install example-pkg-tonychoucc
Looking in indexes: https://pypi.org/simple, http://localhost:28888/simple/
Collecting example-pkg-tonychoucc
  Downloading http://localhost:28888/packages/example_pkg-0.1.0-py3-none-any.whl
Installing collected packages: example-pkg-tonychoucc
Successfully installed example-pkg-tonychoucc-0.0.3
```
