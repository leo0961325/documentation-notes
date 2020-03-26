# [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)

- 2019/07/22

對於 docker-compose 來說, 需要在一個空的資料夾, 新增(以 Python-Django 為例):

- Dockerfile
- Python dependencies file
- docker-compose.yml

```bash
### 資料夾架構
/compose-dir            # App image 的 context (應該只包含 Resources to build the image)
    /Dockerfile                 # 定義了 app image content
    /python dependencies files  #
    /docker-compose.yml         #
```


# 開始吧~

```dockerfile
### Dockerfile
FROM    python:3
ENV     PYTHONBUFFERED 1
RUN     mkdir /code
WORKDIR /code
COPY    . /code
RUN     pip install -r requirements.txt
```

```bash
### requirements.txt
Django>=2.0,<3.0
psycopg2>2.7,<3.0
```

```yml
### docker-compose.yml
version: '3'
services:
    db:
        image: postgres
    web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
            - .:/code
        ports:
            - "8000:8000"
        depends_on:
            - db
```

```bash
### 在 Terminal 上執行~
$ docker-compose run web django-admin startproject proj .

### 就會在本地端, 建立 django 專案 && manage.py
$ ll
total 20
-rw-rw-r--. 1 tony tony 255 Jul 18 14:20 docker-compose.yml
-rw-rw-r--. 1 tony tony 132 Jul 18 14:19 Dockerfile
-rwxr-xr-x. 1 root root 624 Jul 18 14:21 manage.py
drwxr-xr-x. 2 root root  74 Jul 18 14:21 proj
-rw-rw-r--. 1 tony tony  35 Jul 18 14:20 requirements.txt

### 改變 owner
$ chown -R $USER:$USER

### 改變 DB conn
$ vim proj/settings.py
# ↓↓↓↓↓ 如下 ↓↓↓↓↓
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
# ↑↑↑↑↑ 如上 ↑↑↑↑↑
# 如果要改預設密碼的話, 參考這邊吧 https://hub.docker.com/_/postgres

### 看狀況
$  docker-compose ps
    Name                  Command              State    Ports
---------------------------------------------------------------
compose_db_1   docker-entrypoint.sh postgres   Up      5432/tcp

### 重來~
$ docker-compose up

### 最後, 因為是使用 Default Docker Bridge
$ vim proj/settings.py
# ↓↓↓↓↓ 如下 ↓↓↓↓↓
ALLOWED_HOSTS = ['*']   # 可改成 Docker host IP 或 *(較不安全)
# ↑↑↑↑↑ 如上 ↑↑↑↑↑

### 如此一來, 就可以存取了~~~
$ $ docker ps
CONTAINER ID  IMAGE        COMMAND                 CREATED        STATUS        PORTS                   NAMES
066df8400607  compose_web  "python manage.py ru…"  5 minutes ago  Up 5 minutes  0.0.0.0:8000->8000/tcp  compose_web_1
69e88dfa6f5b  postgres     "docker-entrypoint.s…"  8 minutes ago  Up 8 minutes  5432/tcp                compose_db_1

### 關閉方式
# 法 1 (直接 Ctrl + C)

# 法 2 (另一個 Terminal, 進入相同 dir)
$ docker-compose down
```

```bash
### 可看目前 compose 底下有哪些 container
$# docker-compose ps
       Name                      Command               State           Ports
-------------------------------------------------------------------------------------
composetest_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
composetest_web_1     flask run                        Up      0.0.0.0:5000->5000/tcp

### 連同 volumes, 整個移除 compose
$# docker-compose down --volumes

### 查看 compose 內的服務的 環境變數
$# docker-compose run <ServiceName> env
```