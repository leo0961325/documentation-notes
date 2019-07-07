# kafka

- 2019/07/06
- [Docker - bitnami/kafka](https://hub.docker.com/r/bitnami/kafka/)
- [Docker - zookeeper](https://hub.docker.com/_/zookeeper)
- kafka 依賴 zookeeper... 所以不得不提到它


## networking

```bash
### kafka 依賴 zookeeper, 先建立專屬的 network吧...
$# docker network create -d bridge zkp_kafka
```

## zookeeper

```bash
### Linux
$# docker run -d \
    --name zkp \
    --net zkp_kafka \
    -e ZOO_LOG4J_PROP="INFO,ROLLINGFILE" \
    -v $(pwd)/zoo.cfg:/conf/zoo.cfg \
    -v $(pwd)/zoo.log:/logs/zookeeper.log \
    zookeeper:latest

### Win10 (git-bash)
$# docker run -d \
    --name zkp \
    --net zkp_kafka \
    -e ZOO_LOG4J_PROP="INFO,ROLLINGFILE" \
    -v D:\Docker\zookeeper\logs\zoo.log:/logs\zookeeper.log \
    -v D:\Docker\zookeeper\conf\zoo.cfg:/conf\zoo.cfg \
    zookeeper:latest
# 預設 EXPOSE 2181 2888 3888 8080


### 進入 zookeeper (比較特別一點...)
$# docker exec -it zkp zkCli.sh -server zkp
Connecting to zkp
Welcome to ZooKeeper!
JLine support is enabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
[zk: zkp(CONNECTED) 0]          # <--- 命令提示
# zookeeper command line 比較特殊, 分為 C 與 java
#   - java client 需使用 「zkCli.sh -server IP:port」
```

## kafka

```bash
### Start - kafka
$# docker run -d \
    --name kafka \
    --net zkp_kafka \
    -e ALLOW_PLAINTEXT_LISTENER=yes \
    -p 9092:9092 \
    bitnami/kafka:latest

### Kafka - Server
# $# docker run -d \
#     --name kafka \
#     --net zkp_kafka
#     -e ALLOW_PLAINTEXT_LISTENER=yes \
#     -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
#     bitnami/kafka:latest

### Kafka - Client
# $# docker run -it --rm \
#     -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
#     bitnami/kafka:latest kafka-topics.sh --list  --zookeeper zookeeper-server:2181

```


## - compose

```bash
### https://hub.docker.com/r/bitnami/kafka/
$ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-kafka/master/docker-compose.yml > docker-compose.yml
$ docker-compose up -d
```

```yml
# 若想在 compose 保存資料:
kafka:
  volumes:
    - /path/to/kafka-persistence:/bitnami/kafka
```
