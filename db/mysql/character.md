# 編碼問題
- 2018/05/10

建立 Database時, 預設的 字元集(Character Set)會使用 `連線到 MySQL Server 的 Client 的 Character set`


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