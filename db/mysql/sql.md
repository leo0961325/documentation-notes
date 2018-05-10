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