# Process 及 Memory 架構

- 2020/06/03
- [Process and Memory Architecture](http://www.interdb.jp/pg/pgsql02.html)

## 1. 程序架構

- A postgres server Process : PostgreSQL Server 的主程序
- Each backend Process      : 處理所有 SQL Statements 的各個程序
- All background Processes  : 執行所有程序的功能, ex: VACUUM, CHECKPOINT, LOG, ...
- Replication Processes     : 其他 PostgreSQL Server 執行 replication 的程序
- Background worker Process : SQL Client 所執行的程序

### 1-1. Postgres Server Process

PostgreSQL 程序之父, 早期版本又稱為 postmaster

一切由 `pg_ctl` CLI 來啟動

接收所有客戶端連線, 會開啟一個 backend process, 而此 backend process 會用來處理所有的 CRUD


### 1-2. Backend Process

後端進程, 又稱之為 `postgres`

與 Client 進行 TCP Connection && 處理 SQL Statements(CRUD) && 等待斷線

允許多客戶端同時連線, 由 `max_connections` 來控制, 預設為 100 條(由 postgresql.conf 裏頭修改)

如果客戶端過於頻繁的 連線+斷線, 因 PostgreSQL 沒有實作連線池(不知道 v11 有沒有了?), 所以會藉由 `pooling middleware(pgbouncer, Pgpool-II)` 來處理, 減少連線成本


### 1-3. Background Processes

- background writer : 定期把 Shared buffer pool 寫入 disk. v9.1 以前, 此任務是 checkpointer process 在作的.
- checkpointer : Checkpoint process
- autovacuum launcher : 定期建立 autovacuum-worker processes 來清理 PostgreSQL Server
- WAL writer : 定期 清/寫 WAL 快取到 disk
- statistics collector : 蒐集 `pg_stat_activity` && `pg_stat_database` 等等的統計資訊
- logger   : 專門寫 log
- archiver : 壓縮 logging


## 2. 記憶體架構

PostgreSQL 把記憶體架構區分成底下兩類:

- Local memory area  : backend process 各自使用
- Shared memory area : 所有 processes 共同使用

### 2-1. Local Memory Area

主要有底下幾個 sub-areas:

- work_mem             : 執行器使用這個記憶體區塊來做 **ORDER BY** && **DISTINCT** && **merge-join** && **hash-join** 等
- maintenance_work_mem : 作維護相關的使用區, ex: **VACUUM**, **REINDEX** 等
- temp_buffers         : 儲存 temporary tables


### 2-2. Shared Memory Area

此記憶體區塊隨 PostgreSQL Server on 起來之後就分配出來了. 這個區域主要被區分成底下的 sub-areas:

- shared buffer pool : PG 從 tables 內的 pages && disk 內的 indexes 讀取來這邊操作
- WAL buffer         : WAL: Write Ahead Logging (預寫日誌). transaction log. 此為寫入 disk 之前的緩衝區
- commit log         : 因 Concurrency Control(CC) 的機制, Commit Log(CLOG) 用來保存所有交易的狀態


### 2-3. Other...

- 用來作 access control: semaphores, lightweight locks, shared && exclusive locks
- transaction process: 例如 save-point && two-phase-commit


# Other Notes

- Background worker Process : v9.3 後
- checkpointer process : v9.2 後