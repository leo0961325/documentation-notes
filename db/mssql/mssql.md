


```sql
SELECT * FROM ( 
    SELECT ROW_NUMBER() OVER (
        PARTITION BY [學歷] ORDER BY [經驗] DESC 
    ) AS sn,*
```



```sql
SELECT * FROM ( 
    SELECT ROW_NUMBER() OVER (
        PARTITION BY [學歷] ORDER BY [經驗] DESC 
    ) AS sn,*
    FROM [巨匠職缺].[dbo].[求職者]) AS a
WHERE a.sn=1
```



```sql
SELECT ROW_NUMBER() OVER (
    PARTITION BY [學歷] ORDER BY [經驗] DESC 
) AS sn,*
INTO ##t
FROM [dbo].[求職者]
GO
SELECT * FROM ##t WHERE ##t.sn=1
GO
```



```sql
select *,
    SUM(經驗) over(
        partition by 專長 order by 經驗
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as RunningQty
from [dbo].[求職者]
order by 專長;
```


