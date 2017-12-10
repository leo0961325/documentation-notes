
# Docker 筆記

- [2017/12/08進度](https://docs.docker.com/get-started/part3/)


```sh
$ docker --version
Docker version 17.09.0-ce, build afdb6d4
```

參考如下
- [官方網站 Docker reference](https://docs.docker.com/engine/reference/builder/)
- [Git Book - 從入門到實踐](https://philipzheng.gitbooks.io/docker_practice/content/)
- [全面易懂的Docker指令大全](https://www.gitbook.com/book/joshhu/dockercommands/details)

---
---
---

# 1. Docker Command

## 指令
語法 | 說明 
--- | --- 
pull | 下載某個repo的image 

## 結尾
語法 | 說明
--- | --- 
-a | 包含**執行中** && **非執行中**的 container
-t | 別名 
-d | 背景執行

## 範例



### 使用 Dockerfile建立 Docker image
```sh
$ docker build -t friendlyhello .
Sending build context to Docker daemon   5.12kB
Step 1/7 : FROM python:2.7-slim
...
 ---> b0259cf63993
Step 2/7 : WORKDIR /app
 ---> 1577c248b67c
Removing intermediate container bae82b05d02d
Step 3/7 : ADD . /app
 ---> 6f0232726d62
Step 4/7 : RUN pip install --trusted-host pypi.python.org -r requirements.txt
 ---> Running in 77b696cd02f3
...
 ---> 030172103052
Removing intermediate container 77b696cd02f3
Step 5/7 : EXPOSE 80
 ---> Running in 5bee88b18af6
 ---> 979ba90745c3
Removing intermediate container 5bee88b18af6
Step 6/7 : ENV NAME World
 ---> Running in 2a9d13e17d12
 ---> 37b19c8a69e3
Removing intermediate container 2a9d13e17d12
Step 7/7 : CMD python app.py
 ---> Running in 46cf3a0c3fea
 ---> 7aab4420b729
Removing intermediate container 46cf3a0c3fea
Successfully built 7aab4420b729
Successfully tagged friendlyhello:latest
```

### 查看 Docker image
```sh
$ docker image ls  
$ # or docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
friendlyhello       latest              a78e7cf70e43        28 seconds ago      148MB
hello-world         latest              f2a91732366c        2 weeks ago         1.85kB
python              2.7-slim            b0259cf63993        4 weeks ago         138MB
```

### 刪除所有

```sh
$ docker container rm $(docker container ls -a -q) # 刪除所有 container

$ docker image rm $(docker image ls -a -q) # 刪除所有 images
```

### 使用 Docker image 建立並執行 Container

```sh
$ docker run -p 4000:80 friendlyhello
* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
# 上面看到的 *Running ... 的訊息, 是來自 Container發出來的

$ docker run -d -p 4000:80 friendlyhello  # 背景執行
a0aaf046736306c0657620ba230b3660aef5b539a8398f8b56e6989f1aafd9f2

# 藉由在 Dockerfile內 EXPOSE, 以及使用 docker run -p來 publish port, 重新對應成 4000:80
```

### 查看運行中的 Container

```sh
$ docker container ls
# or docker ps
CONTAINER ID   IMAGE           COMMAND           CREATED         STATUS         PORTS                  NAMES
9d0c3e3c8c28   friendlyhello   "python app.py"   6 minutes ago   Up 6 minutes   0.0.0.0:4000->80/tcp   elated_meitner
```

### docker login
```sh
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: cool21540125
Password: 
Login success
```

### docker tag ( 必先 docker login )
> 語法: `docker tag image <使用者名稱>/<repo名字>:<tag>`

> 如果此 image打算上傳到dockerHub, 則`<使用者名稱>`必輸使用 `login的 username`
```sh
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
friendlyhello       latest              7aab4420b729        24 hours ago        148MB
python              2.7-slim            b0259cf63993        4 weeks ago         138MB

$ docker tag friendlyhello cool21540125/firstrepo:1.0 # 把其中一個 image增加 tag

$ docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED             SIZE
cool21540125/firstrepo        1.0                 7aab4420b729        24 hours ago        148MB
friendlyhello                 latest              7aab4420b729        24 hours ago        148MB
python                        2.7-slim            b0259cf63993        4 weeks ago         138MB
```

### docker push ( 建議先 docker tag )

```sh
$ docker push cool21540125/firstrepo:1.0       # 開始進入漫長的上傳...
The push refers to a repository [docker.io/cool21540125/firstrepo]
a6c3a2a51e62: Pushed
7929c66d0dcb: Pushed
582f8397321c: Pushed
c07634f99a74: Pushed
76b9dc677e20: Pushed
b7aadc98f208: Pushed
29d71372a492: Pushed
1.0: digest: sha256:657a118e922ab870421cefda27e72f459a7ce6fa476bc140d56f5c5899c8f269 size: 1787
```

### docker pull

```sh
$ docker pull cool21540125/firstrepo:1.0  # 下載 images (自己遠端 repo要先有這東西, 才能成功)

$ docker run cool21540125/firstrepo:1.0 # 下載 images && 執行 (自己遠端 repo要先有這東西, 才能成功)
```


### yml 調控 container的規模 && 組態
> A `docker-compose.yml` file is a YAML file that defines how Docker containers should behave in production.
```yml
version: "3"
services:
  web:    # 服務為 web
    # replace <username>/<repo>:<tag> with your name and image details
    image: cool21540125/firstrepo:1.0    # 從指定的 repo pull image
    deploy:
      replicas: 5     # 執行 5個 instance
      resources:
        limits:
          cpus: "0.1"   # 每個 instance最多只能使用道每個 CPU的 10%
          memory: 50M   # 每個 instance最多只能使用 50M的 RAM
      restart_policy:
        condition: on-failure   # 若其中一個 instance失敗, 該 instance立刻重啟
    ports:
      - "80:80"   # 開放 80 port(前) 映射到 container的 80 port(後)
    networks:
      - webnet    # 指示 web container透過具有 load-balanced的 network(稱為webnet), 來共同使用 80 port
networks:
  webnet:   # 使用預設的 webnet(具有 load-balanced overlay network)
```


### 執行 load-balance app (要先建好 `docker-compose.yml`)

1. 進入 swarm mode && 讓本台電腦成為 swarm manager
> 日後可以使用 `docker swarm join`來加入其他機器到 swarm as workers.
```sh
$ docker swarm init
Swarm initialized: current node (3usrv4yszs7b5uzw5mfudzhrl) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5yuvv76hzcd3ib2axrd6kl9txg5he09eqy3jvwc6akzgtwk563-e0xv5prl3vb39mfdhvrzfvoj0 192.168.1.127:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

2. 依照 yml, 建立服務
> 語法: `docker stack deploy -c <yml名稱> <app名稱>`
```sh
$ docker stack deploy -c docker-compose.yml getstartedlab
Creating network getstartedlab_webnet
Creating service getstartedlab_web
```

3. 查看 docker service啟動狀況
- 本地單一服務堆疊了 5個 container instance
- NAME 會依照第2步給的, 在加上_web
- 以下訊息為 web container吐出來的

```sh
$ docker service ls
ID             NAME                MODE         REPLICAS   IMAGE                        PORTS
ow28d93snd8m   getstartedlab_web   replicated   5/5        cool21540125/firstrepo:1.0   *:80->80/tcp
```

4. 查看 container (瞬間啟動了 5個 container)
- 每個運行在 service內的單一 container, 都稱為 **task**, 且每個 task都有專屬的 **task id** 
```sh
$ docker ps -a    
CONTAINER ID   IMAGE                        COMMAND           CREATED              STATUS              PORTS    NAMES
e7d33737b65f   cool21540125/firstrepo:1.0   "python app.py"   About a minute ago   Up About a minute   80/tcp   getstartedlab_web.5.ive1q82h833clyhl0tjmh5wlg
e0008228c4f9   cool21540125/firstrepo:1.0   "python app.py"   About a minute ago   Up About a minute   80/tcp   getstartedlab_web.2.7tu39tkc62is3iftreffht930
1e61d9e996b0   cool21540125/firstrepo:1.0   "python app.py"   About a minute ago   Up About a minute   80/tcp   getstartedlab_web.3.0hx1m0yjy5oe3d7yodakfpfpo
dc42c0ebc7af   cool21540125/firstrepo:1.0   "python app.py"   About a minute ago   Up About a minute   80/tcp   getstartedlab_web.4.o81z67upbv042yweithlph5wl
f93397cceb7b   cool21540125/firstrepo:1.0   "python app.py"   About a minute ago   Up About a minute   80/tcp   getstartedlab_web.1.tiu4mfbf9d9is46imcxzowxxm
```

5. 查看服務內的 tasks
> 語法: `docker service ps <SERVICE NAME>`
```sh
$ docker service ps getstartedlab_web
ID             NAME                  IMAGE                        NODE     DESIRED STATE   CURRENT STATE            ERROR       PORTS
tiu4mfbf9d9i   getstartedlab_web.1   cool21540125/firstrepo:1.0   tonynb   Running         Running 18 minutes ago
7tu39tkc62is   getstartedlab_web.2   cool21540125/firstrepo:1.0   tonynb   Running         Running 18 minutes ago
0hx1m0yjy5oe   getstartedlab_web.3   cool21540125/firstrepo:1.0   tonynb   Running         Running 18 minutes ago
o81z67upbv04   getstartedlab_web.4   cool21540125/firstrepo:1.0   tonynb   Running         Running 18 minutes ago
ive1q82h833c   getstartedlab_web.5   cool21540125/firstrepo:1.0   tonynb   Running         Running 18 minutes ago

$ docker container ls -q
e7d33737b65f
e0008228c4f9
1e61d9e996b0
dc42c0ebc7af
f93397cceb7b
```

6. 查看 load-balance的威力~~~, 每次進入的 container都不同!!
- 如果反應時間太久(可能達數十秒), 並不表示 container效能問題, 而是未能滿足 REDIS的依賴關係(後面會談到)
- 底下出現的 `counter disabled`, 是因為服務內, 還沒有儲存數據的機制
- Linux terminal, 要用 `curl -4`, 原理不懂... 單純 `curl` 抓不到orz
```sh
$ curl -4 http://localhost
<h3>Hello World!</h3><b>Hostname:</b> e7d33737b65f<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
$ curl -4 http://localhost
<h3>Hello World!</h3><b>Hostname:</b> 1e61d9e996b0<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
$ curl -4 http://localhost
<h3>Hello World!</h3><b>Hostname:</b> f93397cceb7b<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
$ curl -4 http://localhost
<h3>Hello World!</h3><b>Hostname:</b> dc42c0ebc7af<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
$ curl -4 http://localhost
<h3>Hello World!</h3><b>Hostname:</b> e0008228c4f9<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
```

7. 調整 scale
- 去修改前面建立的 `docker-compose.yml`
- 重新執行 `docker stack deploy -c docker-compose.yml getstartedlab` 即可, 不需要手動刪除或重起任何 container
- 可以在運行期間, 修改 `docker-compose.yml`, 並且重新執行 `docker stack deploy`的指令, 變可在生產途中作 scale outdock.


8. 關閉服務  && 關閉 swarm
> 關閉 app語法: `docker stack rm <app名稱>`
```sh
$ docker stack rm getstartedlab
Removing service getstartedlab_web
Removing network getstartedlab_webnet
```
> 關閉 swarm
```sh
$ docker swarm leave --force
Node left the swarm.
```















---
---
---


# 2. Dockerfile
 起手式 | 範例 | 說明 |
 --- | --- | --- |
 ADD | ADD . /app | 把本地目前資料夾底下的東西, 複製到指定 container的 /app內 |  
 CMD | CMD ["python", "app.py"] | container啟動後, 執行 app.py  
 COPY |  |  
 ENTRYPOINT |  |  
 ENV | ENV NAME World <br />ENV https_proxy host:port | 設定環境變數 NAME 為 World <br /> 可以設定 Proxy Server  
 EXPOSE | EXPOSE 80 | 開放 80 port  
 FROM |  |  
 MAINTAINER |  |  
 ONBUILD |  |  
 RUN |  | 執行腳本
 USER |  |  
 VOLUME |  |  
 WORKDIR | 進入Container後的起始路徑<br /> 對於`RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD`皆有效 <br /> 可以設定絕對/相對路徑 |





--- 
---
---


# 3. Dockerfile Examples

### [Officical Example](https://docs.docker.com/get-started/part2/#dockerfile)
- 2017/12/07
```dockerfile
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

---
---
---

# 4. 備註

> 如果在 `run`和`build` images的時候, 沒有明確指名 `tag`, 則會視為`latest`

```
1. --links
可以讓本地端與Container內作安全的傳輸

建立新的container
$ sudo docker run -d --name db training/postgres

建立名為 web的 Container, 並將它 link到 db Container
$ sudo docker run -d -P --name web --link db:db training/webapp python app.py
```

### 在 Windows中, Ctrl+c無法停止運行中的 Container, 必須用此指令 (Linux也可用)
```cmd
> docker container stop <Container NAME or ID>
```


---
---
---


# 5. 知識

## 定義Docker容器如何在生產中運行的文件: yml
docker-compose.yml 範例
```yml
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:
```



## 名詞
> Docker Trusted Registry, 此為 Docker私有雲服務, 簡稱 DTR.

> yml: 用來表達資料序列的格式

> swarm: A swarm is a group of machines that are running Docker and joined into a cluster. 每台加入 swarm的機器, 都稱為 nodes.

> hypervisor: 虛擬機器監控裝置