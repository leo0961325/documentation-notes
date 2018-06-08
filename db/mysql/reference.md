# Key



```sql
show index from <Table Name>;
+--------------+------------+--------------------+--------------+----------------+-----------+----------+--------+
| Table        | Non_unique | Key_name           | Seq_in_index | Column_name    | Collation | Sub_part | Packed |
+--------------+------------+--------------------+--------------+----------------+-----------+----------+--------+
| data_counter |          0 | PRIMARY            |            1 | id             | A         |     NULL | NULL   |
|data_counter  |          1 | fk_wod_code_idx    |            1 | fk_wod_serial  | A         |     NULL | NULL   |
| data_counter |          1 | fk_sensor_code_idx |            1 | fk_sensor_code | A         |     NULL | NULL   |
+--------------+------------+--------------------+--------------+----------------+-----------+----------+--------+
# 已移除部分欄位
```



# Reference
- [MySQL 建立Foreign Key ( InnoDB ) 時要注意的一件事](http://lagunawang.pixnet.net/blog/post/25455909-mysql-%E5%BB%BA%E7%AB%8Bforeign-key-%28-innodb-%29-%E6%99%82%E8%A6%81%E6%B3%A8%E6%84%8F%E7%9A%84%E4%B8%80%E4%BB%B6%E4%BA%8B)



```
[ON DELETE {CASCADE | SET NULL | NO ACTION | RESTRICT}]
[ON UPDATE {CASCADE | SET NULL | NO ACTION | RESTRICT}]
```