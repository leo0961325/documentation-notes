# 使用 Docker 安裝 MongoDB

- 2020/03/27
- [docker_mongo](https://hub.docker.com/_/mongo)


```bash
### 2020/03/27 的今天, latest 為 4.2.3
$# docker pull mongo:4.2

### 單純測試 起 Mongo Server
$# docker run --rm \
    -p 27017:27017 \
    --name mymongo \
    mongo:4.2

### 正式使用 起 MongoServer
$# docker run -d \
    -p 27017:27017 \
    -v ~/docker_data/mymongo:/db/data \
    --name mymongo \
    mongo:4.2

### 起 MongoClient 使用 MongoCli 的方式, 連入 MongoServer
# 使用前先檢查 mongo server `docker inspect mymongo`
$# docker run -it \
    --network <MongoServerNetwork> \
    --rm mongo:4.2 \
    mongo --host <MongoServerHost> test
# 查看 Networks 使用的 driver. ex: bridge
# 查看 Networks 內的 IPAddress. ex: 172.17.0.2

### 查看 log
$# docker logs mymongo -f
```
