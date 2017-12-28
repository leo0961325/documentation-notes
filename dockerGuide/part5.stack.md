# [Part5 - Stack](https://docs.docker.com/get-started/part5/)
- 2017/12/20

##### 1. [Orientation ](./part1.orientation.md)
##### 2. [Containers](./part2.containers.md)
##### 3. [Services](./part3.services.md)
##### 4. [Swarms](./part4.swarm.md)
## 5. [Stacks](./part5.stacks.md) 
##### 6. [Deploy your app](./part6.deploy.md)

---

### Prerequest:
- 安裝好 Docker
- 安裝好 Docker Compose
- 安裝好 Docker Machine
- 讀完 part1 ~ part4
- 如 part2, 已經建立好 Docker image - friendlyhello, 且以上傳到 Registry
- 如 part4, 正在運行一個 Container `docker run -p 80:80 cool21540125/firstrepo:1.0`
- 如 part4, 稍早建立好的東西正在運行 `docker-machine ls`, 如果已經關掉了, 啟動: `docker-machine start myvm1` && `docker-machine start myvm2`
- 如 part3, 已經建立好 docker-compose.yml
- 如 part4, 已經建立好 Swarm, 且正在運行中, 執行: `docker-machine ssh myvm1 "docker node ls"`

---
### Introduction
從 part4已經知道, swarm這東西就是 一堆執行中的 Container綁成一包來執行一個應用程式.

此章節要講的是 Stack層級, Stack是一堆相互依賴並且共存的服務的集合. 此 Stack可以很彈性的作擴展及收縮.

單一 Stack其實也可以作整個應用程式的功能

如同 part3所提過, 建立好 compile.yml檔後, 執行 `docker stack deploy`, 這個結果是在本地端執行單一 Stack.

本章節將學會, 如何在多台機器上, 運行多個服務.

```yml
version: "3"
services:
  web:
    image: cool21540125/firstrepo:1.0
    deploy:
      replicas: 5
      restart_policy:
        condition: on-failure
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
    ports:
      - "80:80"
    networks:
      - webnet
  visualizer:
    image: dockersamples/visualizer:stable
    ports:
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - webnet
networks:
  webnet:
```