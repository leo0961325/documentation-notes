
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
-t | 標記名稱 
-d | 背景執行 


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