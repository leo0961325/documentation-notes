

```sql
CREATE TABLE "demo"."demo" (
  "id" serial4,
  "name" varchar(16),
  "score" int4,
  PRIMARY KEY ("id")
);
```

## json_build_object

- 2019/04/25
- [Return as array of JSON objects in SQL (Postgres)](https://stackoverflow.com/questions/26486784/return-as-array-of-json-objects-in-sql-postgres)

### 1. 測試資料
```sql
-- https://stackoverflow.com/questions/26486784/return-as-array-of-json-objects-in-sql-postgres
Create Table "demo"."jsonbuildobject" (
    "id" serial2,
    "name" varchar(16),
    "city" varchar(16),
    "phone" varchar(16)
);

insert into "demo"."jsonbuildobject" (name, city, phone) values
    (E'andy', E'Taipei', E'0987-222222'),
    (E'tony', E'Taichung', E'0987-333333'),
    (E'chris', E'Tokyo', E'0987-444444'),
    (E'howard', E'Newyork', E'0987-555555'),
    (E'joshua', E'Kaohsiung', E'0987-666666');
```

### - query - json_build_object
```sql
select
    json_agg(json_build_object('city', city, 'phone', phone)) as info
from
    demo.jsonbuildobject
```
```json
[{
    "city": "Taipei",
    "phone": "0987-222222"
},{
    "city": "Taichung",
    "phone": "0987-333333"
},{
    "city": "Tokyo",
    "phone": "0987-444444"
},{
    "city": "Newyork",
    "phone": "0987-555555"
},{
    "city": "Kaohsiung",
    "phone": "0987-666666"
}]
```

### - query - json_build_object

```sql
select
    name, json_agg(json_build_object('city', city, 'phone', phone)) as info
from
    demo.jsonbuildobject
group by
    name;

+----------+------------------------------------------------
| name     | info
+----------+------------------------------------------------
| "andy"   | "[{"city":"Taipei","phone":"0987-222222"}]"
| "tony"   | "[{"city":"Taichung","phone":"0987-333333"}]"
| "chris"  | "[{"city":"Tokyo","phone":"0987-444444"}]"
| "joshua" | "[{"city":"Kaohsiung","phone":"0987-666666"}]"
| "howard" | "[{"city":"Newyork","phone":"0987-555555"}]"
+----------+------------------------------------------------
```


# select all index

```sql
SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'schemaName'
ORDER BY
    tablename,
    indexname;
```