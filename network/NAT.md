# Network Address Translation, NAT - 網路位址轉換

- 2018/09/28


# Linux 防火牆的主要類別

參考來源: 鳥哥的Linux伺服器架設(第三版)(CentOS6), 與現行的 CentOS7 不知道差多少...

區分為 `網域型` 與 `單一主機型`

- 單一主機型
    - Netfilter
    - TCP Wrappers
- 網域型(區域型) - 都拿來當作 `Router`
    - Netfilter
    - Proxy


## 1. Netfilter (封包過濾機制)

取出來源請求封包表頭, 分析 `MAC`, `IP`, `TCP`, `UDP`, `ICMP`...

主要分析 OSI 的 2, 3, 4 層


## 2. TCP Wrappers (程式控管)

分析 誰對某程式進行存取, 該 Server 誰能連線、誰不能 ; 因為標的是`程式`, 所以與啟動的 port 無關, 只與程式名稱有關


## 3. Proxy (代理伺服器)

偽裝內部網路對外的請求, 由統一的 Public IP 為對外窗口.


# Windows 10 1803 Hyper-V 預設切換:

```powershell
> ipconfig 預設切換
乙太網路卡 vEthernet (預設切換):

   連線特定 DNS 尾碼 . . . . . . . . :
   連結-本機 IPv6 位址 . . . . . . . : fe80::6d63:b9d7:b1eb:229a%18
   IPv4 位址 . . . . . . . . . . . . : 172.22.35.1
   子網路遮罩 . . . . . . . . . . . .: 255.255.255.240
```


## NAT Server 功能區分

POSTROUTING         | PREROUTING
------------------- | ----------
Source NAT, SNAT    | Destination NAT, DNAT
外送                 | 內收
偽裝封包             | 轉發封包
改來源IP             | 改目標IP
對外請求, 隱藏內部IP  | 處理外來請求, 轉發給內部IP
ex: IP分享器         | ex: Web Server

###### note: NAT 一定是個 Router

****************************



