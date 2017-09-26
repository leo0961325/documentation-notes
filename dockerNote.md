
# Docker相關筆記

參考如下
- [官方網站 Docker reference](https://docs.docker.com/engine/reference/builder/)

- [Git Book - 從入門到實踐](https://philipzheng.gitbooks.io/docker_practice/content/)

--- 

## 1. Shell裡下的docker指令
| 指令 | 說明 |
| --- | --- |
| pull | 下載某個repo的image |  


## 2. Dockerfile裡寫的docker指令
| 起手式 | 說明 |
| --- | --- |
| ADD |  |  
| CMD |  |  
| COPY |  |  
| ENTRYPOINT |  |  
| ENV |  |  
| EXPOSE |  |  
| FROM |  |  
| MAINTAINER |  |  
| ONBUILD |  |  
| RUN |  |  
| USER |  |  
| VOLUME |  |  
| WORKDIR | 進入Container後的起始路徑 |

--- 

## 3. Docker Command

WORKDIR 

WORKDIR /path/to/workdir

對於RUN, CMD, ENTRYPOINT, COPY, ADD皆有效

可以設定絕對/相對路徑

ex:
WORKDIR /a

WORKDIR b

WORKDIR c

RUN pwd

則pwd的路徑為/a/b/c

簡單的說, WORKDIR就是在設定進入container後的起始路徑

---

## 4. Dockerfile

```
1. --links
可以讓本地端與Container內作安全的傳輸

建立新的container
$ sudo docker run -d --name db training/postgres

建立名為 web的 Container, 並將它 link到 db Container
$ sudo docker run -d -P --name web --link db:db training/webapp python app.py
```

---
