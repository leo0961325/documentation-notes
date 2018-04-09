# MYSQL user permission(使用者權限 )
- 2018/01/23

## 建立 user
```sql
> CREATE USER '<帳號>'@'<HOST>' IDENTIFIED BY '<密碼>';

> GRANT ALL ON <DB>.<Table> TO '<帳號>'@'<HOST>';
```


## 更改密碼
```sql
> ALTER USER '<使用者帳號>' IDENTIFIED BY '<新密碼>';
```


## 查詢使用者資訊
```sql
> SELECT User, Host FROM mysql.user;
```