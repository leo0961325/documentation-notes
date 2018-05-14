# 資料庫連線相關
- 2018/05/14

## sqlite

```py
"""
    回傳的 c 及 r 都是 <sqlite3.Cursor object>
    取dir後有 ['arraysize', 'close', 'connection', 'description', 'execute', 'executemany', 'executescript', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid', 'row_factory', 'rowcount', 'setinputsizes', 'setoutputsize']
    r無論是select, insert都是回傳 cursor
"""
import sqlite3
try:
    with sqlite3.connect('db.sqlite') as conn:
        c = conn.cursor()
        r = c.execute(""" CREATE TABLE messages (
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            msg TEXT NOT NULL
        )""")
finally:
    conn.close()
```


## pymysql

```py
"""
    c 為<pymysql.cursors.Cursor object>, 具有以下屬性 ['arraysize', 'callproc', 'close', 'connection', 'description', 'execute', 'executemany', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid', 'max_stmt_length', 'mogrify', 'nextset', 'rowcount', 'rownumber', 'scroll', 'setinputsizes', 'setoutputsizes']
"""
import pymysql
config = {
    'host' : 'localhost',
    'user' : 'user01',
    'password' : 'user01',
    'db': 'test',
    'port' : 3306,
    'charset' : 'utf8'
}
conn = pymysql.connect(**config)
with conn.cursor() as c:
    c.execute("select * from roles;")
    conn.commit()   # 記得commit! 記得commit! 記得commit!
```