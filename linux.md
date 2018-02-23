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

2. 如何解決
```

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

> 若出現 `Permission denyed`, 則要改變執行者對此檔案的權限
```sh
$ ll
-rw-rw-r--. 1 ...(略)... pp.py

$ chmod u+x pp.py
$ ll
drwxrwxr-x. 1 ...(略)... pp.py
```

> windows系統下, 若要使用同 shebang的功能, 再去google `cygwin`.



## - chown
```sh
改變檔案的擁有者
$ sudo chown <owner>:<group> <fileName>

改變資料夾的擁有者(及裡頭的東西)
$ sudo chown -R <owner>:<group> <dirName>
```

## -chmod

```sh
讓 pp.py可以被擁有者執行
$ chmod u+x pp.py
```

## -shutdown
```sh
$ sudo shutdown -h +10 # 10分鐘後關機

$ sudo shutdown -r +15 # 15分鐘後重新開機
```

---
## - ps相關指令
```sh
僅列出與自己相關的bash相關程序
$ ps
  PID TTY          TIME CMD
 9342 pts/2    00:00:00 bash
11937 pts/2    00:00:00 ps

列出詳細資訊
$ ps -l
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000  9342  7534  0  80   0 - 29176 wait   pts/2    00:00:00 bash
0 R  1000 11944  9342  0  80   0 - 37232 -      pts/2    00:00:00 ps

列出所有系統運作的程序
$ ps aux
（超多～～～）
```


---
## - top(類似Windows的工作管理員)
[參考自鳥哥](http://linux.vbird.org/linux_basic/0440processcontrol/0440processcontrol-fc4.php#top)

內容大致如下（上半部：系統資訊,下半部：Process資訊)
<img src="img/top.jpg" style="width:480px; height:320px;" />

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
## - kill 殺程序
```
點選視窗後,就可以把相關程序殺掉
$ xkill   

殺掉8888的程序
$ kill 8888
```

---
## - 壓縮/解壓縮

1. zip

```
將a1, a2, a3壓縮為FF.zip, 並設定密碼
$ zip -er FF.zip a1 a2 a3
(下一行再輸入密碼)

把QQ.zip裡面的檔案全部解壓縮出來
$ unzip QQ.zip

把QQ.zip(解壓縮密碼為1234)解壓縮
$ unzip -P QQ.zip
(下一行在輸入密碼)
```

2. (待續)

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
	firewall-cmd --zone=dmz --add-port=3333/tcp
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

## 目前使用者
[Get current user name in bash]https://stackoverflow.com/questions/19306771/get-current-users-username-in-bash
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

## ls的妙用
```sh
$ ls

$ ls -l   # 等同於 ll

$ ls -a   # 包含顯示隱藏的檔案

$ ls -R   # recursively顯示

$ ls | ^l # 只顯示軟連結
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