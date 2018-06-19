# [Docker commit](https://docs.docker.com/engine/reference/commandline/commit/#examples)
- 2018/06/17

> 語法: `docker commit <Container ID> <REPOSITORY[:TAG]>` 

Name, shorthand | 	Default	 | Description
-------- | ----- | ------
--author , -a	|	| Author (e.g., “John Hannibal Smith hannibal@a-team.com”)
--change , -c	|	| Apply Dockerfile instruction to the created image
--message , -m	|	| Commit message
--pause , -p	|true	|Pause container during commit
```sh
# 要先登入~
$ docker login

$ docker images
REPOSITORY           TAG    IMAGE ID        CREATED          SIZE
centos               7      49f7960eb7e4    (pass)           200MB

$ docker ps
CONTAINER ID   IMAGE      COMMAND      CREATED     STATUS    PORTS    NAMES
7b82237ee719   centos:7   "/bin/bash"  (pass)      (pass)

# 有點開始燒錄光碟的感覺... 會花點時間
$ docker commit -a "tonycj" -m "for dev light container" 7b82237ee719 cool21540125/devos7:1.0
sha256:6c24ad6bdb412fe1a65831502c2f6b39c746445a03ad19c70f97161bc45e37af
# -a : 作者
# -m : Commit message
# 指定 image name

$ docker images
REPOSITORY           TAG    IMAGE ID        CREATED          SIZE
centos               7      49f7960eb7e4    (pass)           200MB
cool21540125/devos7  1.0    6c24ad6bdb41    26 seconds ago   961MB

$ docker login

$ docker push cool21540125/devos7:1.0
# 開始漫長的上傳~~
```

完成後前往 Docker Hub, 東西救上去了

```sh
# 執行~
$ docker run -it --name tonyos7 cool21540125/devos7:1.0 /bin/bash
```