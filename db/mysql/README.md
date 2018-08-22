# MySQL 5.7

```sh
$  mysql --version
mysql  Ver 14.14 Distrib 5.7.21, for Linux (x86_64) using  EditLine wrapper
```

- `mysql_demo_data.sql`: `subquery.md` 裏頭使用的範例



# 版本及平台

## For Ubuntu 16.04
ini dir: /etc/mysql/my.cnf
db dir: /var/lib/mysql/


## For CentOS7.3
ini dir: /etc/my.cnf
db dir: /var/lib/mysql
socket: /var/lib/mysql/mysql.sock
log: /var/log/mysqld.log
pid-file: /var/run/mysqld/mysqld.pid


## For Win 10
ini dir: C:\ProgramData\MySQL\MySQL Server 5.7\my.ini
db dir: C:\ProgramData\MySQL\MySQL Server 5.7\Data\



# ER-Model 資料庫規劃
- 2018/06/13

- [關於 Cascade](https://dba.stackexchange.com/questions/44956/good-explanation-of-cascade-on-delete-update-behavior?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

> 若兩個 Table, `Parent` 及 `Child`, 如果 **Foreign Key** 已經被定義為 `ON DELETE CASCADE`, 表示一旦 `Parent` 的 **Primary Key** 被移除後, 則不留孤兒. 而 `ON DELETE RESTRICT` 放在 **Foreign Key** 則表示, 需要把 `Child` 淨空之後, 才可以殺 `Parent`.


## Normalization 正規化

- 第一正規化: 去除重複性
- 第二正規化: `非 Key屬性` 與 `Key 屬性` 完全依賴
- 第三正規化: `非 Key屬性` 之間相互獨立



# 連線相關

- 2018/06/27
- [Waiting for table metadata lock問題](http://ctripmysqldba.iteye.com/blog/1938150)
- [MySQL出现Waiting for table metadata lock的原因以及解决方法](http://blog.51cto.com/11286233/2048000)
- [How do I find which transaction is causing a “Waiting for table metadata lock” state?
](https://stackoverflow.com/questions/13148630/how-do-i-find-which-transaction-is-causing-a-waiting-for-table-metadata-lock-s)
- [資料庫連線占用](https://blog.csdn.net/sinat_30397435/article/details/62932057)
```sh
> show processlist;
+---------+---------------------------------+------------------------------------------+
| Command | State                           | Info                                     |
+---------+---------------------------------+------------------------------------------+
| Sleep   |                                 | NULL                                     |
| Query   | Waiting for table metadata lock | ALTER TABLE `test_emc`.`data_alarm` ...  |
| Query   | starting                        | show processlist                         |
+---------+---------------------------------+------------------------------------------+
# 僅節錄部分欄位...


>  SHOW ENGINE INNODB STATUS \G
# 底下僅節錄部分資料

------------------------
LATEST FOREIGN KEY ERROR
------------------------
2018-06-27 16:29:14 0x46f8 Transaction:
TRANSACTION 14579, ACTIVE 0 sec updating or deleting, thread declared inside InnoDB 4997
mysql tables in use 1, locked 1
5 lock struct(s), heap size 1136, 4 row lock(s), undo log entries 1
MySQL thread id 111, OS thread handle 18168, query id 9225 localhost ::1 tony updating
update data_alarm set alarm = '528' where alarm = '527'
Foreign key constraint fails for table `test_emc`.`data_alarm`:
,
  CONSTRAINT `data_alarm_ibfk_2` FOREIGN KEY (`alarm`) REFERENCES `alarms` (`code`)
Trying to add in child table, in index alarm tuple:
DATA TUPLE: 2 fields;
 0: len 3; hex 353238; asc 528;;
 1: len 4; hex 80000001; asc     ;;

But in parent table `test_emc`.`alarms`, in index PRIMARY,
the closest match we can find is record:
PHYSICAL RECORD: n_fields 4; compact format; info bits 0
 0: len 3; hex 353339; asc 539;;
 1: len 6; hex 000000002997; asc     ) ;;
 2: len 7; hex b60000012a0110; asc     *  ;;
 3: len 18; hex e980b1e69c9fe69982e99693e8ada6e5a0b1; asc                   ;;

------------
TRANSACTIONS
------------
Trx id counter 14589
Purge done for trx''s n:o < 14580 undo n:o < 0 state: running but idle
History list length 133
LIST OF TRANSACTIONS FOR EACH SESSION:
---TRANSACTION 282807065004696, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 282807065005568, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 14581, ACTIVE 3149 sec
2 lock struct(s), heap size 1136, 2 row lock(s), undo log entries 1
MySQL thread id 232, OS thread handle 16664, query id 9229 localhost ::1 admin
Trx read view will not see trx with id >= 14579, sees < 14579
```

因為下了一個有問題的 Alter table 指令, 導致 Table 變成 `Waiting for table metadata lock`... (獨佔鎖啥鬼的)

建議設定 `lock_wait_timeout` 設定超時時間, 避免長時間的 metadata鎖.



# Key

```sql
> show index from <Table Name>;
+--------------+------------+--------------------+--------------+----------------+-----------+----------+--------+
| Table        | Non_unique | Key_name           | Seq_in_index | Column_name    | Collation | Sub_part | Packed |
+--------------+------------+--------------------+--------------+----------------+-----------+----------+--------+
| data_counter |          0 | PRIMARY            |            1 | id             | A         |     NULL | NULL   |
|data_counter  |          1 | fk_wod_code_idx    |            1 | fk_wod_serial  | A         |     NULL | NULL   |
| data_counter |          1 | fk_sensor_code_idx |            1 | fk_sensor_code | A         |     NULL | NULL   |
+--------------+------------+--------------------+--------------+----------------+-----------+----------+--------+
--;# 已移除部分欄位
```



# Reference

- [MySQL 建立Foreign Key ( InnoDB ) 時要注意的一件事](http://lagunawang.pixnet.net/blog/post/25455909-mysql-%E5%BB%BA%E7%AB%8Bforeign-key-%28-innodb-%29-%E6%99%82%E8%A6%81%E6%B3%A8%E6%84%8F%E7%9A%84%E4%B8%80%E4%BB%B6%E4%BA%8B)

預設 FK **不作** `連動更改` (NO ACTION)

```sql
CREATE TABLE `tbl` (
    `id` INT,
    `parent_id` INT,
    INDEX `par_ind` (`parent_id`),
    FOREIGN KEY(`parent_id`) REFERENCES `parent`(`id`) ON DELETE CASCADE ON UPDATE CASADE
);
```

[ON DELETE {CASCADE | SET NULL | NO ACTION | RESTRICT}]

[ON UPDATE {CASCADE | SET NULL | NO ACTION | RESTRICT}]

- `CASCADE`   : FK 欄位一併 刪改
- `SET NULL`  : FK 欄位設為 NULL
- `NO ACTION` : FK 欄位一旦被參照, 則 PK 欄位無法刪改
- `RESTRICT`  : 同 `NO ACTION`



# MySQL 5.7 指令備註

## DML

```sql
drop database tt;
create database tt;
use tt;
create table t1(
    xid int primary key auto_increment, 
    xname varchar(30) not null, xscore int default 0
);

insert into t1(xname, xscore) values ('andy', 88), ('josh', 77), ('howr', 90), ('tony', 99);
insert into t1(xname, xscore) values ('yk', 66), ('john', 75);
select * from t1;

delete from t1 where xname='yk';
select * from t1;

update t1 set xname='michael' where xid=6;
select * from t1;
```


## 查看編碼

```sql
> SELECT @@character_set_database, @@collation_database;
> SHOW variables LIKE 'character%';
```


## 執行外部腳本

```sql
> SOURCE d:\dbinit.sql
```


## 分隔符號

- [只談MySQL (第16天) Stored Procedure及Function](https://ithelp.ithome.com.tw/articles/10032363)

MySQL預設以「;」為分隔符號, 可使用「delimiter //」, 就可把分隔符號改為「//」了.


## 毫秒、微秒 欄位

- [milliseconds](https://stackoverflow.com/questions/13344994/mysql-5-6-datetime-doesnt-accept-milliseconds-microseconds?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

DATETIME(3) -> 毫秒

DATETIME(6) -> 微秒


## 開頭符號

MySQL內, 以下種種, 都有它們所要表達的意思, [看官網說明](https://dev.mysql.com/doc/refman/5.7/en/entering-queries.html)

```sh
# mysql>
# ->
# '>
# ">
# `>
# /*>
```
