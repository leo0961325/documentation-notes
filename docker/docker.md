
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

```sh
$ docker run -d --name nginx nginx

# 查看 Container內的 IP Address
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' nginx
172.17.0.2

# 用 Image: busybox 建立 Container: foo, 指定他的 host為 foobar, 並執行 "sleep 300"的指令
$ docker run -d --name foo -h foobar busybox sleep 300

# 查看 運行中的 Container: foo, 並查看他的 foobar這個 host的 相關資訊
$ docker exec -it foo cat /etc/hosts | grep foobar
172.17.0.2	foobar

# 依照本地的 dockerfile建立名為 flask 的 image
$ docker build -t flask .

# 查看 foobar Container的 5000 port資訊
$ docker port foobar 5000
0.0.0.0:32768

# 建立並執行 Container: nginx, 並且查看本機端的 iptables
$ docker run -d -p 5000/tcp -p 53/udp --name nginx nginx
$ sudo iptables -L
...(一堆)...
Chain DOCKER (2 references)
target    prot opt source      destination    
ACCEPT    tcp  --  anywhere    172.17.0.2     tcp dpt:commplex-main
ACCEPT    udp  --  anywhere    172.17.0.2     udp dpt:domain
...(一堆)...
```


> `docker run -d --name <Container Name> -h <Host Name> <Image Name> <其他指令>` 使用 Image建立 Container, 並指定 hostname, 然後執行相關指令







- 每個運行在 service內的單一 container, 都稱為 **task**, 且每個 task都有專屬的 **task id** 

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
- [官方教學](https://docs.docker.com/engine/reference/builder/#usage)

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


> `docker run 的參數` 可覆寫 DOCKERFILE的 `CMD`

> `docker run --entrypoint XXX` 可覆寫DOCKERFILE的 `ENTRYPOINT`



--- 
---
---


# 3. Dockerfile Examples

#### 範例 - Flask起 Server
- [官方範例](https://docs.docker.com/get-started/part2/#dockerfile)
- 2017/12/07

> 先建立 3個檔案, 再建立 Image

1. dockerfile
```dockerfile
FROM python:2.7-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "app.py"]
```

2. requirement.txt
```
Flask
Redis
```

3. app.py
```py
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

4. run
```sh
$ ls
app.py  requirements.txt  dockerfile

$ docker build .

$ docker images
REPOSITORY    TAG         IMAGE ID        CREATED           SIZE
<none>        <none>      c8d0def6863d    28 seconds ago    148MB
python        2.7-slim    4fd30fc83117    7 weeks ago       138MB
# 因為並沒有指定建立的 Image的名稱..., 所以只有 Image ID

$ docker run -p 4000:80 c8d0
```


#### 範例 - ENTRYPOINT
- 2018/01/30 

1. dockerfile
```dockerfile
FROM ubuntu:14.04
ENTRYPOINT ["/bin/echo"]

# 或者
# FROM ubuntu:14.04
# CMD ["/bin/echo" , "Hi Docker !"]
```
2. run
```sh
$ docker build .

$ docker images
REPOSITORY     TAG       IMAGE ID        CREATED          SIZE
<none>         <none>    ac41d98ae2f5    3 minutes ago    222MB
ubuntu         14.04     dc4491992653    4 days ago       222MB

$ docker run ac41 HIII~~
HIII~~

$ docker ps -a
CONTAINER ID    IMAGE    COMMAND               CREATED    STATUS    PORTS    NAMES
d13e1f5a3f72    ac41     "/bin/echo HIII~~"    ...        ...                stoic_johnson
# 每次 RUN Image, 都會啟動新的 Container, 然後再關掉
```

#### 範例 - CMD
- 2018/01/30 

1. dockerfile
```dockerfile
FROM ubuntu:14.04
CMD ["/bin/echo" , "Hi Docker !"]
```

2. run
```sh
$  docker build .

$ docker images
REPOSITORY    TAG       IMAGE ID        CREATED           SIZE
<none>        <none>    2d0610d94311    17 seconds ago    222MB
ubuntu        14.04     dc4491992653    4 days ago        222MB

$ docker run 2d06 /bin/date
Tue Jan 30 07:06:40 UTC 2018

$ docker container ls -a
CONTAINER ID    IMAGE    COMMAND        CREATED          STATUS    PORTS    NAMES
00f8e0ace3e5    2d06     "/bin/date"    7 seconds ago    ...                distracted_brattain
```


#### 範例 - 
- 2018/01/30

1. dockerfile
```dockerfile
FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get clean all
RUN pip install flask

ADD hello.py /tmp/hello.py
EXPOSE 6000
cmd ["python", "/tmp/hello.py"]
```

2. hello.py
```py
from flask import Flask
app = Flask(__name__)
@app.route('/hi')
def hello_world():
  return 'Hello World!'
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6000)
```

3. run
```sh
$ ls
dockerfile  hello.py

$ docker build -t flask .
# 使用本地 dockerfile 建立 tag為 flask的 docker image

$ docker images
REPOSITORY     TAG         IMAGE ID        CREATED           SIZE
flask          latest      ac9445327790    39 seconds ago    397MB
flask_image    latest      76ab99223787    24 hours ago      707MB
python         2.7-slim    4fd30fc83117    7 weeks ago       138MB

$ docker run -d -P flask
27829ed44e8a82e465380368d6241356669ced08d9563e11a3195af84c482818

$ docker ps
CONTAINER ID    IMAGE    COMMAND                  CREATED    STATUS    PORTS                     NAMES
27829ed44e8a    flask    "python /tmp/hello.py"   ...        ...       0.0.0.0:32768->6000/tcp   epic_ptolemy
# 可透過 localhost:32768/hi 訪問 flask
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