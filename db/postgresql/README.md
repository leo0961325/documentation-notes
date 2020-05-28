# PostgreSQL

- [PostgreSQL 11 - 官方](https://www.postgresql.org/docs/current/tutorial.html)

### Usa Postgresql

#### 1. Operate DB

```sh
### 目前已有哪些 Database
postgres@docker:/root$ psql -l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)

### Create DB


### 進入 DB
$# psql tonydb
# /bin/bash, 執行後進入 psql
```

```sh
tonydb=# select now();
              now
-------------------------------
 2019-01-28 09:51:34.726395+08
(1 row)

### Ubuntu16.04 LocalVM
tonydb=# select version();
                                                      version
-------------------------------------------------------------------------------------------------------------------
 PostgreSQL 9.5.14 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609, 64-bit
(1 row)

### AWS-RDS-Postgres
tony=> select version();
                                                version
--------------------------------------------------------------------------------------------------------
 PostgreSQL 11.2 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.3 20140911 (Red Hat 4.8.3-9), 64-bit
(1 row)

### 離開 DB
tonydb=# \q

### 刪除 DB
$# dropdb tonydb    # (沒有提示QQ...)
```

#### 2. Operate Table

```sh

$# create table posts (title varchar(255), content text);
CREATE TABLE

### 查看 posts 這個 Table 的欄位
$# \d posts
             Table "public.posts"
 Column  |          Type          | Modifiers
---------+------------------------+-----------
 title   | character varying(255) |
 content | text                   |

### 查看 DB 內 Tables 的資訊
$# \dt
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | posts | table | postgres
(1 row)

### rename
$# alter table posts rename to post1;
ALTER TABLE

$# \dt
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | post1 | table | postgres
#         ↑↑↑↑↑ 已改名

### 刪除 Table
$# drop table post1;
DROP TABLE

### 離開 psql
$# \q

### 建立外部文件
$# vim db.sql
Create Table posts (
    title varchar(255),
    content text
);

### 查看所有 users
postgres=$# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

### 查看所有 users
$# SELECT u.usename AS "User name",
  u.usesysid AS "User ID",
  CASE WHEN u.usesuper AND u.usecreatedb THEN CAST('superuser, create
database' AS pg_catalog.text)
       WHEN u.usesuper THEN CAST('superuser' AS pg_catalog.text)
       WHEN u.usecreatedb THEN CAST('create database' AS
pg_catalog.text)
       ELSE CAST('' AS pg_catalog.text)
  END AS "Attributes"
FROM pg_catalog.pg_user u
ORDER BY 1;

### 使用外部腳本建立 Table
$# psql tonydb
$# \i db.sql        # 使用外部 sql 腳本
CREATE TABLE

$# \d posts
             Table "public.posts"
 Column  |          Type          | Modifiers
---------+------------------------+-----------
 title   | character varying(255) |
 content | text                   |
```

#### 3. Constraints

```sql
-- 這東西儲存到 /var/lib/postgresql/db2.sql
Create Table posts (
    id          serial  primary key,
    title       varchar(255) not null,
    content     text    check(length(content) > 12),
    is_draft    boolean default TRUE,
    is_del      boolean default FALSE,
    post_date   timestamp   default 'now'
);

-- check: 建立時的檢查條件
```

使用~

```sh
### postgres
$# psql tonydb

### 先刪除之前的 posts Table, 在建立 Table
$# \i db2.sql
CREATE TABLE

### 建立 Table 完成~ 查看細節
$# \d posts
                                            Table "public.posts"
  Column   |            Type             |                             Modifiers
-----------+-----------------------------+-------------------------------------------------------------------
 id        | integer                     | not null default nextval('posts_id_seq'::regclass)
 title     | character varying(255)      | not null
 content   | text                        |
 is_draft  | boolean                     | default true
 is_del    | boolean                     | default false
 post_date | timestamp without time zone | default '2019-01-28 03:22:30.248251'::timestamp without time zone
Indexes:
    "posts_pkey" PRIMARY KEY, btree (id)
Check constraints:
    "posts_content_check" CHECK (length(content) > 12)
```

#### 4. Datatype

- [PostgreSQL 9.5 - Datatype](https://www.postgresql.org/docs/9.5/datatype.html)

#### 5. CRUD

```sh
### psql tonydb
#@@ insert
$# insert into posts (title, content) values ('title1', 'content1...@@ need 12 words...');
INSERT 0 1

#@@ select
$# select * from posts;
 id | title  |            content             | is_draft | is_del |         post_date
----+--------+--------------------------------+----------+--------+----------------------------
  2 | title1 | content1...@@ need 12 words... | t        | f      | 2019-01-28 03:22:30.248251
# ↑ 第一次插入失敗... 然後再次插入一筆時, id 會自己跳過@@!

#@@ 讓 select 結果, 使用 橫向/縱向 顯示
$# \x
Expanded display is on.
# (底下不做示範, 感覺沒必要, 除非字非常長~, 會換行再用吧)

#@@ update
$# update posts set content = 'fixfixfixfixfixfix~~~' where id = 2;
UPDATE 1

#@@ delete
$# delete from posts where id = 4;
DELETE 1
```

#### 6. DDL

```sh
### psql tonydb
$#

### 增加欄位
$# alter table users add fullname varchar(255);
ALTER TABLE

### 刪除欄位
$# alter table users drop fullname;
ALTER TABLE

### 修改欄位
$# alter table users alter name type varchar(32);
ALTER TABLE

### 建立 index
$# create index idx_name on users(name);
CREATE INDEX
$# \d users;
# (...前半部省略...)
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "idx_name" btree (name)     # <--- 新建立的 Index (btree)

### 刪除 index
$# drop index idx_name;
```


- [2019/1/28 進度 - 13/16](https://www.youtube.com/watch?v=QtXqViS1OU8&list=PLliocbKHJNws0zsx5Akn1DVoPznFYYGA9&index=14)


# psql Command Line

- [postgres-cheatsheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)


## Part 1 - 基本操作

```bash
### 進入 psql(法一)
$# psql -U postgres
postgres=$#         # DONE

### 進入 psql(法二)
$# su postgres
$# psql
postgres=$#         # DONE

### 離開 postgres
postgres=$# \q

### 建立 tonydb Database
postgres=$# createdb tonydb

### 使用 DB
postgres=$# psql tonydb
postgres-$#                 # 命令提示字有變化喔!

### 列出DB(法一)
postgres=$# psql -l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 tonydb    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
(4 rows)

### 列出DB(法二)
postgres=$# \l

### 查看連線的 DB && 目前使用者
postgres=$# \c
You are now connected to database "postgres" as user "postgres".

### 切換資料庫; 連線到資料庫
postgres=$# \connect python_quiz  # 或是 \c python_quiz
You are now connected to database "python_quiz" as user "postgres".
python_quiz=$#    # DONE (切換到 python_quiz 了~)


### 列出 Schema (無法在外部使用 「psql \dn」)
postgres=$# \dn
  List of schemas
  Name    |  Owner
----------+----------
 newcomer | postgres
 public   | postgres
(2 row)

### 列出 indexes
postgres=$# \di
Did not find any relations.

### 列出目前使用者
postgres=$# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}


### 列出 newcomer 這個 Schema 底下所有 table
python_quiz=$# \dt newcomer.*
           List of relations
  Schema  |  Name   | Type  |  Owner
----------+---------+-------+----------
 newcomer | example | table | postgres
(1 row)
# DONE

###
python_quiz=$#
```

## Part2 - DDL

```bash
### 建立 Table - users
tonydb-$# CREATE TABLE users (
tonydb($#   id SERIAL PRIMARY KEY,
tonydb($#   name VARCHAR(16)
tonydb($# );
CREATE TABLE

### 查看 Table - users
tonydb-$# \d users
                                   Table "public.users"
 Column |         Type          | Collation | Nullable |              Default
--------+-----------------------+-----------+----------+-----------------------------------
 id     | integer               |           | not null | nextval('users_id_seq'::regclass)
 name   | character varying(16) |           |          |
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)

### 查看所有 Tables     (等同 MySQL : 「Show Tables;」)
tonydb-$# \d
              List of relations
 Schema |     Name     |   Type   |  Owner
--------+--------------+----------+----------
 public | users        | table    | postgres
 public | users_id_seq | sequence | postgres
(2 rows)

###
```

## Part3 - DML

```bash
### 大量 Insert 到 weather Table, 資料來自 ...
tonydb-$# COPY weather FROM '/home/user/weather.txt';
```


# AUTO_INCREMENT

欄位設定方式:

```sql
-- SQL 寫法
  "COLUMNNAME" int4 NOT NULL DEFAULT nextval('"SCHEMA".seq_COLUMNNAME'::regclass),  -- 似乎無法執行...
  -- OR
  "COLUMNNAME" SERIAL,
```

```py
### SQA 寫法
  sa.Column('COLUMNNAME', sa.Integer(), server_default=sa.text("nextval('SCHEMA.seq_COLUMNNAME')"), nullable=False, comment='auto_increment'),
```


# CLI

```bash
### postgres admin USER 才可使用
$# /usr/lib/postgresql/11/bin/pg_ctl reload
# reload config
```



# Trigger

- 2020/05/28
- [Creating a Trigger in PostgreSQL](https://www.postgresqltutorial.com/creating-first-trigger-postgresql/)

Postgres 上, 若要建立 trigger, 需要分成 2 個步驟:

## 1. 建立 trigger function

trigger function 本身不接收參數, 並且會回傳一個 trigger 類別的值

建立 trigger function 時, 可使用任意 postgreSQL 支援的語言, PL/pgSQL 為其中一種

> A trigger function receives data about its calling environment through a special structure called TriggerData, which contains a set of *local variables*. For example, `OLD` and `NEW` represent the **states of the row in the table before or after the triggering event**.
> PostgreSQL provides other *local variables* starting with `TG_` as the prefix such as TG_WHEN, and TG_TABLE_NAME.
> Once you define a trigger function, you can bind it to one or more trigger events such as INSERT, UPDATE, and DELETE.

PostgreSQL 提共 2 種類型的 triggers:

1. row-level trigger **FOR EACH ROW**
2. statement-level trigger **FOR EACH STATEMENT**

> 兩種類型 triggers 的差異: The differences between the two kinds are how many times the trigger is invoked and at what time. For example, if you issue an UPDATE statement that affects 20 rows, the row-level trigger will be invoked 20 times, while the statement level trigger will be invoked 1 time.

```sql
CREATE FUNCTION trig_func()
  RETURNS trigger AS ...
```


## 2. 建立 trigger, 並把它綁訂到 trigger function

```sql
DROP TRIGGER IF EXISTS "trigger_name" ON "table-name";
CREATE TRIGGER "trigger_name" 
  {BEFORE | AFTER | INSTEAD OF} {event [OR ...]}
  ON "table-name"
    [FOR [EACH] {ROW | STATEMENT}]
        EXECUTE PROCEDURE trig_func()
```