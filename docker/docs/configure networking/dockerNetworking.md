# [Network containers](https://docs.docker.com/v17.09/engine/tutorials/networkingcontainers/)
- 2018/01/07
- 官方估計閱讀時間 6分鐘, 林北看了 3小時, 乾~


`圖1`<br> 本章目標, 要把 Container的網路服務弄成這架構<br>
![圖1](./../img/bridge3.jpg)

## Prerequest
1. 略懂網路架構(起碼看上圖能有點感覺)
2. 安裝完 Docker Engine, 我的版本如下:
```sh
$ docker --version
Docker version 17.09.0-ce, build afdb6d4
```
2. 知道 Docker Container是啥東西
3. 知道 Docker Image是啥東西
---
## 概念
Docker可以藉由設定 Network Driver來部屬 Network Container, 而 Network Driver大致上分為 2類
Network Driver | 說明
--- | ---
bridge(預設) | 只能使用在單一本地端(single host)<br>**A bridge network is limited to a single host running Docker Engine.**
overlay(進階) | 可以包含多數本地端(multiple host)<br>**An overlay network can include multiple hosts and is a more advanced topic.**
(其他自行實作) | 超級高深... 不討論


---

## 建立 network
> 建立 network 語法: <br>
`docker network create <NetworkName>` 或 <br>
                    `docker network create -d <Network Driver> <NetworkName>` <br>
> 刪除 network 語法: <br>`docker network rm <NetworkName>`
```sh
$ docker network ls
NETWORK ID      NAME         DRIVER      SCOPE
0bd6efb035c9    bridge       bridge      local
79a16ba00d8f    host         host        local
7406af2c5d03    none         null        local
# 安裝完 Docker後, 都會有上述 3個預設的 Networks

$ docker network create -d bridge my_bridge     # "-d bridge"可以省略
ccee7fa10da92e031943d8d4b6da378a6fceb11f7407d500e658b41f531e082d
# 建立一個 network, 名為 my_bridge
# 此 network的 driver為 bridge

$ docker network ls
NETWORK ID      NAME         DRIVER      SCOPE
0bd6efb035c9    bridge       bridge      local
79a16ba00d8f    host         host        local
7406af2c5d03    none         null        local
ccee7fa10da9    my_bridge    bridge      local
```

先隨便建立一個運行中的 Container, 但並未指定要用哪種 network driver(預設會使用 bridge)
```sh
$ docker run -itd --name=networktest ubuntu
# 建立 Image為 "ubuntu" 的 Container
# -it為持續執行
# -d為背景執行
# --name=networktest為 Container的名稱
# 這邊沒指定要用哪個 network driver, 所以會採用預設的 bridge

$ docker container ls
CONTAINER ID   IMAGE    COMMAND       CREATED         STATUS         PORTS   NAMES
a9155d48e932   ubuntu   "/bin/bash"   2 minutes ago   Up 2 minutes           networktest
```

`圖2` 剛剛建立的 Container, 看起來像這樣<br>

![bridge](./../img/docker_bridge.jpg)

可以透過下面的指令, 來看看目前有哪些 bridges以及它們的組態設定

> 檢查 <Network>指令:<br>
`docker network inspect <Network Name>` 或<br>
`docker inspect <Network Name>`
```sh
# 這邊我們來檢查 Docker一開始預設的 bridge
$ docker network inspect bridge
[
    {       # 預設 bridge0
        "Name": "bridge",
        "Id": "0bd6efb035c91503015c14260315a4ecaa6f4f2d2128d85796aae018b8eb4be8",
        "Created": "2018-01-07T23:00:31.287691388+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {     # 套用這 bridge的 Container ((請注意這個 Container大概長這樣))
            "6b3c1331550af2085d5aad0514f666e76fcac6d8d3c83276ecf5186509edbd7f": {
                "Name": "networktest",                  # network名稱
                "EndpointID": "66d57c96943e88f35a1a6c382abcfd1ef3b8a5e22132d243b9590987190919ca",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",         # IP在這!!
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```

> 如果不想讓 Container具有 network的功能, 可以用下面指令把 network給拔掉, 指令為: <br>`docker network disconnect <Network Driver名稱> <Container Name>` 或<br>
`docker network disconnect <Network Driver Name> <Container ID>`
```sh
# 把 networktest這個 Container的 network功能給拔掉
$ docker network disconnect bridge networktest

# 再次檢查...
$ docker network inspect bridge
[
    {
        "Name": "bridge",       # 這個是預設的 Network Name, 無法被移除!!
        "Id": "0bd6efb035c91503015c14260315a4ecaa6f4f2d2128d85796aae018b8eb4be8",
        "Created": "2018-01-07T23:00:31.287691388+08:00",
        "Scope": "local",
        "Driver": "bridge",     # 這個是 <Network Name>的 bridge
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},           # 此表示, 目前沒有任何一個 Container是套用此 bridge
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```

在想想 `圖1`的架構, 我們先來看看 my_bridge這塊網卡
```sh
$ docker network inspect my_bridge
[
    {
        "Name": "my_bridge",
        "Id": "ccee7fa10da92e031943d8d4b6da378a6fceb11f7407d500e658b41f531e082d",
        "Created": "2018-01-07T23:21:24.650496745+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,        # 底下沒有 Container這個東西, 要把套用這個 bridge的 Container納近來
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```

## 把 Database Container加入到 my_bridge
```sh
$ docker run -d --net=my_bridge --name db training/postgres
9c815ee0bfcd197c8177e004e7c2db4e610d7ae241cba62532b7a2e51a04c5d3
# --net=my_bridge : 指定 Network Name為 my_bridge
# --name db : Container NAME為 db
# Docker Image的 Repository 為 training/postgres

# 再次檢查 my_bridge
$ docker inspect my_bridge
[
    {
        "Name": "my_bridge",
        "Id": "ccee7fa10da92e031943d8d4b6da378a6fceb11f7407d500e658b41f531e082d",
        "Created": "2018-01-07T23:21:24.650496745+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {     # 將將!! db這個 Container使用此 network囉
            "9c815ee0bfcd197c8177e004e7c2db4e610d7ae241cba62532b7a2e51a04c5d3": {
                "Name": "db",
                "EndpointID": "e62473d303528e2f956b44eaeaca13c2abb21a097cf4c1432865dff32bc4c7c5",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]

# 另外, 也可以反過來檢查 Container連結到哪個 network
$ docker inspect --format='{{json .NetworkSettings.Networks}}'  db
{
    "my_bridge": {
        "IPAMConfig": null,
        "Links": null,
        "Aliases": [
            "9c815ee0bfcd"
        ],
        "NetworkID": "ccee7fa10da92e031943d8d4b6da378a6fceb11f7407d500e658b41f531e082d",
        "EndpointID": "e62473d303528e2f956b44eaeaca13c2abb21a097cf4c1432865dff32bc4c7c5",
        "Gateway": "172.18.0.1",
        "IPAddress": "172.18.0.2",
        "IPPrefixLen": 16,
        "IPv6Gateway": "",
        "GlobalIPv6Address": "",
        "GlobalIPv6PrefixLen": 0,
        "MacAddress": "02:42:ac:12:00:02",
        "DriverOpts": null
    }
}
# 上面的結果我把它美化過了!! 不然原始格式全部擠成一團...
```

回想`圖1`, 開始架設左半部的 Container囉~
```sh
$ docker run -d --name web training/webapp python app.py
# -d : 背景執行
# --name web : Container Name為 web
# training/webapp : Image Name
# python app.py : 一進入 Container後, 立即執行此字串

$ docker container ls
CONTAINER ID   IMAGE              COMMAND                  CREATED     STATUS     PORTS        NAMES
e1468e5ff61a   training/webapp    "python app.py"          (pass)      (pass)     5000/tcp     web
9c815ee0bfcd   training/postgres  "su postgres -c '/..."   (pass)      (pass)     5432/tcp     db
6b3c1331550a   ubuntu             "/bin/bash"              (pass)      (pass)                  networktest

# 檢查剛剛建立的 web Container採用哪種 network
$ docker inspect --format='{{json .NetworkSettings.Networks}}'  web
{
    "bridge": {
        "IPAMConfig": null,
        "Links": null,
        "Aliases": null,
        "NetworkID": "0bd6efb035c91503015c14260315a4ecaa6f4f2d2128d85796aae018b8eb4be8",
        "EndpointID": "b9c316dae8202717ad21afa9af1c0a8cf70afee5acc5a197eef420f9cac882f6",
        "Gateway": "172.17.0.1",
        "IPAddress": "172.17.0.2",
        "IPPrefixLen": 16,
        "IPv6Gateway": "",
        "GlobalIPv6Address": "",
        "GlobalIPv6PrefixLen": 0,
        "MacAddress": "02: 42:ac: 11: 00: 02",
        "DriverOpts": null
    }
}
# ((上面結果已手動美化...))

# 取得此 Container的 IP Address
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
172.17.0.2
```

## 開啟2個 Shell

### Shell 1: 進入 db 這個 Container
```sh
$ docker exec -it db bash

root@9c815ee0bfcd:/# ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:12:00:02  
          inet addr:172.18.0.2  Bcast:0.0.0.0  Mask:255.255.0.0            # 注意這邊的 ip
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:136 errors:0 dropped:0 overruns:0 frame:0
          TX packets:23 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:21057 (21.0 KB)  TX bytes:2198 (2.1 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:39 errors:0 dropped:0 overruns:0 frame:0
          TX packets:39 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:2701 (2.7 KB)  TX bytes:2701 (2.7 KB)

root@9c815ee0bfcd:/# ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
# 然後就停住了!!! ping不到 web Container阿~~~
# 因為兩者根本就是在不同的網段!!!
```
### Shell 2: 進入 web 這個 Container
```sh
$ docker exec -it db web

root@e1468e5ff61a:/opt/webapp# ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:02  
          inet addr:172.17.0.2  Bcast:0.0.0.0  Mask:255.255.0.0             # 注意這邊的 ip
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:58 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:8688 (8.6 KB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

`圖4`: 目前的 Container network架構, 導致 web ping不當db<br>
![圖4](./../img/bridge2.jpg)<br>
解法是, 只需要讓 web附加與 db相同的`虛擬網卡`就行了!!

> 附加網卡的指令`docker network connect <Network Name> <Container Name>`
```sh
$ docker network connect my_bridge web
```

如此一來, 架構就完成了!!<br>
![圖1](./../img/bridge3.jpg)<br>
web 與 db可以找到彼此了!!

```sh
$ docker exec -it db bash

root@9c815ee0bfcd:/# ping web
64 bytes from web.my_bridge (172.18.0.3): icmp_seq=1 ttl=64 time=0.350 ms
64 bytes from web.my_bridge (172.18.0.3): icmp_seq=2 ttl=64 time=0.145 ms
64 bytes from web.my_bridge (172.18.0.3): icmp_seq=3 ttl=64 time=0.160 ms
...
```
---

## 指令備註
```sh
# 查看<Network>這張虛擬網路卡的組態
$ docker network inspect <Network Name>         # "network"可省略

# 抓取特定 Container的 network IP Address
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <Container ID>
```