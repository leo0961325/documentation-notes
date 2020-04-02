# Drone 搭配 Gitea

- [Drone.io-ByGitea](https://docs.drone.io/server/provider/gitea/)
- 2020/04/02


## 法一 dockerfile
```bash
$# docker pull drone/drone:1

$# docker volume create drone-data

$# docker run -d \
  --restart=always \
  --volume=drone-data:/data \
  --env=DRONE_GITEA_SERVER={{DRONE_GITEA_SERVER}} \
  --env=DRONE_GITEA_CLIENT_ID={{DRONE_GITEA_CLIENT_ID}} \
  --env=DRONE_GITEA_CLIENT_SECRET={{DRONE_GITEA_CLIENT_SECRET}} \
  --env=DRONE_RPC_SECRET={{DRONE_RPC_SECRET}} \
  --env=DRONE_SERVER_HOST={{DRONE_SERVER_HOST}} \
  --env=DRONE_SERVER_PROTO={{DRONE_SERVER_PROTO}} \
  --publish=3001:80 \
  --publish=3443:443 \
  --name=mydrone \
  drone/drone:1
```

## 法二 docker-compose
```bash

```