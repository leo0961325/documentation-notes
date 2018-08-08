# 大量匯入

- 2018/08/06
- MySQL v5.7 on Windows 10

如果打算匯入大量資料(ex: 幾百 MB 的 csv, 到 MySQL), 建議使用 MySQL 的 [LOAD DATA INFILE](https://dev.mysql.com/doc/refman/5.7/en/load-data.html)

語法(MySQL Client 登入後):

```sql
LOAD DATA INFILE '<原始檔案完整路徑>'
INTO TABLE <DB Name>.<Table Name>
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n';
```

↑ `LINES TERMINATED` 保險一點, 使用 `Notepad++` 開啟後, 檢視 分隔符號


## 問題案例

使用 `load data infile` 如果出現 「The MySQL server is running with the --secure-file-priv option so it cannot execute this statement」, 簡單的說就是有安全上的疑慮(吧?)

表示, 要塞到DB的檔案, 因為有啟用 `secure_file_priv`, 解法有兩種:

1. 開啟 `my.ini(Windows 10 上的 MySQL 組態檔)`, 在最後面新增一行 「secure_file_priv=''」, 重啟 MySQL服務
2. 把 要匯入的檔案, 移動到 secure_file_priv 所允許的路徑底下

```sql
--;# MySQL 內, 查詢 secure_file_priv 變數內容
SHOW VARIABLES LIKE "secure_file_priv";
+------------------+------------------------------------------------+
| Variable_name    | Value                                          |
+------------------+------------------------------------------------+
| secure_file_priv | C:\ProgramData\MySQL\MySQL Server 5.7\Uploads\ |
+------------------+------------------------------------------------+
```

使用 `load data infile` 一口氣匯入大量資料(速度蠻快的~~)
```sql
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_alarm.csv' INTO TABLE test_emc.data_alarm FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_pressure.csv' INTO TABLE test_emc.data_pressure FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_status.csv' INTO TABLE test_emc.data_status FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_towerlight.csv' INTO TABLE test_emc.data_towerlight FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_work_orders.csv' INTO TABLE test_emc.work_orders FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/fake_data_products.csv' INTO TABLE test_emc.products FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';
```
Windows 10 預設 DB 放在這邊 : `C:\ProgramData\MySQL\MySQL Server 5.7\Data`