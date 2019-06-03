# PostgreSQL 9.5

- 2019/01/28
- [學習資源](https://www.youtube.com/playlist?list=PLliocbKHJNws0zsx5Akn1DVoPznFYYGA9)
- On Ubuntu 16.04

### Install

```sh
$# apt install -y postgresql

$# psql --version
psql (PostgreSQL) 9.5.14

$# apt-get -y update
$# apt-get install -y nmap

### Port 掃描
$# nmap 127.0.0.1

Starting Nmap 7.01 ( https://nmap.org ) at 2019-01-28 02:41 CST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000030s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
631/tcp  open  ipp
5432/tcp open  postgresql

Nmap done: 1 IP address (1 host up) scanned in 1.66 seconds
```

### Usa Postgresql

#### 1. Operate DB

```sh
### 切換 postgresql 使用者~
$# sudo -i -u postgres

### 切換登入目錄
$# pwd
/var/lib/postgresql

### 目前已有哪些 Database
$# psql -l
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
$# createdb tonydb      # (沒有提示QQ...)
# /bin/bash

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

tonydb=# select version();
                                                      version
-------------------------------------------------------------------------------------------------------------------
 PostgreSQL 9.5.14 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609, 64-bit
(1 row)

### 離開 DB
tonydb=# \q

### 刪除 DB
$# dropdb tonydb    # (沒有提示QQ...)
```

#### 2. Operate Table

```sh
$# createdb tonydb

$# psql tonydb
# 底下命令提示字元懶得換了... (tonydb=# -> $#)

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
$# \du

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
$# create table users (id serial primary key, name varchar(16));
CREATE TABLE

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

