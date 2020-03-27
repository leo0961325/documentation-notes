



```bash
###
$# docker pull mariadb:10.4

MYSQL_ROOT_PASSWORD=qwer@1234
### 測試
$# docker run --rm \
    --name mariadb \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
    mariadb:10.4


### 正式
$# docker run -d \
    --name mariadb \
    --restart always \
    -p 3306:3306 \
    -v /var/docker_data/mariadb/data:/var/lib/mysql \
    -v /var/docker_data/mariadb/conf.d:/etc/mysql/conf.d \
    -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
 mariadb:10.4
```
