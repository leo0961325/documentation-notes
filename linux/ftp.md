# [遠端連線伺服器SSH / XDMCP / VNC / RDP](http://linux.vbird.org/linux_server/0310telnetssh.php#ssh_client)

## 模擬 FTP 的檔案傳輸方式： sftp
> ssh用來**登入遠端Server**進行後續操作, 但如果只是想**上傳/下載**資料, 則使用 `sftp` 或 `scp`. 此兩個指令, 也是透過 22port, 只是他們模擬成FTP與複製的動作而已.


put/get               | Description
--------------------- | -----------------------------------
put files to   remote | put <本機目錄或檔案> <遠端位置>
get files from remote | get <遠端主機目錄或檔案> <本機位置> 


```sh
# 登入遠端
# $ sftp <id>@<host>
$ sftp bis@192.168.124.80
Connection to <host>...
# 輸入密碼後即可登入

sftp> # (類似 ssh進去遠端, 開始進行操作)
```

基本操作基本上都跟 Linux指令差不多, 但登入遠端後, 針對 host端的操作行為, 加上`L` or `l`即可.
```sh
$ ls
localdir

$ sftp bis@192.168.124.80
bis@192.168.124.80''s password:
Connected to 192.168.124.80.

$ sftp> ls
home      mysqlbck
```

----------------------------------------

## 使用 sftp登入後, 再互動式上傳
```sh
sftp <id>@<host>
put <file>
```


## 使用 scp上傳(但要手動打密碼)
```sh
scp <file> <id>@<host>
```


## 使用強大的 ncftp上傳
> sudo yum install ncftp

> sudo apt-get install ncftp
#### 1. 互動式上傳
```sh
ncftp -u <id> -p <passwd> <host>
put <file>
```

#### 2. 一口氣上傳(腳本)
```sh
ncftpput -u <id> -p <passwd> <host> <target folder> <file>
```