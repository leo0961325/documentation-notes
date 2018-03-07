# Linux
- 相關指令
- 知識概念備註


---
## EPEL (非常重要阿~~~)
> [What is EPEL](https://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/)

Extra Packages for Enterprise Linux

Linux在安裝許多軟體的時候(ex: yum install ...), 會有軟體相依性的問題, 若發現相依軟體尚未被安裝, yum會自己去`本地 repository`裡頭找有記載的`遠端 repository`去下載相依套件. 而 EPEL就是專門 for CentOS的套件庫, 裡頭有許多CentOS的核心套件.



---



## Linux的軟體管理員

### rpm vs dpkg
distribution 代表 | 軟體管理機制 | 使用指令 | 線上升級機制(指令)
--- | --- | --- | ---
Red Hat/Fedora | RPM | rpm, rpmbuild | YUM (yum)
Debian/Ubuntu | DPKG | dpkg | APT (apt-get)


### rpm vs srpm
檔案格式 | 檔名格式 | 直接安裝與否 | 內含程式類型 | 可否修改參數並編譯
--- | --- | --- | --- | ---
RPM | xxx.rpm | 可 | 已編譯 | 不可
SRPM | xxx.src.rpm | 不可 | 未編譯之原始碼 | 可

### 指令差異
指令 | 說明
--- | ---
-Uvh | 後面接的軟體即使沒有安裝過，則系統將予以直接安裝；<br />若後面接的軟體有安裝過舊版，則系統自動更新至新版；
-Fvh | 如果後面接的軟體並未安裝到你的 Linux 系統上，則該軟體不會被安裝；<br />亦即只有已安裝至你 Linux 系統內的軟體會被『升級』！

```
$ rpm -ivh xxx.rpm
-i ：install 的意思
-v ：察看更細部的安裝資訊畫面
-h ：以安裝資訊列顯示安裝進度
```

---
## 主要目錄


```sh
/bin/      # 可執行檔
/sbin/     # 系統管理員 用的 工具or指令or執行檔. ex: ifconfig, mke2fs
/usr/      # Linux系統安裝過程中必要的 packages
    bin/            # 一般使用者 用的 工具or指令or執行檔
    sbin/           # 系統管理員 用的 工具or指令or執行檔
    src/
        linux/                # 系統核心原始碼
    share/                
        doc/                  # 系統文件
        man/                  # 線上操作手冊
        zoneinfo              # 時區檔案
/etc/      # 系統設定檔. ex: inittab, resolv.conf, fstab, rc.d
    localtime/      # 系統時間
/boot/     # 開機時使用的核心檔案目錄.
/lib/      # 系統的共用函式庫檔案
/opt/      # 非 Linux預設安裝的外來軟體
/var/      # 變動行 & 系統待排隊處例的檔案
    log/            # 紀錄檔
        dmesg                 # 開機時偵測硬體與啟動服務的紀錄
        messages              # 開機紀錄
        secure                # 安全紀錄
    db/           
        mysql/                # mysql檔案
    spool/            
        mail/                 # 等待寄出的 email
/tmp/      # 重開機後會清除
/proc/     # 行程資訊目錄, 
/media/    # 移動式磁碟or光碟 掛載目錄
/mnt/      # 暫時性檔案系統 掛載目錄
/dev/      # 系統設備目錄
    hda/            # IDE硬碟
    sd1/            # SCSI硬碟
    cdrom/          # 光碟機
    fd0/            # 軟碟機
    lp0/            # 印表機
```


---
## 檔案詳細資訊

type | desc
--- | ---
- | 檔案
d | 目錄
l | 連結
b | 區塊類(硬碟, 光碟機, 週邊設備)
c | 字元類(序列埠, 終端機, 磁帶, 印表機)


---
## 解除yum lock

1. 底下這邊不是程式碼, 是說明情境
```
$ sudo yum install -y mongodb-org
Loaded plugins: fastestmirror, langpacks
Existing lock /var/run/yum.pid: another copy is running as pid 7629.
Another app is currently holding the yum lock; waiting for it to exit...
  The other application is: PackageKit
    Memory : 300 M RSS (1.7 GB VSZ)
    Started: Sun Nov 26 13:05:36 2017 - 00:19 ago
    State  : Running, pid: 7629
Another app is currently holding the yum lock; waiting for it to exit...
  The other application is: PackageKit
    Memory : 353 M RSS (1.7 GB VSZ)
    Started: Sun Nov 26 13:05:36 2017 - 00:21 ago
    State  : Running, pid: 7629
...
```

2. 如何解決 - 找出 pid, 砍掉
```
$ ps aux | grep yum
```


## tail 追蹤
> 語法: `tail -n <int> <追蹤的 log路徑>`
```sh
# 顯示最後5行, 並持續監看
$ tail -n 5 -f /var/log/messages
```

---
## - 設定terminal的熱鍵
```
畫面右上角功能表 > 設定 > 鍵盤 > 快捷鍵 > 自訂捷徑列 > +
Name: Terminal Shortcut
Command: gnome-terminal
再點選所要設定的熱鍵
```

## - shebang on Linux
[run python script directly from command line](https://stackoverflow.com/questions/20318158/run-python-script-directly-from-command-line)
> Linux系統底下, 可在任何.py檔的第一行使用 `#!/usr/bin/python` ( 依照使用的 python位置而定 ), 執行此腳本時, 可以藉由下列方式來執行.
```sh
$ python pp.py
$ ./pp.py
```


---
## rwx 權限
> 若出現 `Permission denyed`, 則要改變執行者對此檔案的權限
```sh
$ ll
-rw-rw-r--. 1 ...(略)... pp.py

$ chmod u+x pp.py
$ ll
drwxrwxr-x. 1 ...(略)... pp.py
```

> windows系統下, 若要使用同 shebang的功能, 再去google `cygwin`.



## shell內

hotkey | description
------ | -----------
Ctrl+C | 中斷目前工作
Ctrl+D | 送出eof or 輸入結束特殊字元
Ctrl+Z | 暫停目前工作, 利用 `fg`指令, 可以取得暫停的工作



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

## 軟連結 soft link
> 語法: `ln -s <目標對象> <連結名稱>`
```sh
$ ln -s /opt/anaconda3/bin/python3 ~/py

$ ll | grep py
lrwxrwxrwx. 1 root root   26  3月  2 14:10 py -> /opt/anaconda3/bin/python3
```

## 硬碟空間
```sh
# 查看系統盛多少容量( -h表以KB, MB, GB表示)
$ df -h
檔案系統             容量  已用  可用 已用% 掛載點
/dev/mapper/cl-root   80G  8.2G   72G   11% /
devtmpfs             1.8G     0  1.8G    0% /dev
tmpfs                1.9G   13M  1.8G    1% /dev/shm
tmpfs                1.9G  9.1M  1.8G    1% /run
tmpfs                1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1           1014M  175M  840M   18% /boot
/dev/mapper/cl-home   80G  1.3G   79G    2% /home
/dev/mapper/cl-var    50G  604M   50G    2% /var
tmpfs                370M   12K  370M    1% /run/user/1000

# 可看目標目錄(recursive)的已用空間
$ du -h ~/doc/illu | more
0	/home/tony/doc/illu/.git/branches
44K	/home/tony/doc/illu/.git/hooks
4.0K	/home/tony/doc/illu/.git/info
4.0K	/home/tony/doc/illu/.git/refs/heads
0	/home/tony/doc/illu/.git/refs/tags
4.0K	/home/tony/doc/illu/.git/refs/remotes/origin
...
```


```sh
$ ls -l /dev | more
# more只能往下頁

$ ls -l /dev | less
# less可搜尋, 到第幾行, 往上頁, 往下頁 
```



```sh
# 改變檔案的擁有者
$ sudo chown <owner>:<group> <fileName>

# 改變資料夾的擁有者(及裡頭的東西)
$ sudo chown -R <owner>:<group> <dirName>

# 讓 pp.py可以被擁有者執行
$ chmod u+x pp.py

# 10分鐘後關機
$ sudo shutdown -h +10 

# 15分鐘後重新開機
$ sudo shutdown -r +15 

# 點選視窗後,就可以把相關程序殺掉(GUI專用)
$ xkill   

# 使用預設的 15訊號, 讓 terminal結束訊號
$ kill 8888

# 使用系統的 9訊號(KILL訊號), 強制結束
$ kill -9 8888

# 刪除所有 httpd服務
$ killall httpd

# 只顯示軟連結(-R為 recursive)
$ ls -R <path> | grep "\->"

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
## - 行程狀態 相關指令
```sh
# 僅列出與自己相關的bash相關程序
$ ps
  PID TTY          TIME CMD
 9342 pts/2    00:00:00 bash
11937 pts/2    00:00:00 ps

# 詳細資訊
$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
tony     24634 24626  0 13:58 pts/0    00:00:00 bash
tony     32620 24634  0 20:58 pts/0    00:00:00 ps -f

# 更多詳細資訊
$ ps -l
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000  9342  7534  0  80   0 - 29176 wait   pts/2    00:00:00 bash
0 R  1000 11944  9342  0  80   0 - 37232 -      pts/2    00:00:00 ps
# PPID: Parent Process ID

# 列出系統運作的程序
$ ps aux | grep mysqld
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
tony       919  0.0  0.0 112668   964 pts/0    S+   21:36   0:00 grep --color=auto mysqld
mysql     2941  0.1  4.9 1248528 186788 ?      Sl    3月01   1:52 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid
#           重點
# USER      Y       Process Owner
# PID       Y       Process ID
# %CPU              CUP usage %
# %MEM              Memory usage %
# VSZ               虛擬Memory usage (KB)
# RSS               固定佔用的Memory (KB)
# TTY               Process is from which Terminal(若為系統服務, 則為 ?)
# STAT              Process目前狀態. S:休眠中; R:執行中
# START             Process被啟動的日期
# TIME              實際使用CPU時間
# COMMAND   Y       Process的命令

# 樹狀結構列出 System Procss
$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager───2*[{NetworkManager}]
        ├─2*[abrt-watch-log]
        ├─abrtd
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─alsactl
        ...(略)

# 背景睡覺 60秒
$ sleep 60 &        # sleep 60 seconds
$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
tony      1559 24634  0 21:59 pts/0    00:00:00 sleep 60
tony      1563 24634  0 21:59 pts/0    00:00:00 ps -f
tony     24634 24626  0 13:58 pts/0    00:00:00 bash

# 前景作業改背景作業, 使用 Ctrl+z中斷, 再用 bg指令, 將上一個被停止的行程放入背景中執行.
$ sleep 60
^Z
[1]+  Stopped                 sleep 60
$ bg
[1]+ sleep 60 &
$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
tony      1713  1705  0 22:01 pts/2    00:00:00 bash
tony      1763  1713  0 22:01 pts/2    00:00:00 sleep 60
tony      1770  1713  0 22:02 pts/2    00:00:00 ps -f

# 將背景取回前景 fg
$ jobs
$ sleep 50 &
[1] 2138
$ sleep 40 &
[2] 2142
$ sleep 30 &
[3] 2146
$ jobs
[1]   Running                 sleep 50 &
[2]-  Running                 sleep 40 &
[3]+  Running                 sleep 30 &
$ fg 2          # 取出第二個背景行程
sleep 40
^C              # 中斷

# nice value NI value, 行程優先權(priority)
$ ps l
F   UID   PID  PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND
0  1000  1959  1951  20   0 116568  3232 wait   Ss   pts/0      0:00 bash
0  1000  2198  1959  20   0 148936  1452 -      R+   pts/0      0:00 ps l
0  1000 24277 24261  20   0 116560  3224 n_tty_ Ss+  pts/1      0:00 /bin/bash
# NI為 [-20, 19], 越小越優先, 預設為 0
```


---
## - top(類似Windows的工作管理員)
[參考自鳥哥](http://linux.vbird.org/linux_basic/0440processcontrol/0440processcontrol-fc4.php#top)

內容大致如下（上半部：Resource資訊,下半部：Process資訊)
<img src="img/top.jpg" style="width:480px; height:320px;" />

```
# 第一行
top - 14:53:56                                  目前時間
up 3:47                                         累積開機時間
load average: 0.84, 0.82, 0.70                  系統每 1, 5, 15分鐘平均執行的行程數
```

| top後操作指令 | 說明 |
| --- | --- |
| h | Help |
| P | 依據CPU使用時間排序 |
| M | 依據記憶體使用量排序 |
| T | 依據執行時間排序 |
| N | 依據PID大小排序 |
| u | 只列出該帳號的程序 |
| k | 刪除 |
| d | 更新秒數 |
| q | 離開 |



---
## - CentOS7服務相關指令
```
啟動與關閉<service>
$ systemctl start <service>
$ systemctl stop <service>
$ systemctl restart <service>

重新開機後生效<service>
$ systemctl enable <service>
$ systemctl disable <service>

(以上看狀況加sudo)
```

---

---
## - 壓縮/解壓縮

- gzip
```sh
$ touch aa
$ ll
aa

# 使用 gzip壓縮(取代原始檔案)
$ gzip aa
$ ll
aa.gz

# 使用 gunzip解壓縮(取代原始檔案)
$ gunzip aa.gz
$ ll
aa
```

- zip
Case1
```sh
$ ll
aa

# 使用 zip壓縮
$ zip -r qq.zip aa
  adding: aa (stored 0%)

$ ll
aa  qq.zip

$ rm aa
$ unzip qq.zip
Archive:  qq.zip
 extracting: aa     

$ ls
aa  qq.zip
```

Case2
```sh
# 將a1, a2, a3壓縮為FF.zip, 並設定密碼
$ zip -er FF.zip a1 a2 a3
# (下一行再輸入密碼)

# 把QQ.zip裡面的檔案全部解壓縮出來
$ unzip QQ.zip

# 把QQ.zip(解壓縮密碼為1234)解壓縮
$ unzip -P QQ.zip
# (下一行在輸入密碼)
```

- tar
> 把多的檔案包成一包, 方便 gzip壓縮, 語法: `tar -<選項> <檔名> <要打包的東西>`

> `-c 產生新的包裹檔案` <br> `-v 觀看指令進度` <br> `-f 指定包裹檔案的名稱` <br> `-x 解開已打包的檔案` (解壓縮的概念)
```sh
$ ls 
a  b  c

$ tar -cvf qq.tar a b c
a
b
c

$ rm a b c
$ ls
qq.tar
```

- tgz (tar ball)
> tar + gz的合體, 語法: `tar -<選項> <tar ball檔名> <要打包的東西們> ...`
```sh
$ ls
a  b  c
$ tar -czvf qq.tgz a b c
a
b
c

$ ls
a  b  c  qq.tgz
```

---
## find相關

[參考自網路blog](https://blog.gtwang.org/linux/unix-linux-find-command-examples/)

```
在目前dir底下,忽略大小寫找出所有xx.txt
$ find . -iname xx.txt

-perm:尋找特定權限的檔案
$ find . -type f ! -perm 777

列出唯獨的檔案
$ find . -perm /u=r

列出可執行的檔案
$ find . -perm /a=x
```

```$ find . -type <代碼> -name xx```
| <代碼> | 說明 |
| --- | --- |
| d | 目錄 |
| p | 具名的pipe(FIFO) |
| f | 一般檔案 |
| l | 連結檔 |
| s | socket檔案 |



---
## sshd無法啟動的原因
1. sshd未安裝
2. sshd未啟動
3. 防火牆

1. 安裝sshd
```
$ sudo yum -y install openssh-server
$ service sshd restart
```

2. 檢查看看(應該要有下面兩個)
```
$ ps -e | grep ssh
xxxx ? 00:00:00 ssh-agent
xxxx ? 00:00:00 sshd
```

3. 若出現下列狀況
```
$ ssh localhost
ssh: connect to host localhost port 22: Connection refused
請先依照第2點的說明查看是否有啟動ssh-agent及sshd才可以ssh localhost,
所以只要
$ service sshd restart
$ systemctl enable sshd(這個還不是非常確定是否可行)
```

---

## 建立使用者

> 指令: `adduser <userName>`

```sh
$ adduser tony
# 然後就開始輸入密碼那堆東西~

$ groups tony
tony : tony 

$ sudo usermod -aG sudo tony
# 把使用者加入 root群組

$ groups tony
tony : tony sudo
```


---

## 開啟 port並設定防火牆
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

$ id
uid=1000(tonynb) gid=1000(tonynb) groups=1000(tonynb),10(wheel),983(docker) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

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
## 虛擬檔案
> `/proc`內的檔案, 都是虛擬檔案, 是系統讓使用者查看系統內部狀況的窗口

```sh
# 查看記憶體使用情形
$ cat /proc/meminfo

# 查看檔案分割資訊
$ cat /proc/partitions

# 查看 CPU資訊
$ cat /proc/cpuinfo
```

---

## 其他不知道怎嚜分類
> 系統排程服務`crond`, 每分鐘會檢查 `/etc/crontab`, 並在適當時機執行檔案內指令的排程工作

> `/proc`內部幾乎都是虛擬檔案(唯獨), 少數系統設定值可修改
```sh
$ cat /proc/sys/kernel/hostname
localhost.localdomain

$ echo "tonynb" > /proc/sys/kernel/hostname     # 要進到 su才可, 無法 sudo
# 此檔案權限為 -rw-r--r--. 1 root root 0
# 更改主機名稱就會變成 tonynb
```
