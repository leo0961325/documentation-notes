# Install postgresql by docker

- 2020/04/06
- [DockerHub-postgrs](https://hub.docker.com/_/postgres)


```bash
### 2020/04/06 latest 為 12, 但聽說不穩定?...
$# docker pull postgresql:11

$# PASSWD=1234
$# docker volume create pg_data
$# docker run -d \
    -v pg_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -e POSTGRES_PASSWORD=${PASSWD} \
    --name=mypg \
    postgres:11
```
