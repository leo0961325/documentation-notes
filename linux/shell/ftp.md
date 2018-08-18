# [遠端連線伺服器SSH / XDMCP / VNC / RDP](http://linux.vbird.org/linux_server/0310telnetssh.php#ssh_client)

## 模擬 FTP 的檔案傳輸方式： sftp

ssh用來**登入遠端Server**進行後續操作, 但如果只是想**上傳/下載**資料, 則使用 `sftp` 或 `scp`. 此兩個指令, 也是透過 22port, 只是他們模擬成FTP與複製的動作而已.

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

基本操作基本上都跟 Linux指令差不多, 但登入遠端後, 針對 host端的操作行為, 加上 `L` or `l` 即可.

```sh
$ ls
localdir

$ sftp bis@192.168.124.80
bis@192.168.124.80''s password:
Connected to 192.168.124.80.

$ sftp> ls
home      mysqlbck
```


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

```sh
$ sudo yum install ncftp

$ sudo apt-get install ncftp
```


#### 1. 互動式上傳

```sh
ncftp -u <id> -p <passwd> <host>
put <file>
```


#### 2. 一口氣上傳(腳本)

```sh
ncftpput -u <id> -p <passwd> <host> <target folder> <file>
```



# 跨站複製

1. [sftp](http://linux.vbird.org/linux_server/0310telnetssh.php#sftp)

```sh 
# 完成備份 - sftp指令不能帶密碼, 無法自動化!
$ sftp swrd@192.168.124.80
$ cd /bck
$ put 20180413_1730.tar.gz
```


2. [scp](http://linux.vbird.org/linux_server/0310telnetssh.php#scp)

```sh
# 完成備份 - scp無法帶密碼, 無法自動化!
$ scp 20180413_1730.tar.gz swrd@192.168.124.80:
```


3. ncftp

```sh
$ sudo apt install -y ncftp

$ ncftp -u swrd -p <密碼> 192.168.124.80
$ cd home
> put 20180413_1730.tar.gz
> bye
# 完成備份 - 分階段上傳

# ncftp 帶密碼
ncftpput -u swrd -p <密碼> 192.168.124.80 home <要上傳的檔案>
```


4. sshpass

- [How to pass password to scp?](https://stackoverflow.com/questions/50096/how-to-pass-password-to-scp?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

```sh
# sshpass -p "password" scp -r user@example.com:/some/remote/path /some/local/path

# sshpass -f "/path/to/passwordfile" scp -r user@example.com:/some/remote/path /some/local/path
```


## lftp (作 `下載` && `差異更新` 的好用工具)

```sh
# 用 lftp 連入遠端網址
$ lftp <url>

# list dir
$ ls

# 同步更新
$ mirror <dir>
# 如果已經下載過, 不下載但會檢查更新 ; 若無, 則下載
```