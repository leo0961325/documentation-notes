# [Docker Network](https://docs.docker.com/network/#network-drivers)
- 2018/05
- 範例以 18.03版 作說明

> Docker 從 [v17.09](https://docs.docker.com/v17.09/engine/userguide/networking/) -> [v17.12](https://docs.docker.com/v17.12/network/#network-drivers), 把 Networking 的部分幾乎是作了翻盤式的修改(我也不清楚啦! 但說明文件看起來變很多就是了XD), 而 17.12 -> 18.03, 應該是差不多吧@@? 先暫時把他們當成一樣了.

```sh
$ docker --version
Docker version 18.03.0-ce, build 0520e24
```

## [Docker Network](https://docs.docker.com/network/#network-drivers) 分為5種

1. [bridge Networks](https://docs.docker.com/network/bridge/) (預設)
    * 需要多個 Container相互溝通, 預設是使用這個

2. [host Network](https://docs.docker.com/network/host/)
    * 直接使用 Docker Host 端的 Networking
    * v17.06後, Docker Swarm 只能使用這個 Network Driver
    * `只有 Linux Docker能用這個!` Windows, Mac無法使用!

3. [overlay Networks](https://docs.docker.com/network/overlay/)
    * 讓 Swarm 與 Container 之間溝通
    * 若需要 Containers在不同的 Docker Hosts 之間相互溝通, or 多個 Application 在 Swarm Services之間相互溝通, 就用這個

4. [macvlan Networks](https://docs.docker.com/network/macvlan/)
    * 可在 Container內, 安排 Mac Address (我不知道這啥...)
    * 比較老舊的 Application若要直接(而非透過 Docker Host's Network Stack來做 router) 與 實體網路連接, 用這個就對了
    * 若要 migrating from VM setup, or 要 Containers 在 Network 運作上, 看起來就像 pyhsical hosts(每個 Container 都有各自的 Mac Address), 就用這個.

5. [none](https://docs.docker.com/network/none/)
    * 關閉 Container 內的 Networking
    * 使用 `--network none` 來關閉 Container Network 服務

6. Third-party-plugin
    - 無...

---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------

# Network

> Note: `Class B 的私有IP位址區間 : 172.16.0.1 ~ 172.31.255.254`

```sh
$ ip addr show
docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN
    link/ether 02:42:8d:79:3e:79 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
        valid_lft forever preferred_lft forever
```

> The default `docker0` bridge network supports the use of port mapping and `docker run --link` to allow communications among containers in the `docker0` network (**NOT RECOMMENDED**) . Where possible, you should use user-defined bridge networks instead. [default-bridge-network v17.09](https://docs.docker.com/v17.09/engine/userguide/networking/#the-default-bridge-network)

```sh
# 查看「bridge 網卡」的資訊
# docker network inspect <NetworkName>
$ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "eada4c9a...",
        "Created": "2018-06-19T17:36:50.250035871+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",  # Network Name
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,        # 這好像有點用處, 但做啥我忘了
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "a4804542...": {    # Container 2
                "Name": "alpine2",
                "EndpointID": "eab620...",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            },
            "b8387f41...": {    # Container 1
                "Name": "alpine1",
                "EndpointID": "5fff71...",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
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



# [1.bridge network driver](https://docs.docker.com/network/bridge/)
- 2018/06/03

```sh
# 如果啟用 Container 時, 沒有使用「--network <Name>」指定網卡的話, 預設會使用下面這張~
> docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
5bdb7fd05ba8        bridge              bridge              local
```

> `Bridge Network` 屬於 `Link Layer device`. 它隔離了網路區段之間的 資料傳輸 (藉由設定相同的 Bridge, Containers 之間可相互溝通). 在 *Docker Host*, **bridge driver** 會被自動安裝. `Docker Container` 預設上會自動使用「bridge」的 bridge network, 它會自動開放所有 ports 給所有套用相同 Network 的 Container, 且可以 **`share 彼此的環境變數`**, 但它 <font color="lightgreen">不對外開放</font> . `bridge` Containers 之間透過 IP Address 相互溝通, 老舊時期的做法, 則是使用 「--link」

## Default Bridge Network (以下簡稱 BRIDGE) (( Production 別用這個!! ))
> `BRIDGE` 預設無法讓 Container 傳遞資訊到 外界(outside world), 例如: 不同 Docker Host 之間的 Container 要相互溝通的話, 有2種解法:

```sh
# Container 附加網卡
$ docker network connect <Network Name> <Container Name>

# Container 拔掉網卡
$ docker network disconnect <Network Name> <Container Name>
```


### 法一: 作底下 2 個設定

1. 在 `OS Level` 設定 routing
```sh
# ex: 讓Linux kernel 允許 IP routing
$ sysctl net.ipv4.conf.all.forwarding=1
```

2. 設定「iptables FORWARD policy」為 ACCEPT(原為 DROP)
```sh
$ sudo iptables -P FORWARD ACCEPT
```

### 法二: 改用 `Overlay Network` 

```sh
$ docker network   create       <Network Name>      # 建立 Network
$ docker network   rm           <Network Name>      # 移除 Network
$ docker network   connect      <Network Name>      # 附加 Network 到 running Container
$ docker network   disconnect   <Network Name>      # 拔掉 Network

# 語法: 指定 Network, 並且開放 Port號 映射, 建立 Container
$ docker create --name <Container Name> --network <Network Name> --publish <Host Port>:<Container Port>

# 範例~
$ docker create --name my-nginx --network my-net --publish 8080:80 nginx:latest
# 使用名為 nginx:latest 的 Image 來建立名為 my-nginx 的 Container, 此 Container 使用名為 my-net 的自定義 Network,
# Docker Host端 可透過 8080 port 來用 Container 內的 80 port 所提供的服務.
```

要使用 IPv6 的話, [看這邊](https://docs.docker.com/network/bridge/#use-ipv6), 筆記略...

## [User-defined bridge network 使用者自訂網卡](https://docs.docker.com/network/network-tutorial-standalone/#use-user-defined-bridge-networks)
- 2018/06/19

- `user-defined bridge` 已經自動做好了 **automatic service discovery**, 也就是說, Containers 之間可以 `ping ip` 也可 `ping ContainerName` ; 而 `default bridge` 則只能 `ping ip`

```sh
$ docker network create --driver bridge alpine-net

$ docker network inspect alpine-net
[
    {
        "Name": "alpine-net",   # 建立 User-defined network
        "Id": "2e2529cab4...",
        "Created": "2018-06-19T21:56:36.142750051+08:00",
        "Scope": "local",
        "Driver": "bridge",     # Network Driver 為 bridge
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",  # Network Name 為 172.18.0.0/16
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
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]

# 使用 alpine image 建立 4 個 Container, 並指定 network driver
$ docker run -dit --name alpine1 --network alpine-net alpine ash    # alpine1 指定 alpine-net 網卡
$ docker run -dit --name alpine2 --network alpine-net alpine ash    # alpine2 指定 alpine-net 網卡
$ docker run -dit --name alpine3 alpine ash                         # alpine2 不指定網卡 (預設採用 bridge)
$ docker run -dit --name alpine4 --network alpine-net alpine ash    # alpine4 指定 alpine-net 網卡
$ docker network connect bridge alpine4                             # alpine4 額外附加 bridge 網卡

$ docker container ls
CONTAINER ID    IMAGE     COMMAND    CREATED    STATUS    PORTS    NAMES
e5f58da319fa    alpine    "ash"      (pass)     (pass)    alpine4           # 172.18.0.4/16     172.17.0.3/16
5e8bbe5278ac    alpine    "ash"      (pass)     (pass)    alpine3           #                   172.17.0.2/16
20a3f3cfa029    alpine    "ash"      (pass)     (pass)    alpine2           # 172.18.0.3/16
3e0817ad0f2a    alpine    "ash"      (pass)     (pass)    alpine1           # 172.18.0.2/16

# alpine1, alpine2, alpine4 附加了 "alpine-net network"    subnet: 172.18.0.0/16
# alpine3, alpine4          附加了 "bridge     network"    subnet: 172.17.0.0/16
# 以上 4個 Containers 都具有對外網路的功能(都可以 ping google.com)
```


## 範例

```sh
$ docker network ls
NETWORK ID      NAME               DRIVER    SCOPE
eada4c9a1c64    bridge             bridge    local  # 此次的主角
dc201b36ce6d    host               host      local
1d7619669ced    none               null      local

$ docker run -dit --name alpine1 alpine ash
$ docker run -dit --name alpine2 alpine ash
# 使用 ash (而非 bash) 來作為執行的程式
# 使用 alpine image 建立名為 alpine1, alpine2 的 Container
# 預設上, 都會附加 bridge network

$ 

```

# [2.Overlay Network](https://docs.docker.com/network/overlay/)

TODO: 2018/06/14 - https://docs.docker.com/v17.09/engine/userguide/networking/#overlay-networks-in-swarm-mode



# [3.Host Networking](https://docs.docker.com/network/host/)
- [Host Networking Tutorial](https://docs.docker.com/network/network-tutorial-host/)
- `host networking driver` 只能在 Docker on Linux 使用
- v17.06之後, `host network driver` 也可藉由 `--network host` 用在 swarm service
- `host driver` 直接與 `Docker Host` 做連結(自動 mapping 所有 ports)

```sh
$ docker network ls
NETWORK ID      NAME      DRIVER    SCOPE
572ead22f29c    bridge    bridge    local
a3bab954f849    host      host      local   # 此次的主角~~
faa4e0b64151    none      null      local
```
## 範例 (只能在 Docker for Linux 執行)

```sh
$ docker run --rm -d --network host --name my_nginx nginx
# --rm : stop Container 後, 一併刪除 Container
# -d : 背景執行
# 使用 名為 "host" 的 network driver (這張網卡使用 host driver)
# 建立 container: my_nginx
# 使用 image: nginx, 

# 有網頁了~~「http://localhost:80/」  

# 使用預設的 host network driver, 所以不會建立新的網卡
$ ip addr show

# 檢查 80 port 上有什麼服務
$ sudo netstat -tulpn | grep :80
Proto  Recv-Q  Send-Q  Local Address  Foreign Address  State   PID/Program name
tcp         0       0  0.0.0.0:80     0.0.0.0:*        LISTEN  23988/nginx: master
# 因為在建立 nginx docker image時, 已經在 Dockerfile 定義好了「EXPOSR 80」

# firewall 開放 port 80 port
$ sudo firewall-cmd --zone=public --add-port=80/tcp

# firewall 關閉 port
$ firewall-cmd --zone=public --remove-port=80/tcp

# 別台電腦, 也可藉由 ip, 用瀏覽器看 80 port了~~
```



# [4.Macvlan Networks](https://docs.docker.com/network/macvlan/)



# [5. none network](https://docs.docker.com/network/none/)
- 2018/06/19

關閉 Docker Container Network, Container內, 將不再有 `eth0` 這張網卡

```sh
$ docker run --rm -dit --network none --name no-net-alpine alpine:latest ash

$ docker attach no-net-alpine

$ ifconfig  # 只有 lo 而已
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

# <Ctrl+p> + <Ctrl+q> 離開

$ docker exec no-net-alpine ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN qlen 1
    link/ipip 0.0.0.0 brd 0.0.0.0
3: ip6tnl0@NONE: <NOARP> mtu 1452 qdisc noop state DOWN qlen 1
    link/tunnel6 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00 brd 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00

$ docker exec no-net-alpine ip route
# 沒有回傳值~~ 因為沒有網路, routing table 是空der
```