# [Docker Network](https://docs.docker.com/network/#network-drivers)
- 2018/05

```sh
$ docker --version
Docker version 18.03.0-ce, build 0520e24
```

## 簡單談談 Docker Network, 大概可以分為5種(吧)
- 底下寫得非常~~~~的夢幻, 建議去看原文(但我相信看了會覺得更加夢幻)

1. Bridge(default)
    需要多個 Container相互溝通, 預設是使用這個

2. Host
    * 直接使用 Docker Host端的 Networking
    * 17.06版後, Docker Swarm 只能使用這個 Network Driver
    * 若 Network Stack 不應該與 Docker Host隔絕, 但希望其他方面能隔絕, 就用這個(鬼才看得懂這在寫什麼)

3. Overlay
    * 讓 Swarm 與 Container 之間溝通
    * 若需要 Containers在不同的 Docker Hosts 之間相互溝通, or 多個 Application 在 Swarm Services之間相互溝通, 就用這個(鬼看得懂, 去問他)

4. Macvlan
    * 可在 Container內, 安排 Mac Address (我不知道這啥...)
    * 比較老舊的 Application若要直接(而非透過 Docker Host's Network Stack來做 router) 與 實體網路連接, 用這個就對了
    * 若要 migrating from VM setup, or 要 Containers 在 Network 運作上, 看起來就像 pyhsical hosts(每個 Container 都有各自的 Mac Address), 就用這個.

5. None
    * 關閉 Container 內的 Networking

6. Third-party-plugin


## [Bridge Network](https://docs.docker.com/network/bridge/)

```sh
# 語法: 指定 Network, 並且開放 Port號 映射, 建立 Container
$ docker create --name <Container Name> --network <Network Name> --publish <要開放給 Docker Host 的 port>:<Container內服務的 port>

$ docker network connect <Network Name>         # 附加 Network
$ docker network disconnect <Network Name>      # 拔掉 Network

# 範例~
$ docker create --name my-nginx --network my-net --publish 8080:80 nginx:latest
# 使用名為 nginx:latest 的 Image 來建立名為 my-nginx 的 Container, 此 Container 使用名為 my-net 的自定義 Network,
# Docker Host端 可透過 8080 port 來用 Container 內的 80 port 所提供的服務.

# 把 running 中的 my-nginx(Container)附加 my-net(Network)
$ docker network connect my-net my-nginx
# 此指令使用前提: my-nginx 一定要是個 running Container
```

> `Default Bridge Network` 預設無法讓 Container 傳遞資訊到 外界(outside world), 若要做此功能, 則需要做 2個非 Docker的設定
1. 讓Linux kernel 允許 IP routing
```sh
$ sysctl net.ipv4.conf.all.forwarding=1
```

2. 設定「iptables FORWARD policy」為 ACCEPT(原為 DROP)
```sh
$ sudo iptables -P FORWARD ACCEPT
```
