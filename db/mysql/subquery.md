# subquery 效能
- 2018/05/11



## Question: 查 order資料表內，最近與我下單的所有客戶

### 1. Correlated subqueries 效能差
```sql
SELECT custid, ordid, orderdate
FROM ord o
WHERE orderdate = 
    (
        SELECT MAX(orderdate) 
        FROM ord i
        WHERE i.custid = o.custid
    )
ORDER BY custid;
```



### 2.1. Subquery + Join方法 改寫
> SELF-contained + Join

```sql
SELECT o.custid, o.ordid, o.orderdate
FROM ord o JOIN (
        SELECT custid, MAX(orderdate) LastOrder
        FROM ord 
        GROUP BY custid
    ) i 
    ON (o.custid = i.custid)
WHERE o.orderdate = i.LastOrder
ORDER BY custid;
```



### 2.2. Subquery + Join方法 改寫
> SELF-contained + Join

```sql
SELECT o.custid, o.ordid, o.orderdate
FROM ord o JOIN (
        SELECT custid, MAX(orderdate) LastOrder
        FROM ord 
        GROUP BY custid
    ) i 
    ON (o.custid = i.custid AND o.orderdate = i.LastOrder)
ORDER BY custid;
```



### 3. Table-valued Subquery
> Self-Subquery

> Oracle、MySQL5.6後可，但是SQL Server無法下multi-column subquery (相容性較差)

```sql
SELECT custid, ordid, orderdate
FROM ord
WHERE (custid, orderdate) in (
        SELECT custid, MAX(orderdate)
        FROM ord
        group by custid
    )
ORDER BY custid;
```