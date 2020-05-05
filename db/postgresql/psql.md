# psql


## 設定免密碼連線

- [The Password File](https://www.postgresql.org/docs/11/libpq-pgpass.html)

```bash
### 首先, 要先可以使用 psql
$# which psql
/bin/psql

$# cd ~
$# vim .pgpass
# -----------------------------
127.0.0.1:5432:db_name:user_name:password_of_user
# -----------------------------

$# chmod 600 .pgpass

$# psql -h 127.0.0.1 -p 5432 db_name user_name
psql (9.2.24, server 11.2 (Debian 11.2-1.pgdg90+1))
WARNING: psql version 9.2, server version 11.0.
         Some psql features might not work.
Type "help" for help.

db_name=#
# ↑ 不用密碼, 連信去了
```
