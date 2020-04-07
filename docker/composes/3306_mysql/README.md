# Install mysql by docker

- 2020/04/06
- [DockerHub](https://hub.docker.com/_/mysql)

```bash
### 不管啦, 就算時代變了我還是要 5.7 版
$# docker pull mysql:5.7

### 必備
$# PASSWD=123456

### 測試使用
$# docker run --rm \
    --name mysql57 \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${PASSWD} \
    mysql:5.7


### 正式使用 (目前目錄需要有 ./conf.d/)
$# docker volume create mysql57_db
$# docker run -d \
    --restart always \
    --name mysql57 \
    -v $(pwd)/conf.d/:/etc/mysql/conf.d \
    -v mysql57_db:/var/lib/mysql \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${PASSWD} \
    mysql:5.7
# 不指定密碼, 也可使用 docker logs mysql57 查看 root password
```