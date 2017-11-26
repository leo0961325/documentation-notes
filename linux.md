# Linux
- 相關指令
- 知識概念備註


---
## EPEL
> [What is EPEL](https://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/)

Extra Packages for Enterprise Linux

Linux在安裝許多軟體的時候(ex: yum), 會有軟體相依行的問題, 若發現相依軟體尚未被安裝, yum會自己去 repository裡頭有記載遠端 repo去下載, 而 EPEL就是專門 for CentOS的套件庫, 裡頭有許多CentOS的核心套件.



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

## - chown
```sh
改變檔案的擁有者
$ sudo chown <owner>:<group> <fileName>

改變資料夾的擁有者(及裡頭的東西)
$ sudo chown -R <owner>:<group> <dirName>
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
| h	| Help |
| P	| 依據CPU使用時間排序 |
| M	| 依據記憶體使用量排序 |
| T	| 依據執行時間排序 |
| N	| 依據PID大小排序 |
| u	| 只列出該帳號的程序 |
| k	| 刪除 |
| d	| 更新秒數 |
| q	| 離開 |



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
最近更新日期 2017/09/23, by TonyCJ
