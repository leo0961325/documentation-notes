# Install nginx by compose

- 2020/04/01
- [DockerHub Nginx](https://hub.docker.com/_/nginx)

```bash
### 2020/04/01 的今天, latest 為 1.17, 而最新的 stable 為 1.16
docker pull nginx:1.17

### 測試
$# docker run --rm \
    --name mynginx \
    nginx:1.17


$# mkdir ./conf.d
$# docker run -d \
    --restart always \
    -v ./conf.d:/etc/nginx/conf.d \
    nginx:1.17

$#
```