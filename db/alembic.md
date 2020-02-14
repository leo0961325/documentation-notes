# alembic



## basic

- 2019/08/14
- https://michaelheap.com/alembic-python-migrations-quick-start/

```bash
### 虛擬環境底下
$# pip install mysqlclient      # 若無法解決, 參考 DBApi 那篇
$# pip install alembic
$# alembic init <alembic name>
# 產生如下
/alembic
    /__pycache__
    /env.py
    /README
    /script.py.mako
    /versions
/alembic.ini

$# vim alembic.ini
# 修改裏頭的 sqlalchemy.url 部分, 定義好 DB 連線

$# alembic revision -m "meaningful operation name"
# 會產生
/alembic/versions/68ff4441380d_meaningful_operation_name.py
# 其中, 裏頭的 upgrade && downgrade 需要是
# 操作完其中一者後, 另一者可以把它復原
# ex: upgrade 用來 create table, 則 downgrade 需要作 drop table

### DB 依照 alembic file 升級至 最新版
$# alembic upgrade head
INFO  [alembic.migration] Context impl MySQLImpl.
INFO  [alembic.migration] Will assume non-transactional DDL.
INFO  [alembic.migration] Running upgrade None -> 469d90f0cd28, Create users table

### DB 依照 alembic file 降一版
$# alembic downgrade -1

### DB 依照 alembic file 降至最初始版本
$# alembic downgrade base

### 查看目前 DB 版本
$# alembic current
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

```
