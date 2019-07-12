# Python Database API (DBAPI) 2.0
- 2018/06/21
- [PEP249 -- Python Database API Specification v2.0](https://www.python.org/dev/peps/pep-0249/)
- [MySQL DB API Drivers](https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-db-api-drivers)
- [PyMySQL vs MySQLdb](https://stackoverflow.com/questions/7224807/what-is-pymysql-and-how-does-it-differ-from-mysqldb-can-it-affect-django-deploy)
- [Django db使用MySQL连接池](https://zhu327.github.io/2016/09/25/django-db%E4%BD%BF%E7%94%A8mysql%E8%BF%9E%E6%8E%A5%E6%B1%A0/)



Python標準程式庫沒有內附 RDBMS介面, 而廣為使用的第三方模組 多半遵循 Python Database API 2.0標準 (PEP249)



```py
import <DBAPI相容性模組>

# conn 為 Connection 實例, 代表對 DB 的連線
conn = <DBAPI相容性模組>.connect(<必要參數>)

# Connection 的 4種方法
conn.close()       # Close Connection
conn.commit()      # Commit
conn.rollback()    # Rollback
c = conn.cursor()  # 取得 Cursor

c.DB方法()  
c.DB屬性

# c.execute(<SQL Statement>)
c.execute( ... )
            ↑
        不建議使用 「'select * from tbl where col2={!r}'.format(x)」這類的寫法
        => 慢 不安全(SQL Injection問題)

        改用「'select * from tbl where col2=?', (some_value,)」
```

## [MySQL DB API Drivers](https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-db-api-drivers)

1. MySQLdb

    Python3以上不支援此 Native Driver

2. mysqlclient

    從 MySQLdb 抄過來的東西 (支援 Python3)
    Django 1.11官網建議用這個 Driver.

3. MySQL Connector/Python

- Oracle 發行的 Pure Python Driver ; 此 Driver **不依賴** `Python標準函式庫以外的模組` 及 `MySQL client library`
- [MySQL 官網](https://dev.mysql.com/downloads/connector/python/) 強烈建議 MySQL 5.5, 5.6, 5.7, 8.0 搭配使用 `MySQL Connector/Python 8.0`
- `pip install mysql-connector-python` (這東西依賴於 [Microsoft Visual C++ 2015 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=52685))

----------

Django 有為 `MySQLdb` 及 `mysqlclient` 配置 adapter ; 而 `MySQL Connector/Python` 有自己的 adapter