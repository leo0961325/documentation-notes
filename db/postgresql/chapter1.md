# Database Cluster, Databases, and Tables

- 2020/06/02
- http://www.interdb.jp/pg/pgsql01.html


```bash
$# cd $PGDATA && ls -l
drwx------. 9 postgres postgres      97 Apr 24 06:57 base
-rw-------. 1 postgres postgres 1978368 Apr 29 06:28 core.21442
-rw-------. 1 postgres postgres 2289664 Apr 29 05:52 core.26
drwx------. 2 postgres postgres    4096 Jun  2 10:21 global
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_commit_ts
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_dynshmem
-rw-------. 1 postgres postgres    4535 Nov 20  2019 pg_hba.conf          # PG client 認證定義檔
-rw-------. 1 postgres postgres    1636 Nov 20  2019 pg_ident.conf        # PG user name mapping
drwx------. 4 postgres postgres      68 Jun  2 11:35 pg_logical
drwx------. 4 postgres postgres      36 Nov 20  2019 pg_multixact
drwx------. 2 postgres postgres      18 May  7 08:03 pg_notify
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_replslot
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_serial
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_snapshots
drwx------. 2 postgres postgres       6 May  7 08:03 pg_stat
drwx------. 2 postgres postgres     126 Jun  2 11:39 pg_stat_tmp
drwx------. 2 postgres postgres      18 May 25 14:39 pg_subtrans
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_tblspc         # 額外的 data area. (其他 RDBMS 沒有這東西, 此為 PG 僅有)
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_twophase
-rw-------. 1 postgres postgres       3 Nov 20  2019 PG_VERSION             # posgressql 版本
drwx------. 3 postgres postgres    4096 Jun  2 11:35 pg_wal
drwx------. 2 postgres postgres    4096 Apr 18 01:42 pg_xact
-rw-------. 1 postgres postgres      88 Nov 20  2019 postgresql.auto.conf
-rw-------. 1 postgres postgres   23880 Jun  2 03:26 postgresql.conf         # PG 設定主檔
-rw-------. 1 postgres postgres      36 May  7 08:03 postmaster.opts          # 最近一次 PG 啟動所使用的 CLI 選項紀錄
-rw-------. 1 postgres postgres      94 May  7 08:03 postmaster.pid

```

```sql
-- 此與 $PGDATA/base 內容相對應
SELECT datname, oid FROM pg_database;


-- 若 table / index < 1GB, 則該檔案歸屬於 $PGDATA/base/{database}
-- Tables && indexes 都是 database objects, 內部由 OIDs 管理(relfilenode 變數)
SELECT relname, oid, relfilenode FROM pg_class WHERE relname = 'jkb_check_data';
-- oid 與 relfilenode 並不一定會一樣 (如果做了 truncate, reindex, cluster..., 就會導致不同)


-- v9.0 開始, 可用底下這個來查出此 Table 對應的實體路徑
SELECT pg_relation_filepath ('jkb_check_data');
-- 以下便是輸出結果:
-- pg_relation_filepath
-- base/17658/62945

-- 承上, 如果 Table/Index > 1GB, 則會建立
-- base/17658/62945
-- base/17658/62945.1  <-- 新的
-- 而此定義的 1GB, 可使用 --with-segsize 修改

```

```bash
$# cd $PGDATA/base/17658

$# ls -l 62945*
-rw-------. 1 postgres postgres 33202176 Jun  2 11:14 62945
-rw-------. 1 postgres postgres    24576 Jun  2 11:14 62945_fsm  # free space map (Chap 5.3.4)
-rw-------. 1 postgres postgres        0 Jun  2 09:41 62945_vm   # visibility map (Chap 6.2)
# 上述也可視為是 data file 的 forks 關聯檔案
#  - data file 的 fork number 為 0
#  - fsm       的 fork number 為 1
#  - vm        的 fork number 為 2
# Note: Index 只有 visibility map
```




# Other Notes

- pg_xlog   是 v9.6 版 以前 的東西了
- pg_tblspc 是 v8.0 版 以後 加入的東西