# Database Cluster, Databases, and Tables

- 2020/06/02
- [Database Cluster, Databases, and Tables](http://www.interdb.jp/pg/pgsql01.html)


## 1. Database Cluster 的邏輯結構

- PostgreSQL Cluster 並非指叢集, PostgreSQL Server 只在單一 host 上頭 運行/管理 Single database cluster
- PostgreSQL 使用 **object identifiers(OIDs)** (4-bytes) 來辨識 database objects.
- Database Object 內含有:
  - Tables
  - Indexes
  - Other objects
    - Views
    - functions
    - sequences

```sql
-- 此與 $PGDATA/base 內容相對應
SELECT datname, oid FROM pg_database WHERE datname = 'dayu';
-- | datname | oid   |
-- | ------- | ----- |
-- | dayu    | 16428 |

-- 若 table / index < 1GB, 則該檔案歸屬於 $PGDATA/base/{database}
-- Tables && indexes 都是 database objects, 內部由 OIDs 管理(relfilenode 變數)
SELECT relname, oid, relfilenode FROM pg_class WHERE relname = 'jkb_check_data';
-- | relname        | oid    | relfilenode |
-- | -------------- | ------ | ----------- |
-- | jkb_check_data	| 350272 | 350272      |
-- oid 與 relfilenode 並不一定會一樣 (如果做了 truncate, reindex, cluster..., 就會導致不同)
```


## 2. Database 的物理結構

```bash
$# cd $PGDATA && ls -l
drwx------. 9 postgres postgres      97 Apr 24 06:57 base                 # 
-rw-------. 1 postgres postgres 1978368 Apr 29 06:28 core.21442
-rw-------. 1 postgres postgres 2289664 Apr 29 05:52 core.26
drwx------. 2 postgres postgres    4096 Jun  2 10:21 global               # Cluster-wide tables 等的子目錄, ex: pg_database && pg_control
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
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_tblspc         # 額外的 data area. (其他 RDBMS 沒有這東西, 此為 PG 僅有). 指向 tablespaces 的 soft links
drwx------. 2 postgres postgres       6 Nov 20  2019 pg_twophase
-rw-------. 1 postgres postgres       3 Nov 20  2019 PG_VERSION             # posgressql 版本
drwx------. 3 postgres postgres    4096 Jun  2 11:35 pg_wal                # WAL (Write Ahead Logging)(預寫日誌), 自 v10 後, 由 pg_xlog 重新命名
drwx------. 2 postgres postgres    4096 Apr 18 01:42 pg_xact
-rw-------. 1 postgres postgres      88 Nov 20  2019 postgresql.auto.conf   # 儲存組態參數
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


-- 先建立 /var/lib/postgresql/tblspc
CREATE TABLESPACE demo_dbspace LOCATION '/var/lib/postgresql/tblspc';
-- DROP TABLESPACE IF EXISTS demo_dbspace;

CREATE TABLE dayu_monitoring.newtbl (
	xid INT,
	xname VARCHAR(16)
) TABLESPACE demo_dbspace;

SELECT pg_relation_filepath('newtbl');
-- 得到
-- pg_relation_filepath
-- pg_tblspc/63108/PG_11_201809051/17658/63109
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

## 3. Heap Table File 的內部 Layout

每個 table 的 page 包含 3 個部分:
1. heap tuples(record data)   : 從 page 底部開始向上堆疊(stack). (要深入了解他的話, 需要先懂 *Concurrency Control(CC)* && *Write-Ahead Logging(WAL)*)
2. line pointer(item pointer) : 與 heap tuple 為 1對1. 4bytes, 裏頭有個 pointer, 指向 heap tuple, 可把它視為 tuples 的 Index. 每個 line pointer 都有個編號(offset number), 從 1 開始
3. header data                : 24 bytes, 此包含了 page 的表頭資訊. 底下節錄幾個重要參數:
	- pd_lsn      : Unsigned 8-bytes, This variable stores the LSN of XLOG record written by the last change of this page.
	- pd_checksum : 此 page 的 checksum. v9.3 以前, 存在於 timelineId of the page
	- pd_lower    : free space 的起始位置. (最後一個 line pointer, 間接指向最新一筆 heap tuple)
	- pd_upper    : free space 的結束位置. (最新一筆 heap tuple)
	- pd_special  : special space 的起始位置. (用於索引) In the page within tables, it points to the end of the page. 

備註

- heap tuple > 2KB (1/4 的 page size) 的話會使用 **TOAST(The Oversized-Attribute Storage Technique)** 機制來做儲存及管理
- free space(hole)
- tuple identifier, TID : 用來識別 table 內部的 tuple. A TID comprises a pair of values:
  - the *block number* of the page that contains the tuple
  - the *offset number* of the line pointer that points to the tuple
  - 例如: `(2,3)`, 表示找 page 2 的第 4 筆


## 4. 讀寫 Heap Tuples 的方法

```sql
-- 底下兩個查詢結果相同
select * from jkb_check_data offset 1 limit 1;
select ctid, * from jkb_check_data where ctid = '(0,2)';
```

↑ 範例比較偏, PostgreSQL 提供了 TID-Scan, Bitmap-Scan, Index-Only-Scan

上頭使用了 TID-Scan, 直接藉由 TID 來去找 tuple 第0頁的第4筆


# Other Notes

- pg_xlog              是 v9.6 前 的東西
- pg_tblspc            自 v8.0 後 加入
- pd_checksum          自 v9.3 後 加入
- postgresql.auto.conf 自 v9.4 後 加入
- pg_wal               自 v10  後 加入
- pg_xact              自 v10  後 加入
- 查看當前 session 快取的查詢計畫 `select * from pg_prepared_statements;` (只在當前 session 有效, 會在當前 session 結束時被釋放)