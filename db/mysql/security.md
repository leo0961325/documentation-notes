

# 組態

## 
- 2018/06/27
- [Safe Update Mode](http://chingsoo.pixnet.net/blog/post/292464274-%5Bmysql%5D-%E9%97%9C%E9%96%89safe-update-mode)
```sh
> select * from data_alarm;
+----+-------+-------+---------------------+--------+
| id | src   | alarm | dt_start            | dt_end |
+----+-------+-------+---------------------+--------+
|  1 | emcgo | 527   | 2018-06-27 16:00:25 | NULL   | 
+----+-------+-------+---------------------+--------+
1 row in set (0.00 sec)

# 打算把 dt_end 為 NULL 者, 改為現在時間
# CLI環境
> UPDATE `data_alarm` SET `dt_end` = CURRENT_TIMESTAMP where `dt_end` IS NULL;

# ↑ 語法沒錯, 但是整個 BLOCK 住...

# 在 MySQL WorkBench 則告知: 並非使用 KEY column 來做修改...
# You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column
```


```sh
> show variables like '%safe_updates%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| sql_safe_updates | OFF   |
+------------------+-------+
1 row in set, 1 warning (0.00 sec)

> SET SQL_SAFE_UPDATES=0;
Query OK, 0 rows affected (0.00 sec)
```