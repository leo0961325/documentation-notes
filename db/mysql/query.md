# 查詢語法細節 v5.7.19


```sql
mysql> SELECT VERSION();
+------------+
| VERSION()  |
+------------+
| 5.7.19-log |
+------------+
1 row in set (0.00 sec)
```

```sh
mysql> # 中斷查詢語法, 且不執行
mysql> SELECT USER()
    ->\c
mysql>
```

---
MySQL內, 以下種種, 都有它們所要表達的意思, [看官網說明](https://dev.mysql.com/doc/refman/5.7/en/entering-queries.html)
```sh
# mysql>
# ->
# '>
# ">
# `>
# /*>
```