# MYSQL 指令備註
- 2018/01/23

```
> systeminfo
作業系統名稱:         Microsoft Windows 10 專業版
系統類型:             x64-based PC
系統地區設定:         zh-tw;中文 (台灣)
輸入法地區設定:       zh-tw;中文 (台灣)
# ...((僅節錄部分資訊))...

> mysql --version
mysql  Ver 14.14 Distrib 5.7.19, for Win64 (x86_64)

```

建立使用者 && 賦予權限
```sql
CREATE USER '<帳號>'@'<HOST>' IDENTIFIED BY '<密碼>';

GRANT ALL ON <DB>.<Table> TO '<帳號>'@'<HOST>';
```

更改密碼
```sql
ALTER USER '<使用者帳號>' IDENTIFIED BY '<新密碼>';
```

查詢使用者資訊
```sql
SELECT User, Host FROM mysql.user;
```