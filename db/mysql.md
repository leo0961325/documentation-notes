# MySQL 5.7 on CentOS7

我的環境
```sh
$ 
CentOS7
```

> DB目錄: /var/lib/mysql/

> (Ubuntu16.04)組態目錄: /etc/mysql/mysql.cnf<br>
> (CentOS7.3)組態目錄: /etc/my.cnf

## 模擬資料
```sql
drop database tt;
create database tt;
use tt;
create table t1(xid int primary key auto_increment, xname varchar(30) not null, xscore int default 0);
insert into t1(xname, xscore) values ('andy', 88), ('josh', 77), ('howr', 90), ('tony', 99);

insert into t1(xname, xscore) values ('yk', 66), ('john', 75);
```
## backup

pyhsical | logical
-------- | --------
快 | 慢
企業級 | -
無法 backup Memory中資料 | 可
mysqlbackup | mysqldump
會有 Engine問題 | 可跨 Engine
可能需要關服務, backup比較不會有問題 | 可以暖備份

### 1. 工具函式 mysqldump
> 將 transaction flush到檔案, 語法: `mysqladmin -uroot -p flush-logs` 

> 資料庫備份, 語法: `mysqldump <DB Name> -uroot -p --opt > <備份的文檔名稱.sql>`

> 對於 InnoDB, 執行 non-lock online backup `mysqldump--single-transaction`
```sh
# full backup 'tt資料庫' 到 tt.sql
$ mysqldump --user=root -p tt > ttbck.sql
$ ll
-rw-rw-r--  1 tony tony    0  三   6 10:16 tt.sql

# 依照時間做備份紀錄
$ mysqldump --user=root -p tt > 
```

### 2. LVM快照備份
```sh
$ mysql>FLUSH TABLES WITHREAD LOCK


```


## restore
> 依備份檔還原資料庫, 語法: `mysql [DB Name] -uroot -p < [備份的文檔名稱.sql]`
```sh
# 還原前, 關閉二進位日誌
$ mysql > set sql_log_bin=0;

$ mysql tt -uroot -p < ttbck.sql

$ mysql > set sql_log_bin=1;
```


