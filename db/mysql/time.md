# 關於時間
- 2018/07
- [adding 30 minutes to datetime php/mysql
](https://stackoverflow.com/questions/1436827/adding-30-minutes-to-datetime-php-mysql?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- [Should I use the datetime or timestamp data type in MySQL?](https://stackoverflow.com/questions/409286/should-i-use-the-datetime-or-timestamp-data-type-in-mysql?rq=1)

```sql

SELECT CURRENT_TIMESTAMP;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 SECOND;  # +10 seconds
SELECT CURRENT_TIMESTAMP + INTERVAL 10 MINUTE;  # +10 minutes
SELECT CURRENT_TIMESTAMP + INTERVAL 10 HOUR;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 DAY;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 MONTH;
SELECT CURRENT_TIMESTAMP + INTERVAL 10 YEAR;
```


# MySQL Server Time Zone

MySQL 具有下列幾種的 Time Zone Setting:
1. System time zone
2. Server's current time zone
3. Per-connection time zones



## 1. System time zone

Server啟動後, 使用 `Host Machine 所在時區` 當成 MySQL `@@system_time_zone` (系統變數), 之後不再改變.

```sql
# -- # Windows 10 MySQL 5.7.19
> SELECT @@system_time_zone;
+--------------------+
| @@system_time_zone |
+--------------------+
| ¥x¥_¼зǮɶ¡          |      # -- # chcp 65001(utf-8) 看到的 乾~ 這三小...
+--------------------+

+--------------------+
| @@system_time_zone |
+--------------------+
| ?x?_?з???          |      # -- # chcp 950(big5) 看到的... 傻眼
+--------------------+
```

官方底下這段不是很懂..

    You can set the system time zone for MySQL Server at startup with the --timezone=timezone_name option to mysqld_safe. You can also set it by setting the TZ environment variable before you start mysqld. The permissible values for --timezone or TZ are system dependent. Consult your operating system documentation to see what values are acceptable.


## 2. Server's current time zone

MySQL 全域系統變數 `time_zone` 為 MySQL Server 的 *current time zone*

預設 `@@time_zone` = 'SYSTEM', 此表示, **Server time zone = System time zone**

```sql
> SELECT @@time_zone;
+-------------+
| @@time_zone |
+-------------+
| SYSTEM      |
+-------------+
```

> Note (官方這段備註 好像不是很重要... ) <br> 
> If set to SYSTEM, every MySQL function call that requires a timezone calculation makes a system library call to determine the current system timezone. This call may be protected by a global mutex, resulting in contention.

改變 `@@time_zone` 的方式有 3 種:
1. 組態檔, 於 **[mysqld]** 下方, 更改 `default-time-zone` = timezone, ex: **default-time-zone = '+8:00'**
2. Command Line 起始 MySQL Daemon, 使用 `--default-time-zone` = timezone;
3. 於 Runtime 時, 使用 SET GLOBAL `time_zone` = timezone;    (SUPER privilege才能用)



## 3. Per-connection time zones

每個 MySQL 連線 都擁有他自己的 time zone setting, 此即為 session `time_zone` variable. 預設的 session `time_zone` variable 來自 global `time_zone` variable.

```sql
> SELECT @@SESSION.time_zone;
+---------------------+
| @@SESSION.time_zone |
+---------------------+
| SYSTEM              |
+---------------------+

--#; 更改的方式如:
--#; > set  time_zone = '+8:00';
```

# [MySQL 時區設定](https://paper.tuisec.win/detail/f7cdb5df913d4b8)

timezone為字串型態, 代表 `UTC的偏移量`

```sql
> SELECT @@system_time_zone, @@global.time_zone, @@session.time_zone;
+--------------------+--------------------+---------------------+
| @@system_time_zone | @@global.time_zone | @@session.time_zone |
+--------------------+--------------------+---------------------+
| ¥x¥_¼зǮɶ¡          | SYSTEM             | SYSTEM              |
+--------------------+--------------------+---------------------+

--#; 或

> SHOW VARIABLES like '%time_zone%';
+------------------+--------+
| Variable_name    | Value  |
+------------------+--------+
| system_time_zone |        |
| time_zone        | SYSTEM |
+------------------+--------+
```

```sql
> SELECT CURTIME();
+-----------+
| CURTIME() |
+-----------+
| 10:04:28  |
+-----------+

> SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2018-07-23 10:04:32 |
+---------------------
```