


# Docker - MySQL

- 2017/10/01
- [Severalnines Blog - MySQL Docker Container](https://severalnines.com/blog/mysql-docker-containers-understanding-basics)
- 前提, 已經下載並安裝好
	1. Docker
	2. MySQL

1. 下載及安裝MySQL image, 建立Container, 設定root密碼
```sh
$ docker run -d --name=<containerName> --env="MYSQL_ROOT_PASSWORD=<password>" mysql 
```

2. 看mysql啟動的Log
```sh
$ docker logs <containerName>
```

3. 取得每次啟動的docker ip
```sh
$ docker inspect <containerName> | grep IPAddress
```

4. 連進去Container囉!!
```sh
$ mysql -u <user> -p <password> -h <ip> -P <port>
```

5. 關閉MySQL Container
$ docker stop <containerName>

6. 將來再進去(Container要在, 只是還沒被啟動 docker ps -a要有)
$ docker start <containerName>



# MongoDB in docker

```sh
$ docker run --name mongo -it mongo /bin/bash

$ sudo docker images
REPOSITORY         TAG       IMAGE ID        CREATED         SIZE
docker.io/mongo    latest    88b7188af865    23 hours ago    358.3 MB
...

可以直接取得每次啟動的docker ip
$ docker inspect <containerName> | grep IPAddress

進入 docker 的 mongo
$ mongo --port <port> --host <ip>

# 啟動後,檢查mongoDB是否正在運行

$ ps auxw | grep mongod
$ systemctl status mongod 

# 加入下面兩行, 不再顯示警告訊息
$ sudo vi /etc/rc.local
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag

# 加入下面1行
$ sudo vim /etc/security/limits.d/20-nproc.conf 	
mongod   soft  nproc   64000

$ systemctl restart mongod
# 重啟後, 就不會有亂七八糟的警告訊息了
```



### 額外備註

在 `centos:7` 的 docker image內, 編譯 git 時, 因為缺乏許多套件, 發生下列錯誤
```sh
$ make 
    * new build flags
    CC credential-store.o
In file included from credential-store.c:1:0:
cache.h:42:18: fatal error: zlib.h: No such file or directory
 #include <zlib.h>
                  ^
compilation terminated.
make: *** [credential-store.o] Error 1
```

解法: [Install Git](https://tecadmin.net/install-git-2-0-on-centos-rhel-fedora/)

```sh
$ sudo yum install zlib-devel
# 之後即可正常 make
```