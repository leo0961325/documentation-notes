
# PostgreSQL

- 2019/05/16

```bash
### Run Container
$# docker run -d -p 54321:5432 -v /var/data/container/postgres:/var/data/postgres -v /var/data/container/xlog_archive:/var/data/xlog_archive -v /var/data/container/backup:/var/data/backup -e POSTGRES_PASSWORD=postgres --name=app-postgres postgres

### ps
$# docker ps
CONTAINER ID  IMAGE     COMMAND                 CREATED        STATUS        PORTS                    NAMES
66f01f9cc264  postgres  "docker-entrypoint.s…"  4 seconds ago  Up 2 seconds  0.0.0.0:54321->5432/tcp  app-postgres

### Usage
$# psql -h <HOST> -p <PORT> -U postgres -W <PASSWORD> <DATABASE>
# 或者, 使用 GUI 登入, 帳號預設為 postgres

### 進入 Shell
$# docker exec -it app-postgres /bin/bash
```


# RabbitMQ

- 2019/05/03
- [Docker 安裝部署 RabbitMQ](https://www.jianshu.com/p/14ffe0f3db94)

```bash
$ docker search rabbitmq:management

$ docker pull rabbitmq:management

$ docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:management
# 管理介面 localhost:15672
# ???? localhost:5672
```

