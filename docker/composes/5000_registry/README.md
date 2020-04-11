# Install docker-registry by docker

- 2020/04/10
- [DockerHub-registry](https://hub.docker.com/_/registry)

```bash
### 2020/04/10, 最新版為 2.7.1
$# docker pull registry

### 一開始先這麼做
$# docker volume create docker_registry
$# docker run -d \
    --restart always \
    --name myregistry \
    -p 5000:5000 \
    registry:2

### 然後開始做 SSL...


### 完成 SSL 後, 重來~
$# docker stop myregistry
$# docker run -d \
    --restart always \
    -e STORAGE_PATH=/registry \
    -e SEARCH_BACKEND=sqlalchemy \
    -e REGISTRY_HTTP_ADDR=0.0.0.0:443 \
    -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
    -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
    --name myregistry \
    -v docker_registry:/var/lib/registry \
    -v $(pwd)/certs/domain.crt:/certs \
    -p 5000:5000 \
    -p 443:443 \
    registry:2
```