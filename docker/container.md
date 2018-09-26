# Windows vs Linux Container

- 2018/09/20


```powershell
### Linux Container
> docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
7280e8a0597c        bridge              bridge              local
a26f1acc48e6        host                host                local
5c32253289c9        none                null                local


### Windows Container
> docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
45f5073a72bf        ExternalSwitch      transparent         local
619942edbcff        nat                 nat                 local
b26d7431a85e        none                null                local
3432c65f886b        預設切換             ics                 local
```

![HyperV Linux Container](../img/HypervLinuxContainer.jpg)

MobyLinuxVM 是啟用 Linux Container 之後才出現的, 原本我使用 Windows Container 時, 還看不到它, 但要使用 Linux Images 時, 發現 Windows Container 無法使用, 切換到 Linux Container 之後, 它就出現了!!


```powershell
> ipconfig


### 1
乙太網路卡 vEthernet (InternalSwitch):

   連線特定 DNS 尾碼 . . . . . . . . :
   連結-本機 IPv6 位址 . . . . . . . : fe80::c941:1ad4:5463:ad66%7
   自動設定 IPv4 位址 . . . . . . . .: 169.254.173.102
   子網路遮罩 . . . . . . . . . . . .: 255.255.0.0
   預設閘道 . . . . . . . . . . . . .:

### 2
乙太網路卡 vEthernet (ExternalSwitch):

   連線特定 DNS 尾碼 . . . . . . . . :
   連結-本機 IPv6 位址 . . . . . . . : fe80::80f5:8c6f:43f9:dd4f%21
   IPv4 位址 . . . . . . . . . . . . : 192.168.124.101
   子網路遮罩 . . . . . . . . . . . .: 255.255.255.0
   預設閘道 . . . . . . . . . . . . .: 192.168.124.254

### 3
乙太網路卡 vEthernet (nat):

   連線特定 DNS 尾碼 . . . . . . . . :
   連結-本機 IPv6 位址 . . . . . . . : fe80::690f:d8e:dec8:255a%29
   IPv4 位址 . . . . . . . . . . . . : 172.25.144.1
   子網路遮罩 . . . . . . . . . . . .: 255.255.240.0
   預設閘道 . . . . . . . . . . . . .:

### 5
乙太網路卡 vEthernet (預設切換):

   連線特定 DNS 尾碼 . . . . . . . . :
   連結-本機 IPv6 位址 . . . . . . . : fe80::6d63:b9d7:b1eb:229a%18
   IPv4 位址 . . . . . . . . . . . . : 172.22.35.1
   子網路遮罩 . . . . . . . . . . . .: 255.255.255.240
   預設閘道 . . . . . . . . . . . . .:

### 6
乙太網路卡 vEthernet (DockerNAT):

   連線特定 DNS 尾碼 . . . . . . . . :
   IPv4 位址 . . . . . . . . . . . . : 10.0.75.1
   子網路遮罩 . . . . . . . . . . . .: 255.255.255.0
   預設閘道 . . . . . . . . . . . . .:
```

![HyperV Virtual Switch](../img/vSwitch.jpg)
