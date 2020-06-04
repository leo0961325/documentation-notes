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


### 1-1. Parser

從底下的 SQL Statement 為出發點

```sql
SELECT id, data FROM tbl_a WHERE id < 300 ORDER BY data;
```

`Parse Tree` 根節點為 `SelectStmt`

此步驟將只會檢查 語法上有無錯誤, 並不做 欄位有無存在 等等的驗證


### 1-2. Analyzer

依據 Parser 所建立的 Parse Tree 執行語意分析, 並且建立 `Query Tree`

Query Tree 根節點為 `Query`, 裏頭的元素節點就例如 `SELECT`, `INSERT`

底下記錄一些 [Query Tree](https://www.postgresql.org/docs/11/querytree.html) 的(今天寫明天忘 && 似乎對我來說一點都不重要的)東西

> The rule system is located between the parser and the planner.
  如果要查看 `Query Tree` 的創建過程, 可以修改 `debug_print_parse`, `debug_print_rewritten`, `debug_print_plan` 這幾個組態. 
  而所謂 Query Tree, 其實只是 SQL statement 的內部表達形式.


#### Query 的組成成分:

- command type : SELECT, INSERT, UPDATE, DELETE
- range table : 以 SELECT 來說的話, range table 就是 FROM 之後的那些 關鍵字們
- result relation
- target list
- qualification
- join tree
- others

### 1-3. Rewriter

rule system(query rewrite system)

舉例來說, `Views` (CREATE VIEW ...) 就是被 rule system 來實作, 相關的規則會被自動建立 && 紀錄在 `pg_rules` 這個 catalog

```sql
-- CREATE VIEW ...
CREATE VIEW vvemployees AS SELECT e.id, e.name, d.name AS department FROM employees AS e departments AS d WHERE e.dept_id = d.id;

-- 此動作, 查詢此 VIEW 的動作, 會建立一個新的 Query Tree
SELECT * FROM vvemployees;
```

### 1-4. Planner && Executor

可使用 `EXPLAIN` 來查看 `Plan Tree`

Planner(RDBMS 裏頭最為複雜的子系統) 接收 `Query Tree` 並產生 `(Query) Plan Tree`, 這東西可以很有效率地被後續的 `Executor` 執行

PG 的 Planner 只是單純的依據 cost-base 做最佳化, 不支援 rule-base, hints-base 最佳化

```sql
-- 可使用 EXPLAIN 來查看 Plan Tree
EXPLAIN SELECT * FROM tbl WHERE id < 30 ORDER BY data;
```

EXECUTOR 處理 query 時會使用到一些記憶體區域: `temp_buffs` && `work_mem` 並在必要時刻建立 temporary files. 最終要存取 tuples 的時候, PG 使用 `Concurreycy Control` 機制來維持 **consistency** 及 **isolation**


## 2. 單表查詢的成本估計


### 2-1. 循序查詢 (Table Scan, Sequential Scan)


### 2-2. Index Scan


### 2-3. Sort


## 3. 單表查詢的 Plan Tree


## 4. Executor Performs


## 5. Join

### 5-1. Nested Join

### 5-2. Merge Join

### 5-3. Hash Join

### 5-4. Join Access Paths && Join Nodes

## 6. 多表查詢的 Plan Tree


### 6-1. Preprocessing

### 6-2. Getting the Cheapest Path

### 6-3. Getting the Cheapest Path (三表查詢)

