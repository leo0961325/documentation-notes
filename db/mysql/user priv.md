

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