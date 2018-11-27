# mysql

```sh
docker search mysql
```

```sh
# 
docker run --name my -p 3307:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:5.7
# 3307 進入
# 密碼: password
# image : mysql:5.7
# container : my
```

```sh
# 看設定檔
docker exec my cat /etc/mysql/my.cnf
docker exec my ls /etc/mysql/conf.d
```

```sh
# 把之前的先清除
docker stop my
docker rm my

# Windows 10 寫法
docker run --name my -p 3307:3306 -v E:\www\data\my.cnf:/etc/mysql/my.cnf -e MYSQL_ROOT_PASSWORD=password -d mysql:5.7

# Linux 寫法
docker run --name my -p 3307:3306 -v           ./my.cnf:/etc/mysql/my.cnf -e MYSQL_ROOT_PASSWORD=password -d mysql:5.7

# 對映 port : 3307 進入
# volume : /data
```

```sh
# 上式成功後, 就可以進入 mysql 了~~
$# mysql -uroot -p -P 3307
# 密碼 password

mysql> 
```