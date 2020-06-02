# 基礎

- [Introduction to PostgreSQL physical storage](http://rachbelaid.com/introduction-to-postgres-physical-storage/)

一條 Query 送到 DB, 會經過 `查詢分析`, `查詢重寫`, `查詢規劃`, `查詢執行` 這幾個階段才能獲得最後的結果


# terminology

- Tuple/Item: A synonym for a row
- Block/Page: Represent a 8kb segment information the file storing the table.
- Heap: Refer to heap file. Heap files are lists of unordered records of variable size. Although sharing a similar name, heap files are different from heap data structure.
- CTID: Represent the physical location of the row version within its table. CTID is also a special column available for every tables but not visible unless specifically mentioned. It consists of a page number and the index of an item identifier.
- OIDs: Object identifiers. PostgreSQL 內部用來管理所有的 database object. 此為 *unsigned 4-byte integers*




```bash
$# cd $PGDATA
$# ll
$PGDATA/base/
            /1
            /
$PGDATA/core.21442
$PGDATA/core.26
$PGDATA/global
$PGDATA/pg_commit_ts
$PGDATA/pg_dynshmem
$PGDATA/pg_hba.conf
$PGDATA/pg_ident.conf
$PGDATA/pg_logical
$PGDATA/pg_multixact
$PGDATA/pg_notify
$PGDATA/pg_replslot
$PGDATA/pg_serial
$PGDATA/pg_snapshots
$PGDATA/pg_stat
$PGDATA/pg_stat_tmp
$PGDATA/pg_subtrans
$PGDATA/pg_tblspc
$PGDATA/pg_twophase
$PGDATA/PG_VERSION
$PGDATA/pg_wal
$PGDATA/pg_xact
$PGDATA/postgresql.auto.conf
$PGDATA/postgresql.conf
$PGDATA/postmaster.opts
$PGDATA/postmaster.pid
```


