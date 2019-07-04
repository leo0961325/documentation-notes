


```bash
### 使用 doctest 這模組(or套件) 執行 abc.py, 並列出詳細執行情況
python -m doctest -v abc.py
```



Python中, 任何資料夾內如果有包含`__init__.py`的話, 這個資料夾就被視為是一個`package`, 如此一來就可以被 import


---

# shebang
```py
#! /usr/bin/python
# coding: utf-8

```


# 函式範例
```py
>>> a = 1
>>> type(a)
<class 'int'>
>>>
>>> isinstance(a, int)
True

>>> dict.fromkeys('hello', 2)
{'h': 2, 'e': 2, 'l': 2, 'o': 2}

>>>
```

# configureParser

- configureParser.py
```py
import configparser

# 讀取外部組態檔
def getConfig(iniPath):
    config = configparser.ConfigParser()
    config.read(iniPath)
    dbhost = config.get('Section_A', 'sql_dbhost')
    user = config.get('Section_A', 'sql_id')
    passwd = config.get('Section_A', 'sql_pd')
    return dbhost, user, passwd
#

def mainFunction():
    iniPath = './house.ini'
    dbhost, user, passwd = getConfig(iniPath)
#
```

- house.ini
```ini
[Section_A]
sql_dbhost=localhost
sql_pport=3306
sql_id=tony
sql_pd=12345687


[Section_B]
# 放其他的...
```

# 環境變數

```py
import os
os.environ['PATH']
```

# metaclass

- 2019/07/03
- [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)

- object 為 class     的 instance
- class  為 metaclass 的 instance

> `type` is the usual metaclass in python, `type` is itself a class, and it is its own type.

---

- 鴨子定型: duck typing
- 鵝定型法: goose typing (Python技術手冊 3ed p233)
-