# 使用 Docker 安裝 MongoDB

- 2020/03/27
- [docker_mongo](https://hub.docker.com/_/mongo)
- [How to spin MongoDB server with Docker and Docker Compose](https://dev.to/sonyarianto/
how-to-spin-mongodb-server-with-docker-and-docker-compose-2lef)


底下紀錄了 2 種啟動方式

- by docker run
- by docker-compose


```bash
### 2020/03/27 的今天, latest 為 4.2.3
$# docker pull mongo:4.2

### 單純測試 起 Mongo Server
$# docker run --rm \
    -p 27017:27017 \
    --name mymongo42 \
    mongo:4.2

### 正式使用 起 MongoServer
MONGO_ROOT_USER=demo
MONGO_ROOT_PASSWD=1234
$# docker run -d \
    -p 27017:27017 \
    -v ~/docker_data/mymongo42:/data/db \
    -e MONGO_INITDB_ROOT_USERNAME=${MONGO_ROOT_USER} \
    -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_ROOT_PASSWD} \
    -e MONGO_INITDB_DATABASE=admin \
    --name mymongo42 \
    mongo:4.2


### 起 MongoClient 連入 MongoServer
# 使用前先檢查 mongo server `docker inspect mymongo42`
MongoServerNetwork=bridge
MongoServerHost=172.17.0.2
# 進入 mongo shell
$# docker run -it \
    --network  ${MongoServerNetwork} \
    --rm mongo:4.2 \
    mongo --host ${MongoServerHost} test
# 查看 Networks 使用的 driver. ex: bridge
# 查看 Networks 內的 IPAddress. ex: 172.17.0.2
# 最後面的 test 似乎可免...


### 查看 log
$# docker logs mymongo42 -f
```
