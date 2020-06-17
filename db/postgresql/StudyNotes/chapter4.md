# Foreign Data Wrappers and Parallel Query

- http://www.interdb.jp/pg/pgsql04.html
- 2020/06/10

## 1. Foreign Data Wrappers, FDW 外部資料包裝器

2003年, SQL standard 增加了一項規範: 用來存取遠端資料, 稱之為 **SQL Management of External Data (SQL/MED)**. PG 於 v9.1 之後實作此規範.

在 SQL/MED 中, 遠端 Server 上的 table 就稱之為 **foreign table**.

PG 的 FDW 就是用來包裝 SQL/MED, 讓使用 **foreign table** 就像是使用本地 table 一樣.

------

如果要使用 FDW, 則需要事先安裝擴充套件(可使用PG 自行維護的 `postgres_fdw`), 並使用像是 `CREATE FOREIGN TABLE`, `CREATE SERVER`, `CREATE USER MAPPING` 等

看起來像是可在本地的 PG, 去查詢別台 Server 的 MySQL, PG, ... (死狗已!!)


## 2. Parallel Query

