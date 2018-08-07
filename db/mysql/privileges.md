# MYSQL user privileges(使用者權限 )
- 2018/01/23



## 建立 user
```sql
> CREATE USER '<帳號>'@'<HOST>' IDENTIFIED BY '<密碼>';
# <HOST> 只能用 'localhost', 無法使用'127.0.0.1'...

> GRANT ALL ON <DB>.<Table> TO '<帳號>'@'<HOST>';
```



移除使用者
```sql
DROP USER '<帳號>'@'<HOST>';
```


## 更改密碼
```sql
> ALTER USER '<使用者帳號>' IDENTIFIED BY '<新密碼>';
```


## 查詢使用者資訊
```sql
> SELECT User, Host FROM mysql.user;
```



### 範例
```sql
drop database ww;
create database ww character set utf8;
use ww;
create table ee (
    `id`        int         primary key auto_increment,
    `datetime`  datetime    NOT NULL,
    `value`     varchar(5)  NOT NULL,
    `source`    varchar(20) NOT NULL
);
delete from ee where `source` = 'tl01';
insert into ee (`datetime`, `value`, `source`) values
    (CURRENT_TIMESTAMP+0, '001', 't01'),
    (CURRENT_TIMESTAMP+1, '001', 't01'),
    (CURRENT_TIMESTAMP+2, '001', 't01'),
    (CURRENT_TIMESTAMP+3, '011', 't01'),
    (CURRENT_TIMESTAMP+4, '011', 't01'),
    (CURRENT_TIMESTAMP+5, '011', 't01'),
    (CURRENT_TIMESTAMP+6, '001', 't01');
select * from ee;
```

```sql
> SHOW GRANTS FOR CURRENT_USER;
+---------------------------------------------------------------------+
| Grants for root@localhost                                           |
+---------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
| GRANT PROXY ON ''@'' TO 'root'@'localhost' WITH GRANT OPTION        |
+---------------------------------------------------------------------+
```



```sql
mysql> create user 'qq'@'localhost' identified by '1234';
mysql> grant all on test.* to 'qq'@'localhost';
```

```sql
mysql> show grants for 'qq'@'localhost';
+------------------------------------------------------+
| Grants for qq@localhost                              |
+------------------------------------------------------+
| GRANT USAGE ON *.* TO 'qq'@'localhost'               |
| GRANT ALL PRIVILEGES ON `test`.* TO 'qq'@'localhost' |
+------------------------------------------------------+
```