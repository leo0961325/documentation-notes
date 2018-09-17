# Linux
- 相關指令
- 知識概念備註
- [Ubuntu16.04的pdf](http://arbas.assam.gov.in/resources/pdf/ubuntu_16.04.pdf)
- [還蠻初階的語法教學](https://www.puritys.me/docs-blog/article-357-Linux-%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4%E6%95%99%E5%AD%B8.html)

```sh
# 此篇指令及概念, 主要都作用在 CentOS 7  (半年前是 7.3版, N 個月前下了 yum update 後, 升級成 7.4了...)
$ cat /etc/centos-release
CentOS Linux release 7.4.1708 (Core)

$ uname -a
Linux tonynb 3.10.0-693.21.1.el7.x86_64 #1 SMP Wed Mar 7 19:03:37 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

# 這東西需要額外安裝 yum install redhat-lsb
$ lsb_release -a
LSB Version:    :core-4.1-amd64:core-4.1-noarch
Distributor ID: CentOS
Description:    CentOS Linux release 7.4.1708 (Core)
Release:        7.4.1708
Codename:       Core
```



# EPEL(Extra Packages for Enterprise Linux)
> Linux在安裝許多軟體的時候(ex: yum install ...), 會有軟體相依性的問題, 若發現相依軟體尚未被安裝, yum會自己去`本地 repository`裡頭找有記載的`遠端 repository`去下載相依套件. 而 EPEL就是專門 for CentOS的套件庫, 裡頭有許多CentOS的核心套件. <br>查看補充說明: 
[What is EPEL](https://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/)
```sh
$ sudo yum install -y epel
```



# Linux的軟體管理員 - rpm

### - rpm vs dpkg

distribution 代表 | 軟體管理機制 | 使用指令 | 線上升級機制(指令)
--- | --- | --- | ---
Red Hat/Fedora | RPM | rpm, rpmbuild | YUM (yum)
Debian/Ubuntu | DPKG | dpkg | APT (apt-get)


### - rpm vs srpm

檔案格式 | 檔名格式 | 直接安裝與否 | 內含程式類型 | 可否修改參數並編譯
--- | --- | --- | --- | ---
RPM | xxx.rpm | 可 | 已編譯 | 不可
SRPM | xxx.src.rpm | 不可 | 未編譯之原始碼 | 可

rpm套件管理的語法: `rpm -<options> <xxx.rpm>`


### - options

options     | description
----------- | ------------
-i          | 安裝套件
-v          | 安裝時, 顯示細部的安裝資訊
-h          | 安裝時, 顯示安裝進度
-e          | 移除套件
-U          | 更新套件
-q          | 查詢套件資訊
-qa         | - 已安裝套件清單
-qi         | - 特定套件安裝資訊
-ql         | - 套件安裝了哪些東西
-qf         | - 某個東西是被哪個套件安裝的 (與 -ql相反)

```sh
# 可以反查某個檔案被哪個套件所安裝
$ rpm -qf /etc/fstab
setup-2.8.71-7.el7.noarch

##### 底下是範例程式及說明 #####
setup-2.8.71-4.el7.noarch   <---安裝包
  套件名稱: setup
  版本: 2.8.71
  修訂: 4, 修正 bug錯誤第4版
  適用發行版: el7, RedHat Enterprise Linux 7
  適用平台: noarch
```


### - sub options
sub options | description
----------- | ------------
--test      | 僅測試模擬安裝過程, 不會真正安裝`(移除時, 可嘗試用此搭配)`
--nodeps    | 忽略安裝前的相依性檢查
--force     | 強制安裝(若已安裝, 會覆蓋掉前次安裝)


### 常用選項
options     | description
----------- | ------------
-Uvh        | if 未安裝, then 直接安裝<br />if 安裝過舊版, then 版本升級
-Fvh        | if 未安裝, then 不動作<br />if 安裝過舊版, then 版本升級
-ivh        | 最常用的安裝方式, 安裝時, 顯示安裝資訊


### 主機 host

```sh
# 查看主機名稱資訊
$ hostnamectl
Static hostname: tonynb
         Icon name: computer-laptop
           Chassis: laptop
        Machine ID: e5c76287078c4e5fb54034d3d8b26e76
           Boot ID: 6d9919d9a79a4636b7e1da1d0c060cde
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-514.el7.x86_64
      Architecture: x86-64

# 設定新的主機名稱
$ hostnamectl set-hostname <new host name>
```



---
## Linux的軟體管理員 - yum
> 解決 rpm安裝時, 套件相依性的問題

```sh
$ yum install <套件名稱>

$ yum update <套件名稱>

$ yum remove <套件名稱>

$ yum searcn <套件名稱>
# 搜尋 YUM Server上的特定套件

$ yum list
# 列出 YUM Server上的所有套件資訊, 套件名稱, 版本, 是否已經安裝...

# 列出 系統可用的 yum套件庫
$ yum repolist
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: ftp.isu.edu.tw
 * elrepo: dfw.mirror.rackspace.com
 * epel: ftp.cuhk.edu.hk
 * extras: ftp.isu.edu.tw
 * updates: ftp.isu.edu.tw
repo id                         repo name                                        status
base/7/x86_64                   CentOS-7 - Base                                   9,591
code                            Visual Studio Code                                   29
docker-ce-stable/x86_64         Docker CE Stable - x86_64                            13
epel/x86_64                     Extra Packages for Enterprise Linux 7 - x86_64   12,382
extras/7/x86_64                 CentOS-7 - Extras                                   392
google-chrome                   google-chrome                                         3
mysql-tools-community/x86_64    MySQL Tools Community                                59
mysql57-community/x86_64        MySQL 5.7 Community Server                          247
updates/7/x86_64                CentOS-7 - Updates                                1,962
repolist: 24,950
```


---
## Linux安裝軟體方式 - 原始碼編譯 && 安裝
1. 取得原始碼
  - 大多為 `tar.gz`, 可用 `tar zxvf`解開
2. 觀看 README 與 INSTALL
  - README: 軟體的介紹
  - INSTALL: 編譯與安裝的方法及步驟
3. 設定組態
  - 使用 `./configure`, 並給予必要參數及選項
  - 產生 `Makefile`編譯腳本
4. 編譯與安裝
  - 使用 `make`進行編譯
  - 無誤後, 使用 `sudo make install`開始安裝



# 網路介面卡 && ifconfig

> CentOS7前: 網路介面卡名稱, eth0, eth1, ... 分別代表第1張網卡, 第2張網卡, ...; 名稱由 **開機時核心偵測的時機** 決定, 故可能因為更換硬體設備而異動. 網卡名稱變動可能造成防火牆錯誤.

> CentOS7: 裝置名稱改為 `p1p1, p2p1, p3p1`等 BIOS名稱, 目的是為了維持設備名稱的一致性, 並以 **名稱得知網路卡在主機板上插槽的位置**. 

```sh
$ ifconfig enp1s0
enp1s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.124.73  netmask 255.255.255.0  broadcast 192.168.124.255
        inet6 fe80::be4e:db5a:2ead:fc61  prefixlen 64  scopeid 0x20<link>
        ether c8:5b:76:7e:4d:8e  txqueuelen 1000  (Ethernet)
        RX packets 84842  bytes 6617933 (6.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3073  bytes 507757 (495.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ ifconfig enp1s0 up          # 開啟 enp1s0網路卡
$ ifconfig enp1s0 down        # 關閉 enp1s0網路卡 (別白痴到在 ssh時使用阿XD )

# 重新手動指定 ip
$ ifconfig enp1s0 <new IP>   

# 重新手動指定 ip及 mask
$ ifconfig enp1s0 <new IP> netmask <new Mask>

$ ip address show   # 

$ ip link show      # 類似 ip address show, 但省略 ip位址資訊
```
> `ip`指令可以拿來作 **變更網路組態**, **增刪改特定設備的 ip位址**.... 遇到再 google



# Linux檔案時間

- 2018/07/08
- 檔按時間有分成3種, 會因為各種因素, 電腦上可能會有`未來檔案`

在 Linux 理頭, 會有 3 個主要的變動時間
- modification time (mtime) : `檔案內容` 最後變動時間
- status time (ctime) : `檔案狀態` 最後變動時間 (ex: 權限, 屬性)
- access time (atime) : `檔案內容` 最近讀取時間... 被看了!... 害羞(>///<)

```sh
$ ll /etc/man_db.conf; ll --time=atime /etc/man_db.conf ; ll --time=ctime /etc/man_db.conf
-rw-r--r--. 1 root root 5171  6月 10  2014 /etc/man_db.conf     # 內容最後變動時間 (預設使用 mtime)
-rw-r--r--. 1 root root 5171  7月  8 19:33 /etc/man_db.conf     # 狀態最後變動時間
-rw-r--r--. 1 root root 5171  2月 27 14:05 /etc/man_db.conf     # 內容最近讀取時間
```



# cp, mkdir

```sh
# 遞迴複製
$ cp -r dir1 dir2
# 把 dir1 內所有東西, 都複製到 dir2

# 遞迴建立
$ mkdir -r d1/d2/d3/d4/f1
# 建立目錄結構
```



# touch 這東西

- 新增 檔案
- 修改 檔案時間 (mtime, atime), ctime 無法被修改

```sh
$ touch [-acdmt] <filename>
# -a : 僅改 access time   (參考 Linux檔案時間)
# -c : 僅修改檔案的時間 (若不存在則不建立)
# -d : 可以自己設定 修改時間... 「--date="日期or時間"」 或 「-d "2 days ago"」
# -m : 僅改 mtime
# -t : 依照 YYYYMMDDhhmm 設定想修改的時間

$ touch f1
$ ll f1
-rw-rw-r--. 1 tony tony 0  7月  8 22:05 f1
```



# 解除yum lock

```sh
$ sudo yum install -y mongodb-org
Loaded plugins: fastestmirror, langpacks
Existing lock /var/run/yum.pid: another copy is running as pid 7629.    # <-- 殺~~
Another app is currently holding the yum lock; waiting for it to exit...
  The other application is: PackageKit
    Memory : 300 M RSS (1.7 GB VSZ)
    Started: Sun Nov 26 13:05:36 2017 - 00:19 ago
    State  : Running, pid: 7629

$ sudo kill -9 7629
```



# - 設定terminal的熱鍵


    畫面右上角功能表 > 設定 > 鍵盤 > 快捷鍵 > 自訂捷徑列 > +
    Name: Terminal Shortcut
    Command: gnome-terminal
    再點選所要設定的熱鍵




# - shebang on Linux

- [run python script directly from command line](https://stackoverflow.com/questions/20318158/run-python-script-directly-from-command-line)

> Linux系統底下, 可在任何.py檔的第一行使用 `#!/usr/bin/python` ( 依照使用的 python位置而定 ), 執行此腳本時, 可以藉由下列方式來執行.<br>
> windows系統下, 若要使用同 shebang的功能, 再去google `cygwin`.

```sh
$ python pp.py
$ ./pp.py
```



# 常見系統環境變數

env variables  | description
-------------- | -----------------
$HOSTNAME      | tonynb
$HOME          | /home/tony
$PWD           | 目前位置
$PATH          | ...(一大堆)...
$USER          | tony
$UID           | 1000
$LANG          | en_US.UTF-8
$RANDOM        | 0~32767整數亂數
$?             | 上次指令結束後的狀態碼(0:true, 1:false)



# shell內
hotkey | description
------ | -----------
Ctrl+C | 中斷目前工作 ; 終止目前命令
Ctrl+D | 送出eof or 輸入結束特殊字元
Ctrl+Z | 暫停目前工作, 利用 `fg` 指令, 可以取得暫停的工作



---
## - 測試硬碟讀取效能
```sh
# 檢測硬碟讀取效能
$ sudo hdparm -Tt /dev/sda
[sudo] password for tony:

/dev/sda:
 Timing cached reads:   14942 MB in  2.00 seconds = 7478.28 MB/sec
 Timing buffered disk reads: 344 MB in  3.01 seconds = 114.20 MB/sec
# 至於, 這數字實際代表意義是啥... 我目前沒概念= =
```



---
## date
```sh
$ date
公曆 20十八年 三月 六日 週二 十一時39分廿四秒

$ date +%Y%m%d
20180306

# 依照時間來命名檔案
$ touch bck_`date +\%H\%M`.sql
$ ls
bck_1608.sql
```

script | desc
------ | ----
%Y     | 年
%m     | 月
%d     | 日
%H     | 時
%M     | 分
%S     | 秒


## 查看 CPU數

```sh
$  grep 'processor' /proc/cpuinfo
processor       : 0
processor       : 1
processor       : 2
processor       : 3
# 我有一顆 4 核心的 CPU
```


## 誰在線上

```sh
$ who
tony     :0           2018-03-01 15:34 (:0)
tony     pts/0        2018-03-02 13:58 (:0)
tony     pts/2        2018-03-02 14:06 (:0)
#誰在線上 (未知)       登入時間          (來源ip)

$ w
 14:45:41 up 1 day, 1 min,  3 users,  load average: 0.08, 0.05, 0.14
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
tony     :0       :0               Thu15   ?xdm?  28:40   0.44s gdm-session-worker [pam/gdm-password]
tony     pts/0    :0               13:58   18:13   2.76s  2.69s top
tony     pts/2    :0               14:06   18:13   0.26s  0.12s bash
# 可以多看使用者停頓時間, 佔用CPU運算資源時間, 正在執行的工作名稱...
```



# chown

```sh
# 10分鐘後關機
$ sudo shutdown -h +10 

# 15分鐘後重新開機
$ sudo shutdown -r +15 

# 點選視窗後,就可以把相關程序殺掉(GUI專用)
$ xkill   

# 使用預設的 15訊號, 讓 terminal結束訊號
$ kill 8888

# 使用系統的 9訊號(KILL訊號), 強制結束(強制關閉 強制終止)
$ kill -9 8888

# 刪除所有 httpd服務
$ killall httpd

# 只顯示軟連結(-R為 recursive)
$ ll -R <path> | grep "\->"

# 搜尋 PATH內的執行檔 (完整檔名)
$ which python
/opt/anaconda3/bin/python

# 搜尋檔案的 fullpath (完整檔名)
$ whereis python
python: /usr/bin/python /usr/bin/python2.7 /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/include/python2.7 /opt/anaconda3/bin/python /opt/anaconda3/bin/python3.6-config /opt/anaconda3/bin/python3.6m /opt/anaconda3/bin/python3.6 /opt/anaconda3/bin/python3.6m-config /usr/share/man/man1/python.1.gz

# 更新檔案系統資料庫 /var/lib/mlocate/mlocate.db
$ sudo updatedb

# 同上, 但採用背景執行
$ sudo updatedb &

# 到 /var/lib/mlocate/mlocate.db 查詢 (片段檔名)
$ locate ifconf # 要查詢的東西, 檔名可以不完整
```

---




# su 這東西
- 2018/07/08
- [換人做做看--sudo 和 su](http://kezeodsnx.pixnet.net/blog/post/25810396-%E6%8F%9B%E4%BA%BA%E5%81%9A%E5%81%9A%E7%9C%8B--sudo-%E5%92%8C-su)

```sh
# 使用 「sudo su」
[tony@tonynb ~]$ sudo su
[sudo] password for tony:   # 輸入 tony 的 admin 密碼~
[root@tonynb tony]# exit
[tony@tonynb ~]$

# 使用 「su」
[tony@tonynb ~]$ su
密碼：                      # 輸入 root 密碼~
[root@tonynb tony]# exit
[tony@tonynb ~]$
```



# sshd (CentOS 7 已內建 && 預設啟動)

```sh
# 產生ssh公私金鑰
$ ssh-keygen -t rsa -b 4096 -C "<id>@<host>"
# -t [rsa|tsa] : 加密演算法
# -b <number> : 加密位元數, 建議都 2048 以上
# -C <xxx> : keygen 名稱
```

1. 安裝sshd
```sh
$ sudo yum -y install openssh-server
$ systemctl start sshd
```

2. 檢查看看(應該要有下面兩個)
```sh
$ ps -e | grep ssh
xxxx ? 00:00:00 sshd
xxxx ? 00:00:00 ssh-agent
# CentOS7 的 圖形話介面, 預設啟用 ssh-agent
```

3. 若出現下列狀況
```sh
$ ssh localhost
ssh: connect to host localhost port 22: Connection refused
# 請先依照第2點的說明查看是否有啟動 ssh-agent 及 sshd 才可以 ssh localhost, 所以只要
$ sudo service sshd restart
$ sudo systemctl enable sshd(這個還不是非常確定是否可行)
```


## 若發現無法啟動, 可能原因如下 (應該不會有 sys-admin這樣作吧?)

1. sshd 被砍了~
2. sshd 被關閉了~
3. 防火牆擋住了~



# SSH 概念說明

每次作 ssh 連線時, 會作 2 件事情 :
1. 建立加密連線通道 (set up the secure encryption for the communication channel)
2. 對 Server 作驗證 (authenticate the server)

> Client 使用 `ssh-keygen` 時, 比較明智的做法是使用 passphrase(密語), 但如此一來, 每每要動到 `private key` 時, 都得輸入 `passphrase`, 相當麻煩, 因此有了 `ssh-agent` 幫忙作代理, 只需要首次使用時, 輸入 passphrase, 日後就不再需要輸入 passphrase 了!

> 客戶端 **每次** ssh 到 Server 時, Server 都會給客戶端它的 `public key`; 客戶端再找出自己的 `~/.ssh/known_hosts` 裏頭該 Server 的 `public key` 來比對看看是否 public key 有改變過, 若改變過(可能客戶端 restart sshd 或者 網路遭到劫持...), 則無法 ssh. [解法: 砍掉該 Server 的 known_hosts 裏頭的 public key, 再重連(假設沒遭到crack入侵的話)] ; 而客戶端會把自己的 `public key` 丟到 Server端的 `~/.ssh/authorized_keys`

> 然而每次 Client ssh 到 Server 都得打密碼太麻煩了, 所以乾脆直接讓 Server 認識 Client 就好了啊!! 因此 Client 可以使用 `ssh-copy-id <remote user id>@<remote host>` 把自己的 `public key` 都給 Server(預設會 Copy `~/.ssh/id_rsa.pub`), 日後 ssh 到 Server 後, Server 會主動將該 Client 的 public key 從 Server 的 `~/.ssh/authorized_keys` 取出來, 去要求 Client 作 公私鑰比對認證,

> `private key : 600` ; `public key : 644`


## ※安全觀點 : sshd 組態 /etc/ssh/sshd_config

組態更改後, 需要 `systemctl restart sshd`

```ini
# PermitRootLogin yes                   # 禁止 ssh root
# PermitRootLogin without-password      # 折衷方案, 禁止 root 使用密碼登入
PermitRootLogin no                      # (預設) 未禁止 ssh root

#PasswordAuthentication yes             # 禁止 使用密碼來作 ssh
PasswordAuthentication yes              # (預設) 未禁止 使用密碼來作 ssh
# ↑ 很重要! 作這之前, 記得先丟 ssh-copy-id 阿~~ 不然登出後就進不來了
```


# 查看誰登入

```sh
# 可看到 誰從哪裡登近來, 然後在幹嘛
$ w
 20:01:47 up  1:19,  2 users,  load average: 0.02, 0.07, 0.12
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
tony     :0       :0               18:43   ?xdm?   1:21   0.21s /usr/libexec/gnome-session-binary --session gnome-c
tony     pts/0    192.168.124.101  18:46    3.00s  0.19s  0.02s w
# TTY : 「:0」 為 圖形化介面
# TTY : 「pts/0」 為 pseudo-terminal 登入
# FROM : 從哪裡來的

```




# 開啟 port並設定防火牆

- 2018/02/19
- [CentOS 7 設定防火牆允許特定 PORT 連線](https://blog.yowko.com/2017/09/centos-7-firewall.html?m=1)

> 語法: `firewall-cmd --zone=public --add-port=3333/tcp --permanent`  對外永久開放 3333 port, 支援 TCP連線

> `firewall-cmd --reload` 重新讀取 firewall設定 
```sh
# 看看 FirewallD是否執行中
$ firewall-cmd --state
running

# 列出目前已設定的 zone
$ firewall-cmd --get-active-zone
public                          # 主機的防火牆設定為「公開場所」
  interfaces: wlp2s0            # 網路介面卡

# 列出 public這個 zone的詳細防火牆資訊
$ firewall-cmd --zone=public --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: wlp2s0
  sources:
  services: dhcpv6-client ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  sourceports:
  icmp-blocks:
  rich rules:

# 所有可選擇的 zones
$ firewall-cmd --get-zones
work drop internal external trusted home dmz public block

# 開啟 port, 可接收外界連線請求
$ firewall-cmd --zone=public --add-port=3333/tcp
success

$ firewall-cmd --zone=public --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: wlp2s0
  sources: 
  services: dhcpv6-client ssh
  ports: 3333/tcp                  # <--- 對外開放了
  protocols: 
  masquerade: no
  forward-ports: 
  sourceports: 
  icmp-blocks: 
  rich rules:
```

#### 防火牆嚴謹度, 由高到低
ser | zone名稱 | desc
--- | -------- | -----
1   | public   | 不信任網域內的所有主機, 只有被允許的連線才能進入
2   | external | 同 public, 但用於 IP偽裝的 NAT環境
3   | dmz      | 主機位於 DMZ區域, 對外部為開放狀態, 對內部網路存取有限制的網路環境, 只有被允許的連線才能進入
4   | work     | 工作場合(信任大多數同網域的主機), 只有被允許的才能連入
5   | home     | 家用場合(信任同網域的主機), 只有被允許的才能連入
6   | internal | 內部網路(信任同網域的主機), 只有被允許的才能連入
7   | trusted  | 允許所有網路連線

#### 有關封包處置的 zone
ser | zone名稱 | desc
--- | -------- | -----
1   | drop     | 丟棄所有 incoming的封包(不回應任何資訊), 只會有 outgoing的連線
2   | block    | 阻擋所有 incoming的封包, 並以 `icmp`回覆對方, 只有從本機發出的連線是被允許的

> 永久套用設定的語法: `firewall-cmd --permanent --zone=dmz --change-interface=ens0s3`
```sh
$ firewall-cmd --get-active-zone
public
  interfaces: wlp2s0

# 指定 zone所使用的網路界面
$ firewall-cmd --zone=home --change-interface=wlp2s0
The interface is under control of NetworkManager, setting zone to 'home'.
success

$ firewall-cmd --reload         # 重新讀取設定檔
$ firewall-cmd --get-active-zone
public
  interfaces: ens0s3 wlp2s0

# 永久改變
$ firewall-cmd --permanent --zone=dmz --change-interface=ens0s3 
```

Service服務在 FirewallD中代表 1~多個 port所組成的一個服務.
(一個 service可包含多個 port或 protocal)

> ex: `ssh服務代表 22/TCP`; `mysql服務代表 3306/TCP`
```sh
# 取得所有已通過防火牆的服務
$ firewall-cmd --get-services
dns docker-registry ftp https mysql smtp ssh telnet ...(略)...
# 這些 services定義在 /usr/lib/firewalld/services/
```

### 允許通過防火牆 FirewallD
> service可過防火牆, 語法: `firewall-cmd --zone=<zone名稱> --add-service=<服務名稱>`

> port可通過防火牆, 語法: `firewall-cmd --zone=<zone名稱> --add-port=<port>/<協定>`
```sh
# 查看 public的防火牆設定
$ firewall-cmd --zone=public --list-all
public (active)
  ...(略)...
  services: dhcpv6-client ssh
  ...(略)...
  
# 防火牆允許 http服務(永久)
$ firewall-cmd --permanent --add-service=http

# ex: 某主機是公司的 DNS Server, 則應在 zone中加入 dns service
$ firewall-cmd --zone=public --add-service=dns
success

$ firewall-cmd --zone=public --list-all
public (active)
  ...(略)...
  services: dhcpv6-client dns ssh           # 多了 dns
  ...(略)...

# 永久允許 3333/tcp通過 public的防火牆
$ firewall-cmd --zone=public --add-port=3333/tcp --permanent
success

$ firewall-cmd --zone=public --list-all
public (active)
  ...(略)...
  ports: 3333/tcp                           # 3333/tcp
  ...(略)...
```



---
## 目前使用者
[Get current user name in bash](https://stackoverflow.com/questions/19306771/get-current-users-username-in-bash)
```sh
$ echo $USER
tonynb

$ whoami
tonynb

$ logname
tonynb

# 查看使用者
$ id
uid=1000(tonynb) gid=1000(tonynb) groups=1000(tonynb),10(wheel),983(docker) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

# 看其他使用者 (只能看到基本資訊)
 id root
uid=0(root) gid=0(root) groups=0(root)

$ 

$ id -u
1000

$ id -u -n
tonynb
```

呼叫目前使用者群組 user group
```sh
$ id -g -n
tonynb
```


---
## source 與 bash
- [鳥哥 - bash 與 source](http://linux.vbird.org/linux_basic/0340bashshell-scripts.php#script_run)

1. 建立一個檔案, 名為 urname.sh, 內容如下 :
```sh
#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

read -p "Your name : " name      # 提示使用者輸入
read -p "Your age :  " age       # 提示使用者輸入
echo -e "Your full name and age : ${name} ${age}" # 結果由螢幕輸出
```

2. 執行看看~
```sh
# 使用 sh 執行
$ echo ${name} ${age}
                                # 因為沒有這個環境變數, 所以啥都沒有, 這很正常
$ sh urname.sh  # 方法一
Your name : tony                     # <--- 輸入
Your age :  30                       # <--- 輸入
Your full name and age : tony 30     # 輸出結果

$ echo ${firstname} ${age}
                                # 一樣是空的哦~~~啥都沒有!! 因為剛剛的執行環境是 子bash

# 使用 source 執行
$ source urname.sh  # 方法二
Your name : tony
Your age :  30
Your full name and age : tony 30

$ echo ${firstname} ${age}
tony 30                         # 東西出現啦~~~~  只要此 terminal沒關, 這環境變數會一直存在
```


---
## 寫 shell script / bash script
範例1
```sh
# 寫 script
$ vi ex1.sh
n1=10
n2=15
test $n1 -eq $n2

$ chmod +x ex1.sh
$ ./ex1.sh
$ echo $?
1
```

範例2
```sh
# 寫 script
$ vi ex2.sh
n1=$1       # 第一個參數
n2=$2       # 第二個參數
echo $n1 -eq $n2

$ chmod +x ex2.sh
$ ./ex2.sh 30 40    # 給參數
$ echo $?
1

$ ./ex2.sh 40 40    # 給參數
$ echo $?
0
```

範例3
```sh
$ vi ex3.sh
n1=$1
n2=$2
if test $n1 -gt $n2   # if 參數1 > 參數2 
  then
    echo "n1:$n1 is bigger than n2:$n2"
  else
    echo "n1:$n1 is not bigger than n2:$n2"
fi

$ chmod +x ex3.sh
$ ./ex3.sh 30 40
n1:30 is not bigger than n2:40
```

範例4
```sh
$ vi ex4.sh
for n in `seq 1 3`  # 重音符號「``」內, 優先執行
do
  echo $n
done
# (後略)
```

範例5
```sh
$ vi ex5.sh
for n in `ls`
do
  echo $n
done
# (後略)
```


## 其他不知道怎嚜分類

> `/proc`內部幾乎都是虛擬檔案(唯獨), 少數系統設定值可修改
```sh
$ cat /proc/sys/kernel/hostname
localhost.localdomain

$ echo "tonynb" > /proc/sys/kernel/hostname     # 要進到 su才可, 無法 sudo
# 此檔案權限為 -rw-r--r--. 1 root root 0
# 更改主機名稱就會變成 tonynb
```

### less 與 more
```sh
$ ll /dev | more
# more只能往下頁

$ ll /dev | less
# less可搜尋, 到第幾行, 往上頁, 往下頁 
```
> 語法: `less <options> <file>`

options | description
------- | --------------
-m      | 顯示類似 more的百分比
-N      | 顯示 line number
/\<str> | 搜尋特定文字(向下找)
n       | 使用 / 後, 向下找
N       | 使用 / 後, 向上找
h       | 顯示 help介面       


### 計數(word count) - wc

```sh
# wc -[lwc] <file>  Line, Word, Character
$ wc .bashrc
118  520 3809 .bashrc
# 檔案內有 118行, 520個字節數, 3809 Byte Counts
```

### 取代/刪除字元 - tr
```sh
$ echo "ABCDEFG"
ABCDEFG

$ echo "ABCDEFG" | tr ABC xyz
xyzDEFG

$ echo "ABCDEFG" | tr [:upper:] [:lower:]
abcdefg

$ echo "ABC" | tr -d 'A'
BC
```

### 跨主機複製 - scp
> 語法1: `scp <要複製的檔案> <要放置的id>@<要放置的host>:<放在哪邊>`<br>
  語法2: `scp <要複製的來源id>@<來源host>:<檔案絕對路徑> <放置位置>`
```sh
$ scp requirement.txt tony@192.168.124.81:/home/tony/tmp
# 把 requirement.txt 丟到 tony@192.168.124.81的 /home/tony/tmp裏頭

$ scp tony@192.168.124.81:/home/tony/tmp/requirement.txt .
# 把 tony@192.168.124.81 內的 /home/tony/tmp/requirement.txt 複製到目前目錄底下
```

### 產生序列數字 - seq
```sh
$ seq 1 2 7
1
3
5
7

# 補上「0」讓它們等寬
$ seq -w 1 2 7
01
03
05
07
```

### 排序 - sort
```sh
$ cat doc1
031
2
1345
001

# 預設逐字依照 ascii排序
$ sort doc1
001
031
1345
2

# -g: 嘗試以數字排序
$ sort -g doc1
001
2
031
1345
```

### 過濾重複 - uniq
> 將檔案中, `相鄰且重複`的多行資料, 取 set, 確保唯一 <br>
> 搭配 `sort`, 語法: `sort <檔案> | uniq`


### 擷取子字串 - cut
> 預設處理以「tab分隔」的檔案, 用 `-d` 指定分隔符號, `-f` 指定要取出的欄位
```sh
$ cat doc2
tom,22,31000
jack,21,29500
eric,18,42000

$ cut -d',' -f2 doc2
22
21
18
```


### 主機名稱 - hostname
> 設定主機名稱, 重新登入後開始生效, 語法: `set-hostname <新的 hostname名稱>`
```sh
$ hostname
tony

$ hostnamectl

```

### 別名 - alias
> 底下的設定, 登出後就無效了, 因此可將別名設到 `.bashrc` 或 `/etc/profile(不建議)` 之中.
```sh
$ alias
alias ll='ls -alF'
alias ls='ls --color=auto'
...(很多別名)...

$ alias dv='du -sh /var'
# 自行設定別名

$ unalias dv
# 刪除別名
```

### echo
```sh
$ echo "L1\nL2\nL3"
L1\nL2\nL3

# 讓特殊字元作用
$ echo -e "L1\nL2\nL3"
L1
L2
L3
```

### 互動式 input - read
```sh
$ read n
88   # 自行輸入

$ echo $n
88
```

### ls
[ls查看目錄內容](http://blog.xuite.net/altohorn/linux/17259902-ls+%E5%88%97%E5%87%BA%E7%9B%AE%E9%8C%84%E5%85%A7%E5%AE%B9)
> 語法: `ls [options] <檔案or資料夾>`

```sh
$ ls -i     # 列出 inode
$ ls -s     # 列出檔案大小
$ ls -R     # Recursive (遞回列出)
$ ls -r     # 反向排序
$ ls -h     # 檔案內容以 KB, MB, GB顯示
$ ls -d     # 只顯示 directory
$ ls -t     # 依時間排序
$ ls -S     # 依檔案大小排序
$ ls -F     # 附加資料結構, *: 可執行檔; /: 目錄; =: socket檔案; |: FIFO檔案;
$ ls -n     # 列出 UID 及 GID

$ ls -l     # 詳細資訊
drwxr-xr-x. 2 tony tony     6  5月 30 17:58 desktop
...(略)...

# 第 1 個字
# - : 檔案
# d : 目錄
# l : 連結
# b : 區塊類(硬碟, 光碟機, 週邊設備)
# c : 字元類(序列埠, 終端機, 磁帶, 印表機)

$ ls --full-time  # 列出 詳細時間
$ ls --time={atime, ctime}  # 列出 {access時間 , 改變權限屬性時間 }
```


### 追蹤 - tail (動態log)
> 語法: `tail -f <追蹤的 log路徑>`
```sh
# 顯示最後5行, 並持續監看 (追蹤log)
$ tail -n 5 -f /var/log/messages
```


## 好用的資料處理工具(分欄位) - awk
> 語法: `awk '條件1{動作1} 條件2{動作2} ...' <filename>`; 欄位分隔符號預設為「空白鍵」or「tab鍵」

```sh
$ last -n 5
tony     pts/10       192.168.124.94   Mon Apr  9 20:59   still logged in
tony     pts/11       192.168.124.88   Mon Apr  9 20:11 - 20:12  (00:01)
tony     pts/10       192.168.124.94   Mon Apr  9 19:37 - 20:51  (01:14)
tony     pts/9        192.168.124.94   Mon Apr  9 17:02   still logged in
tony     pts/9        192.168.124.94   Mon Apr  9 10:35 - 16:58  (06:23)

$ last -n 5 | awk '{print $1 "\t" $3}'
tony    192.168.124.94
tony    192.168.124.88
tony    192.168.124.94
tony    192.168.124.94
tony    192.168.124.94
```


### ncftpget ncftpput

```sh
ncftpput -u <帳號> -p <密碼> <host>:~/ upload <標的檔案>
```


### substring
```sh
$ a='12345678'
$ echo ${a:2:3}
345
```


### 測試 - test
> 測試, 語法: `test <option> <filename>`<br>
```sh
$ touch file1

$ test -d file1 # 是否為 dir
$ echo $?
1

$ test -e file1 # 是否存在
$ echo $?
0

$ test -r file1 # readable
$ echo $?
0
```
option         | description
-------------- | -------------
file           | 
  -d           | 為 dir
  -e           | 存在
  -s           | 大小 >0
  -r           | readable
  -w           | writable
  -x           | executable
  -L           | 為連結
string         | 
-n \<str>      | 長度 >0
-z \<str>      | 是否 =0
\<str>==\<str> | 字串相等
\<str>!=\<str> | 字串不相等
number         | 
n1 -eq n2      | n1 == n2
-ne, -gt, ...  | (略)




# Locale - Linux語系編碼

```sh
$ locale
LANG=zh_TW.UTF-8    # 原本的語系 zh_TW.UTF-8
LC_CTYPE="zh_TW.UTF-8"      # 字元的編碼
LC_NUMERIC="zh_TW.UTF-8"    # 數字格式
LC_TIME="zh_TW.UTF-8"       # 時間格式
LC_COLLATE="zh_TW.UTF-8"    # (定序)文字如何比較(為了排序)
LC_MONETARY="zh_TW.UTF-8"   # 貨幣格式
LC_MESSAGES="zh_TW.UTF-8"   # 訊息顯示的格式(ex: 錯誤訊息)
LC_PAPER="zh_TW.UTF-8"
LC_NAME="zh_TW.UTF-8"
LC_ADDRESS="zh_TW.UTF-8"
LC_TELEPHONE="zh_TW.UTF-8"
LC_MEASUREMENT="zh_TW.UTF-8"
LC_IDENTIFICATION="zh_TW.UTF-8"
LC_ALL=

# 改變語系吧
$ LANG=en_US.utf8
$ export LANG=${LANG}
$ locale
LANG=en_US.utf8     # 底下一切都變了 en_US.utf8
LC_CTYPE="en_US.utf8"   
LC_NUMERIC="en_US.utf8"
LC_TIME="en_US.utf8"
LC_COLLATE="en_US.utf8"
LC_MONETARY="en_US.utf8"
LC_MESSAGES="en_US.utf8"
LC_PAPER="en_US.utf8"
LC_NAME="en_US.utf8"
LC_ADDRESS="en_US.utf8"
LC_TELEPHONE="en_US.utf8"
LC_MEASUREMENT="en_US.utf8"
LC_IDENTIFICATION="en_US.utf8"
LC_ALL=

# locale -a 可以查看 Linux 支援了多少語系
$ locale -a | wc
    789     789    8231     # 支援了 789 個語系...

# zh_TW.big5 : 大五碼的中文編碼
# zh_TW.utf8 : 萬國碼的中文編碼
```


```sh
# 取得檔名
$ basename /etc/nginx/nginx.conf
nginx.conf

# 取得目錄名
$ dirname /etc/nginx/nginx.conf
/etc/nginx

# 列出內容(包含行號)
$ nl /etc/nginx/nginx.conf
     1  user  nginx;
     2  worker_processes  1;
...(略)...

# 列出檔案內容(用來查看二進制檔案)
$ sudo od /usr/bin/passwd

$ 
```


```sh
# umask : 讓目前使用者 建立 檔案 or 目錄 時的權限設定值
# 預設上, 檔案 最多應為 666
# 預設上, 目錄 最多可為 777
# umask 的分數指 該預設值需要檢調的權限!! 
# 適用情境: 不同使用者, 要各自登入 linux, 要共同合作開發某資料夾下的專案, 可先改好 umask後, 便可方便將來合作


$ umask   # 用來清除對應的權限
0002    # 第 1 碼為特殊用途; 後面分別為 user, group, other

$ umask -S    # 以符號類型的方式, 顯示(如上例, umask 0002)
u=rwx,g=rwx,o=rx
```



# 觀察檔案類型: file

```sh
# 一般 ASCII 文檔
$ file /etc/passwd
/etc/passwd: ASCII text

# 二進位編碼過後的執行檔
$ file /usr/bin/passwd
/usr/bin/passwd: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, BuildID[sha1]=1e5735bf7b317e60bcb907f1989951f6abd50e8d, stripped

# data檔
$ sudo file /var/lib/mlocate/mlocate.db
/var/lib/mlocate/mlocate.db: data
```



# 檢查檔案細項屬性

```sh
# 不知道怎麼解釋 =口=...
$ stat /etc/passwd
  File: ‘/etc/passwd’
  Size: 2541        Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d    Inode: 201385622   Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Context: system_u:object_r:passwd_file_t:s0
Access: 2018-07-23 09:01:28.195275508 +0800
Modify: 2018-07-20 16:11:33.755081384 +0800
Change: 2018-07-20 16:11:33.818081653 +0800
 Birth: -

$ stat /bin/passwd
  File: ‘/bin/passwd’
  Size: 27832       Blocks: 56         IO Block: 4096   regular file
Device: fd00h/64768d    Inode: 201780015   Links: 1
Access: (4755/-rwsr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Context: system_u:object_r:passwd_exec_t:s0
Access: 2018-07-23 21:37:58.500276830 +0800
Modify: 2014-06-10 14:27:56.000000000 +0800
Change: 2018-02-27 13:54:29.234444218 +0800
 Birth: -
```



# 光碟寫入工具
- 光碟製作成 iso 鳥哥`mkisofs`
- 燒光碟 鳥哥`cdrecord`



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


# 網路 verify
$ ip link show
$ ip addr show
$ ip route show
$ cat /etc/resolv.conf
$ ss

# 網路 Test
$ traceroute  # 追蹤 route
$ tracepath   # 追蹤 route
$ nslookup
```

```sh
# CentOS7 rpm 檢核用的 public key
$ ll /etc/pki/rpm-gpg/
```