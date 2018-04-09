# backup

## 使用 `mysqldump` 做完整備份
```sh
$ mysqldump -u 'root' -p 'pome' --single-transaction --flush-logs --master-data=2 --all-databases --delete-master-logs > /home/pome/    backup/mysql/full_backup_`date +\%H\%M`.sql
```

## 備份 backup
pyhsical                           | logical
---------------------------------- | --------
快                                 | 慢
企業級                              | -
無法 backup Memory中資料            | 可
mysqlbackup                        | mysqldump
會有 Engine問題                     | 可跨 Engine
可能需要關服務, backup比較不會有問題  | 可以暖備份

### 1. 工具函式 mysqldump
```sh
# 將 transaction flush到檔案: `mysqladmin -uroot -p flush-logs`
mysqladmin -uroot -p flush-logs

# db backup
> mysqldump <db name> -u<帳號> -p<密碼> --opt > <backup name.sql>

# 對於 InnoDB, 執行 non-lock online backup
> mysqldump--single-transaction

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


## 還原 restore
> 依備份檔還原資料庫, 語法: `mysql [DB Name] -uroot -p < [備份的文檔名稱.sql]`
```sh
# 還原前, 關閉二進位日誌
$ mysql > set sql_log_bin=0;

$ mysql tt -uroot -p < ttbck.sql

$ mysql > set sql_log_bin=1;
```