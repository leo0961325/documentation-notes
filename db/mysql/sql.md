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
mysql> select @@character_set_database, @@collation_database;

mysql> show variables LIKE 'character%';
```

## 執行外部腳本
> 語法: ``
```sql
mysql> source d:\dbinit.sql
```


## COMMAND LINE編碼
- [Change default code page of Windows console to UTF-8](https://superuser.com/questions/269818/change-default-code-page-of-windows-console-to-utf-8?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
```
chcp 65001
```

## 分隔符號
- [只談MySQL (第16天) Stored Procedure及Function](https://ithelp.ithome.com.tw/articles/10032363)
MySQL預設以「;」為分隔符號, 可使用「delimiter //」, 就可把分隔符號改為「//」了.


## 毫秒、微秒 欄位
- [milliseconds](https://stackoverflow.com/questions/13344994/mysql-5-6-datetime-doesnt-accept-milliseconds-microseconds?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

DATETIME(3) -> 毫秒

DATETIME(6) -> 微秒