# [Docker Network](https://docs.docker.com/network/#network-drivers)
- 2018/05

```sh
$ docker --version
Docker version 18.03.0-ce, build 0520e24
```

## 簡單談談 Docker Network, 大概可以分為5種(吧)
- 底下寫得非常~~~~的夢幻, 建議去看原文(但我相信看了會覺得更加夢幻)

1. Bridge(default)
    * 需要多個 Container相互溝通, 預設是使用這個

2. Host
    * 直接使用 Docker Host端的 Networking
    * 17.06版後, Docker Swarm 只能使用這個 Network Driver
    * 若 Network Stack 不應該與 Docker Host隔絕, 但希望其他方面能隔絕, 就用這個(鬼才看得懂這在寫什麼)

3. Overlay
    * 讓 Swarm 與 Container 之間溝通
    * 若需要 Containers在不同的 Docker Hosts 之間相互溝通, or 多個 Application 在 Swarm Services之間相互溝通, 就用這個

4. Macvlan
    * 可在 Container內, 安排 Mac Address (我不知道這啥...)
    * 比較老舊的 Application若要直接(而非透過 Docker Host's Network Stack來做 router) 與 實體網路連接, 用這個就對了
    * 若要 migrating from VM setup, or 要 Containers 在 Network 運作上, 看起來就像 pyhsical hosts(每個 Container 都有各自的 Mac Address), 就用這個.

5. None
    * 關閉 Container 內的 Networking

6. Third-party-plugin


# [1.Bridge Network](https://docs.docker.com/network/bridge/)
- 2018/06/03

```sh
# 如果啟用 Container 時, 沒有使用「--network <Name>」指定網卡的話, 預設會使用下面這張~
> docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
5bdb7fd05ba8        bridge              bridge              local
```

> `Bridge Network` 屬於 `Link Layer device`. 它隔離了網路區段之間的 資料傳輸 (藉由設定相同的 Bridge, Containers 之間可相互溝通). 在 *Host端*, **Docker Bridge Driver** 會被自動安裝. `Docker Container` 預設上會自動使用「bridge」的 bridge network, 它會自動開放所有 ports 給所有套用相同 Network 的 Container, 且可以 **`share 彼此的環境變數`**, 但它不對外開放. `BRIDGE` Containers 之間透過 IP Address 相互溝通, 老舊時期的做法, 則是使用 「--link」

## Default Bridge Network (以下簡稱 BRIDGE) (( Production 別用這個!! ))
> `BRIDGE` 預設無法讓 Container 傳遞資訊到 外界(outside world), 例如: 不同 Docker Host 之間的 Container 要相互溝通的話, 有2種解法:

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

# [2.Overlay Network](https://docs.docker.com/network/overlay/)



# [3.Host Networking](https://docs.docker.com/network/host/)
- 官方說明很簡短, 但我看不懂它想說什麼... 傻眼
```sh
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
6665f5c15572        host                host                local
# host 這張網卡
```

# [4.Macvlan Networks](https://docs.docker.com/network/macvlan/)

# 