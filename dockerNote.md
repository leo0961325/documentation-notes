
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
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                  NAMES
9d0c3e3c8c28        friendlyhello       "python app.py"     6 minutes ago       Up 6 minutes        0.0.0.0:4000->80/tcp   elated_meitner
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

### docker push ( 必先 docker tag )

```sh
$ docker push cool21540125/firstrepo:1.0       # 開始進入漫長的上傳...
The push refers to a repository [docker.io/cool21540125/firstrepo]
a6c3a2a51e62: Pushing [=====>                                             ]  1.094MB/9.946MB
7929c66d0dcb: Pushing [==================================================>]  5.632kB
582f8397321c: Pushing  1.536kB
c07634f99a74: Pushing [====>                                              ]  626.7kB/6.5MB
76b9dc677e20: Pushing [=>                                                 ]  967.7kB/45.88MB
b7aadc98f208: Waiting
29d71372a492: Waiting
```

### docker pull

```sh

```




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

## 名詞
> Docker Trusted Registry, 此為 Docker私有雲服務, 簡稱 DTR.
