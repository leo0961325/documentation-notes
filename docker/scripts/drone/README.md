# Install Drone-Server by Docker

- 2020/03/27
- [drone](http://plugins.drone.io/drone-plugins/drone-docker/)
- [dockerhub-drone/drone](https://hub.docker.com/r/drone/drone)
- [Drone環境變數](https://docs.drone.io/server/reference/)
- [Install DroneServer for Gitea](https://docs.drone.io/server/provider/gitea/)

### 使用方式分為

- docker run ...
- docker-compose up -d


```bash
### 2020/03/27 的今天,
$# docker pull drone/drone:1


### 測試-使用 dockerfile (使用 sqlite)
$# docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITEA_SERVER={{DRONE_GITEA_SERVER}} \
  --env=DRONE_GITEA_CLIENT_ID={{DRONE_GITEA_CLIENT_ID}} \
  --env=DRONE_GITEA_CLIENT_SECRET={{DRONE_GITEA_CLIENT_SECRET}} \
  --env=DRONE_RPC_SECRET={{DRONE_RPC_SECRET}} \
  --env=DRONE_SERVER_HOST={{DRONE_SERVER_HOST}} \
  --env=DRONE_SERVER_PROTO={{DRONE_SERVER_PROTO}} \
  --publish=3001:80 \
  --publish=3443:443 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:1




### 實際使用

```
