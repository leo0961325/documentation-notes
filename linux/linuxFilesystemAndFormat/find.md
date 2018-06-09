# 搜尋
- 2018/06/09
- [鳥哥 尋找](http://linux.vbird.org/linux_basic/0220filemanager.php#whereis)


# 1. 找指令
```sh
# 搜尋 某個指令放在哪裡
$ which [-a] command
# -a: 把所有找得到的都列出來, 不要只列一個

$ which ifconfig
/sbin/ifconfig

# which 會從 PATH 環境變數裏頭, 找出 command 的位置
# 而 history 為 「bash的內建指令」, 所以會找不到
$ which history
/usr/bin/which: no history in (/opt/anaconda3//bin:/opt/jdk1.8//bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/tony/.local/bin:/home/tony/bin)

$ history --help
-bash: history: --：無效選項
history: usage: history [-c] [-d offset] [n] or history -anrw [filename] or history -ps arg [arg...]
```

# 2. 找檔案
- whereis : 只找 特定目錄 下的檔案(快)
- locate : 利用 資料庫 來搜尋檔名(快)
- find : 很操硬碟(慢)

## 1. whereis

> 只會去尋找`特定目錄`, 主要針對 `/bin`, `/sbin`, `/usr/share/man` 等資料夾作搜尋而已, 可用 `whereis -l` 來看究竟找了那些資料夾

```sh
$ whereis [-bmsu] <file or dir>

$ whereis ifconfig
ifconfig: /usr/sbin/ifconfig /usr/share/man/man8/ifconfig.8.gz
```

## 2. locate/updatedb

> locate 依據 「已建立的資料庫 /var/lib/mlocate/」, 找出要查的關鍵字 ; updatedb(此指令下下去, 可能要等一下子) 根據 `/etc/updatedb.conf` 設定去搜尋磁碟內的檔名, 並更新 `/var/lib/mlocate` 內的資料庫檔案


```sh
$ locate [-ir] keywork


$ locate -l 5 passwd    # 「-l 5」找出所有與 passwd 相關的檔名, 僅輸出 5 個
/etc/passwd
/etc/passwd-
/etc/pam.d/passwd
/etc/security/opasswd
/opt/anaconda3/pkgs/openssl-1.0.2l-h077ae2c_5/ssl/man/man1/passwd.1
```


## 3. find


### 基本語法
```sh
$ find [PATH] [option] [action]
# 時間選項 : -atime, -ctime, -mtime
# 使用者/群組參數
# 檔案權限相關參數
# 額外可進行的動作
```


### 依 時間 find
```
# -mtime n : 表示 「在 n 天前」的「一天之內」被更動過內容的檔案
$ find / -mtime 0
# (會開始搜尋~~~ 有點久, 然後印出一大堆不知道幹嘛的)

# 尋找 /etc 底下, 檔案日期 比 /etc/passwd 還新的
$ find /etc -newer /etc/passwd



# 找出 4天之內被更動過的檔案名稱
$ find /var -mtime -4

# 找出 4天之前的 1天內被更動過的檔案名稱
$ find /var -mtime 4

# 找出 大於 5天之前被更動過的檔案名稱
$ find /var +mtime 4
```

### 依 使用者/群組 find
```sh
# 尋找 /home 下, 屬於 tony 的檔案
$ find /home --user tony

# 尋找 不屬於任何使用者的檔案
$ sudo ls -l /etc | grep ssmtp
drwxr-s---.  2 root mail       42  4月 11 18:13 ssmtp   # ex: 自行編譯原始碼軟體時, 就會經常看到
```

### 依 權限 find
```sh
$ find /run -type s
# 找出 /run 底下, 類型為 Socket的檔案

$ find / -perm /7000
# 找出「---s--s--t」權限的檔案(任意一個即可)

$ find / -perm -7000
# 找出完全符合「---s--s--t」權限的檔案
```

### 額外附加選項的 find (有點偏, 懶得寫了)

```sh
$ find / size +1M
# 找出 > 1MB 檔案
```
