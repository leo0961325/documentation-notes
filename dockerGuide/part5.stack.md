# Part3 - Services
- [Services](https://docs.docker.com/get-started/part3/)
- 2017/12/16

##### 1. [Orientation ](./part1.orientation.md)
##### 2. [Containers](./part2.containers.md)
## 3. [Services](./part3.services.md)
##### 4. [Swarms](./part4.swarm.md)
##### 5. [Stacks](./part5.stacks.md) 
##### 6. [Deploy your app](./part6.deploy.md)

---

本章, 要開始談 Service這鬼東西, 另外會舉例用 docker實作 load-balance

為了作到 load-balance, 我們得把自己看系統架構的層級提高~~
- Stack
- Services (我們在這了~~)
- Container (in part 2)


---

開始之前, 由於我是 Linux, 所以需要額外安裝 Compose

(( 安裝完後想刪除 Compose, 自己到官網看說明囉~ [Install Docker Compose](https://docs.docker.com/compose/install/#uninstallation) ))

```sh
# 1. 下載 Compose
$ sudo curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

# 2. 允許目前使用者執行
$ sudo chmod +x /usr/local/bin/docker-compose

# 3. 安裝 Bash completion (可不安裝)
# 我就懶得安裝了...

# 4. 看看版本~
$ docker-compose --version
docker-compose version 1.17.0, build ac53b73
```


