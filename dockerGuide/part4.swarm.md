# Part4 - Swarms
- [Swarms](https://docs.docker.com/get-started/part4/)
- 2017/12/16

##### 1. Orientation 
##### 2. Containers 
##### 3. Services
## 4. Swarms 
##### 5. Stacks 
##### 6. Deploy your app

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

---

要開始模擬 docker cluster, 模擬方式採用 VM

建立 docker Virtual-Machine
```sh
# 建立 docker-machine
$ docker-machine create --driver virtualbox myvm1       # 建立第1台 VM
Running pre-create checks...
Creating machine...
(myvm1) Copying /home/tonynb/.docker/machine/cache/boot2docker.iso to /home/tonynb/.docker/machine/machines/myvm1/boot2docker.iso...
(myvm1) Creating VirtualBox VM...
(myvm1) Creating SSH key...
(myvm1) Starting the VM...
(myvm1) Check network to re-create if needed...
(myvm1) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
.Detecting the provisioner...
Provisioning with boot2docker...
1Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: docker-machine env myvm1

$ docker-machine create --driver virtualbox myvm2       # 建立第2台 VM
# 提示訊息同上, 此略

$ docker-machine ls
NAME    ACTIVE   DRIVER       STATE     URL                        SWARM   DOCKER        ERRORS
myvm1   -        virtualbox   Running   tcp://192.168.99.100:2376          v17.09.1-ce
myvm2   -        virtualbox   Running   tcp://192.168.99.101:2376          v17.09.1-ce
```

> 指定 docker VM啟動 swarm, 並成為 **swarm manager** <br />
  語法: `docker-machine ssh <VM Name> "docker swarm init --advertise-addr <docker VM的 ip>"`

> 指定 docker VM裡的 **swarm manager**, 增加 **swarm worker** <br />
  語法: `docker-machine ssh myvm2 "docker swarm join --token <啟動 swarm init的 token> <docker VM的 IP>:2377"`
```sh
# 啟動 Swarm (這台 docker VM會自動成為 Swarm Manager)
$ docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100"
Swarm initialized: current node (osegh4bhtk25wbzugieg9qck9) is now a manager.
To add a worker to this swarm, run the following command:
    docker swarm join --token SWMTKN-1-3x34nxl3s7ljrq8z30ppgfdf5kzjowuq5u696gsqlb9ya3bce0-3ef8c24650bc863byqj8irwxh 192.168.99.100:2377
To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

# 增加 Swarm Worker
$ docker-machine ssh myvm2 "docker swarm join \
--token SWMTKN-1-3x34nxl3s7ljrq8z30ppgfdf5kzjowuq5u696gsqlb9ya3bce0-3ef8c24650bc863byqj8irwxh \
192.168.99.100:2377"
This node joined a swarm as a worker.
```
> 官方建議: 使用 `docker swarm init`及 `docker swarm join`時, 永遠使用預設 port **2377**<br />
  2377 port為 swarm manager port

> 若使用 `docker-machine ls`, VM IP會回傳 **2376 port**, 此為 Docker daemon port. 勿用此 IP, 以免發生錯誤.

> 備註: 若 ssh發生問題, 使用 `docker-machine --native-ssh ssh myvm1 ...`, 詳情參考官方說明



```sh
# 查看 myvm1這台 Swarm Manager為首的 Swarm Nodes
$ docker-machine ssh myvm1 "docker node ls"
ID                            HOSTNAME    STATUS      AVAILABILITY    MANAGER STATUS
osegh4bhtk25wbzugieg9qck9 *   myvm1       Ready       Active          Leader
d0z2empg8l9mgwp4tj9zea3ba     myvm2       Ready       Active
```

## 在 Swarm Cluster部署 app


前面部份, 如果要與 swarm溝通, 都必須使用

`docker-machine ssh <VM Name>` `"<寫死的指令字串>"`

有點不方便, 而我們可以利用另一種方法來對 swarm下指令!!
> 語法: `docker-machine env <VM Name>`, 取得 < VM Name> 的組態命令

```sh
# 取得 myvm1的組態指令
$ docker-machine env myvm1
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/home/tonynb/.docker/machine/machines/myvm1"
export DOCKER_MACHINE_NAME="myvm1"
# Run this command to configure your shell:
# eval $(docker-machine env myvm1)

# 下這行指令完後, 以後下的 Bash Script都是針對此 docker VM
$ eval $(docker-machine env myvm1)

$ docker-machine ls
NAME    ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
myvm1   *        virtualbox   Running   tcp://192.168.99.100:2376           v17.09.1-ce
myvm2   -        virtualbox   Running   tcp://192.168.99.101:2376           v17.09.1-ce
# *為下此指令的機器
```

[2017/12/17進度到這](https://docs.docker.com/get-started/part4/#deploy-the-app-on-the-swarm-manager)





---

指令備註

```sh
$ docker-machine create --driver virtualbox <Machine Name>      # 建立 docker VM

$ docker-machine ls                                             # 列出所有 docker VM及其相關資訊

$ docker-machine rm <VM Name>                                   # 移除 docker VM

$ docker-machine ssh <VM Name> "docker node ls"                 # 查看<VM Name>這台Swarm Manager裡的 Swarm Nodes

$ docker-machine ssh <VM Name> "<指令>"                         # 指定<VM Name>, 執行<指令>

$ docker-machine env <VM Name>                                  # 

```