
# Install MariaDB by Docker

- 2020/03/27
- [Docker-MariaDB](https://hub.docker.com/_/mariadb)


```bash
### 2020/03/27 的今天, latest 為 10.4.12
$# docker pull mariadb:10.4

MYSQL_ROOT_PASSWORD=12345678
### 測試
$# docker run --rm \
    --name mariadb \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
    mariadb:10.4


### 正式 (若無 SELinux 問題, 拿掉 :Z)
$# docker run -d \
    --name mariadb \
    --restart always \
    -p 3306:3306 \
    -v ~/docker_data/mariadb/data:/var/lib/mysql:Z \
    -v ~/docker_data/mariadb/conf.d:/etc/mysql/conf.d:Z \
    -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
    mariadb:10.4
```
