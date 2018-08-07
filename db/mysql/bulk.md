# 大量匯入
- 2018/08/06
- [Load Data Infile](https://dev.mysql.com/doc/refman/5.7/en/load-data.html)
- MySQL v5.7

```sh
LOAD DATA INFILE '<原始檔案>'
INTO TABLE <DB Name>.<Table Name>
FIELDS TERMINATED BY ','
```

## problem - 使用 `load data infile` 如果出現

- [How should I tackle --secure-file-priv in MySQL?](https://stackoverflow.com/questions/32737478/how-should-i-tackle-secure-file-priv-in-mysql)

    The MySQL server is running with the --secure-file-priv option so it cannot execute this statement

表示, 要塞到DB的檔案, 因為有啟用 `secure_file_priv`, 解法有兩種:

1. 關閉 `secure_file_priv`
2. 把要塞的檔案, 移動到 `secure_file_priv` 所允許的目錄內, 如下:

```sql
SHOW VARIABLES LIKE "secure_file_priv";
+------------------+------------------------------------------------+
| Variable_name    | Value                                          |
+------------------+------------------------------------------------+
| secure_file_priv | C:\ProgramData\MySQL\MySQL Server 5.7\Uploads\ |
+------------------+------------------------------------------------+
# 開啟 my.ini, 更改 secure_file_priv=''
```


```sql
mysql> LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_alarm.csv' INTO TABLE test_emc.data_alarm FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
mysql> LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_pressure.csv' INTO TABLE test_emc.data_pressure FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
mysql> LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_status.csv' INTO TABLE test_emc.data_status FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
mysql> LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_towerlight.csv' INTO TABLE test_emc.data_towerlight FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';


#--# 此表示需要到 mysql 組態檔, 修改 secure_file_priv='', 並重啟服務
```