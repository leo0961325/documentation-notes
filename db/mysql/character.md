# 編碼問題
- 2018/05/10
- [Mysql調整成全UTF-8語系](http://bunkera.pixnet.net/blog/post/24326115-mysql%E8%AA%BF%E6%95%B4%E6%88%90%E5%85%A8utf-8%E8%AA%9E%E7%B3%BB)

建立 Database時, 預設的 字元集(Character Set)會使用 `連線到 MySQL Server 的 Client 的 Character set`


```sql
# 進入MySQL後
> \s
--------------
mysql  Ver 14.14 Distrib 5.7.19, for Win64 (x86_64)

Connection id:          2
Current database:       tt
Current user:           tony@192.168.124.94
SSL:                    Cipher in use is DHE-RSA-AES256-SHA
Using delimiter:        ;
Server version:         5.7.21 MySQL Community Server (GPL)
Protocol version:       10
Connection:             192.168.124.73 via TCP/IP
Server characterset:    latin1
Db     characterset:    latin1
Client characterset:    big5
Conn.  characterset:    big5
TCP port:               3306
Uptime:                 4 min 36 sec

Threads: 1  Questions: 9  Slow queries: 0  Opens: 106  Flush tables: 1  Open tables: 99  Queries per second avg: 0.032
--------------
```

### 以下模擬 2種情境
1. Windows10 command terminal

```cmd
> chcp
使用中的字碼頁: 950
```

```sql
mysql> CREATE DATABASE qq;
mysql> USE qq
mysql> show variables like 'character%';
+--------------------------+---------------------------------------------------------+
| Variable_name            | Value                                                   |
+--------------------------+---------------------------------------------------------+
| character_set_client     | big5                                                    |
| character_set_connection | big5                                                    |
| character_set_database   | utf8                                                    |
| character_set_filesystem | binary                                                  |
| character_set_results    | big5                                                    |
| character_set_server     | utf8                                                    |
| character_set_system     | utf8                                                    |
| character_sets_dir       | C:\Program Files\MySQL\MySQL Server 5.7\share\charsets\ |
+--------------------------+---------------------------------------------------------+
```


2. Linux Terminal

```sh
$ echo $LANG
zh_TW.UTF-8
```

```sql
mysql> CREATE DATABASE qq;
mysql> USE qq
mysql> show variables like 'character%';
+--------------------------+---------------------------------------------------------+
| Variable_name            | Value                                                   |
+--------------------------+---------------------------------------------------------+
| character_set_client     | utf8                                                    |
| character_set_connection | utf8                                                    |
| character_set_database   | utf8                                                    |
| character_set_filesystem | binary                                                  |
| character_set_results    | utf8                                                    |
| character_set_server     | utf8                                                    |
| character_set_system     | utf8                                                    |
| character_sets_dir       | C:\Program Files\MySQL\MySQL Server 5.7\share\charsets\ |
+--------------------------+---------------------------------------------------------+
```

所以在 MySQL 使用 `source` 指令時, 如果要執行的腳本內, 有 *非英文字* 時, 要注意到編碼問題


# Database Server 編碼問題
- [MySQL 將預設資料庫編碼 latin1 改為 UTF8](https://shazi.info/mysql-%E5%B0%87%E9%A0%90%E8%A8%AD%E8%B3%87%E6%96%99%E5%BA%AB%E7%B7%A8%E7%A2%BC-latin1-%E6%94%B9%E7%82%BA-utf8/)

發現說, Linux 底下的 MySQL **character_set_server** 居然是 `latin1` ; 但是 Windows底下卻是 `utf8`, 如何調整
```sh
$ vim /etc/my.cnf # for Ubuntu

[mysqld]
character-set-server=utf8
collation-server=utf8_unicode_ci 
```