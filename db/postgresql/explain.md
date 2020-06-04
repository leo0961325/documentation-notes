## EXPLAIN (有無使用 index 做 where 搜尋)

```sql
-- Table 裡面資料量 14998 筆
EXPLAIN SELECT * FROM ip_location WHERE routing_ip_number = 193180913;
EXPLAIN ANALYSE SELECT * FROM ip_location WHERE routing_ip_number = 193180913;

-- 情境1. 有 Index(routing_ip_number) 的情況
Index Scan using ix_ip_location_routing_ip_number on ip_location  (cost=0.29..8.30 rows=1 width=52)
  Index Cond: (routing_ip_number = 193180913)

-- 情境2. 無 Index 的情況
Seq Scan on jkb_cache_ip_location  (cost=0.00..297.38 rows=1 width=52)
  Filter: (routing_ip_number = 193180913)

Seq Scan on jkb_cache_ip_location  (cost=0.00..297.38 rows=1 width=52) (actual time=0.024..3.450 rows=1 loops=1)
  Filter: (routing_ip_number = 193180913)
  Rows Removed by Filter: 14998
Planning Time: 0.088 ms
Execution Time: 3.472 ms

-- 說明:
使用 Table Scan, 循序搜尋
cost=0.00..297.38 rows=1 width=52
     AAAA  BBBBBB      C       DD
    A: 估計的啟動成本
    B: 估計總成本
    C: 此計劃節點輸出的估計資料列數量
    D: 此計劃節點輸出的資料列估計的平均資料大小
```

