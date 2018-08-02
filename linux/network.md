# CentOS7 網路相關問題及指令備註

- 2018/06/08

> 網路卡相關組態放在這邊 : `/etc/sysconfig/network-scripts/`



# 常用網路相關指令

- ifconfig
- ifup, ifdown : 只能針對 `/etc/sysconfig/network-scripts/` 內的 `ifcfg-ethXX` 進行動作
- route
- ip


```sh
# 可以在 CLI 底下編輯 網卡(手動設定IP等)
$ nmtui edit <網卡名稱>

# 顯示網卡資訊

$ nmcli dev status
DEVICE   TYPE       STATE           CONNECTION
eth0     ethernet   disconnected    --
lo       loopback   unmanaged       --
```



# 更改 ip

```sh
$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    ...(略)...
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 00:15:5d:64:05:08 brd ff:ff:ff:ff:ff:ff
    inet 192.168.137.47/24 brd 192.168.137.255 scope global dynamic eth0    # 原本只有這個
       valid_lft 604794sec preferred_lft 604794sec
    inet6 fe80::f044:abf9:731c:462f/64 scope link
       valid_lft forever preferred_lft forever

# 進入 su
$ cd /etc/sysconfig/network-scripts/
$ ls
ifcfg-eth0   ifdown-eth   ifdown-isdn    ...(大概有三四十個...(略))

$ vi ifcfg-eth0
IPADDR=192.168.137.99       # 修改 or 增加這行

$ systemctl restart network
# 重啟網路服務後~~

$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    ...(略)...
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 00:15:5d:64:05:08 brd ff:ff:ff:ff:ff:ff
    inet 192.168.137.99/24 brd 192.168.137.255 scope global eth0    # 多出來的~~
       valid_lft forever preferred_lft forever
    inet 192.168.137.47/24 brd 192.168.137.255 scope global secondary dynamic eth0    # 這是原本的
       valid_lft 604797sec preferred_lft 604797sec
    inet6 fe80::f044:abf9:731c:462f/64 scope link
       valid_lft forever preferred_lft forever
# Host 可以 用 192.168.137.47 及 192.168.137.99 找到它了~
```
