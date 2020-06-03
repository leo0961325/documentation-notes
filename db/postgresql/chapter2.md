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


## 2. 記憶體架構

- Local memory area  : backend process 各自使用
- Shared memory area : 所有 processes 共同使用


# Other Notes

- Background worker Process : v9.3 後