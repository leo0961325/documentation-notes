
# 連線相關

- 2018/06/27
- [Waiting for table metadata lock問題](http://ctripmysqldba.iteye.com/blog/1938150)
- [MySQL出现Waiting for table metadata lock的原因以及解决方法](http://blog.51cto.com/11286233/2048000)
- [How do I find which transaction is causing a “Waiting for table metadata lock” state?
](https://stackoverflow.com/questions/13148630/how-do-i-find-which-transaction-is-causing-a-waiting-for-table-metadata-lock-s)
- [資料庫連線占用](https://blog.csdn.net/sinat_30397435/article/details/62932057)
```sh
> show processlist;
+---------+---------------------------------+------------------------------------------+
| Command | State                           | Info                                     |
+---------+---------------------------------+------------------------------------------+
| Sleep   |                                 | NULL                                     |
| Query   | Waiting for table metadata lock | ALTER TABLE `test_emc`.`data_alarm` ...  |
| Query   | starting                        | show processlist                         |
+---------+---------------------------------+------------------------------------------+
# 僅節錄部分欄位...


>  SHOW ENGINE INNODB STATUS \G
# 底下僅節錄部分資料

------------------------
LATEST FOREIGN KEY ERROR
------------------------
2018-06-27 16:29:14 0x46f8 Transaction:
TRANSACTION 14579, ACTIVE 0 sec updating or deleting, thread declared inside InnoDB 4997
mysql tables in use 1, locked 1
5 lock struct(s), heap size 1136, 4 row lock(s), undo log entries 1
MySQL thread id 111, OS thread handle 18168, query id 9225 localhost ::1 tony updating
update data_alarm set alarm = '528' where alarm = '527'
Foreign key constraint fails for table `test_emc`.`data_alarm`:
,
  CONSTRAINT `data_alarm_ibfk_2` FOREIGN KEY (`alarm`) REFERENCES `alarms` (`code`)
Trying to add in child table, in index alarm tuple:
DATA TUPLE: 2 fields;
 0: len 3; hex 353238; asc 528;;
 1: len 4; hex 80000001; asc     ;;

But in parent table `test_emc`.`alarms`, in index PRIMARY,
the closest match we can find is record:
PHYSICAL RECORD: n_fields 4; compact format; info bits 0
 0: len 3; hex 353339; asc 539;;
 1: len 6; hex 000000002997; asc     ) ;;
 2: len 7; hex b60000012a0110; asc     *  ;;
 3: len 18; hex e980b1e69c9fe69982e99693e8ada6e5a0b1; asc                   ;;

------------
TRANSACTIONS
------------
Trx id counter 14589
Purge done for trx''s n:o < 14580 undo n:o < 0 state: running but idle
History list length 133
LIST OF TRANSACTIONS FOR EACH SESSION:
---TRANSACTION 282807065004696, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 282807065005568, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 14581, ACTIVE 3149 sec
2 lock struct(s), heap size 1136, 2 row lock(s), undo log entries 1
MySQL thread id 232, OS thread handle 16664, query id 9229 localhost ::1 admin
Trx read view will not see trx with id >= 14579, sees < 14579
```

因為下了一個有問題的 Alter table 指令, 導致 Table 變成 `Waiting for table metadata lock`... (獨佔鎖啥鬼的)

建議設定 `lock_wait_timeout` 設定超時時間, 避免長時間的 metadata鎖.

而現在... 

```sh

```