# Query

- 2020/06/04
- [Query Processing](http://www.interdb.jp/pg/pgsql03.html)
- [PG官網寫的Query](https://www.postgresql.org/docs/11/overview.html)

關於 Query, PG 提供了 3 種有趣的技術:

- [Foreign Data Wrappers(FDW)](https://www.postgresql.org/docs/11/fdwhandler.html)
- [Parallel Query](https://www.postgresql.org/docs/11/parallel-query.html)
- [JIT compilation](https://www.postgresql.org/docs/11/jit-reason.html)


## 1. Overview

PG 收到 SQL statement 後, 會在 backend process 進行下列流程:

- Parser   : 從 SQL 查詢字串, 生成 `parse tree`
- Analyzer : 針對 `parse tree` 進行語意分析, 而後生成 `query tree`
- Rewriter : 將 `query tree` 的規則, 拿 [rule system](https://www.postgresql.org/docs/11/rules.html) 內的規則來比對, 若有此規則, 則轉換 `query tree`
- Planner  : 由 `query tree` 產生一個執行上最有效率的 plan tree
- Executor : 依照 plan tree 指示, 依序到 tables && indexes 去執行 query


## 1-1. Parser

從底下的 SQL Statement 為出發點

```sql
SELECT id, data FROM tbl_a WHERE id < 300 ORDER BY data;
```

`Parse Tree` 根節點為 `SelectStmt`



## 2.
