# Concurrency Control

- http://www.interdb.jp/pg/pgsql05.html
- 2020/06/11

併發控制, 維持 ACID 之中的 *consistency* && *isolation*

廣為使用的併發技術有三類:
- Multi-version Concurrency Control (MVCC)
  - 任何寫入操作, 都會建立新版本的資料項目(保留舊版本資料)
  - 好處是, readers 及 writers 不會相互 block
  - `PG 及某些 RDBMS` 使用 MVCC 的一種變體, 稱之為 `Snapshot Isolation, SI`
- Strict Two-Phase Locking (S2PL)
  - writer 寫入資料時, 會去取得 *exclusive lock*, 會讓 reader 發生堵塞
- Optimistic Concurrency Control (OCC)


- Oracle 寫入新資料時, 舊版本會先寫入到 rollback segment, 隨後資料會覆蓋掉 data area.
- PG 與 Oracle 類似, 新資料直接寫入 relevant table pae. 讀取時, PG 藉由 **visibility check rules**, 會選擇適當版本的資料來回應特定的 transaction

> SI 不允許 SQL-92 標準裏頭所訂定的3個異常 *Dirty Reads*, *on-Repeatable Reads*, *Phantom Reads*. 但 SI 因允許 *serialization anomalies*, 導致無法達到真正的 serializability.... v9.1 開始, 增加了 *Serializable Snapshot Isolation(SSI)* , 它可 檢測 && 處理 序列化異常. 因而 v9.1 以後, 提供了真正的 serializable isolation level. (SQL Server 也使用 SSI, Oracle 依舊只使用 SI)




# NOTE

- acid: atomicity, consistency, isolation, durability
