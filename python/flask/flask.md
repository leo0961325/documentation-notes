# Python Flask
- 2018/02/17


## 一些不錯的文章 (新手不宜)
- [Flask0.1源码阅读——请求处理和响应](https://jiayi.space/post/flask0.1yuan-ma-yue-du-qing-qiu-chu-li-he-xiang-ying)
- [Flask 的 Context 机制](https://blog.tonyseek.com/post/the-context-mechanism-of-flask/)
- 2018/05/30


#### SQLAlchemy column types
Type name | Python type
--- | ---
Integer | int
SmallInteger | int
BigInteger | int
Float | float
Numberic | decimal.Decimal
String | str
Text | str
Unicoe | unicode
UnicodeText | unicode
Boolean | bool
Date | datetime.date
Time | datetime.time
DateTime | datetime.datetime
Interval | datetime.timedelta
Enum | str
PickleType | Any Python Object
LargeBinary | str

#### SQLAlchemy column options
Option name | Description
--- | ---
primary_key | bool
unique | bool
index | bool
unllable | bool
default | default value

#### SQLAlchemy relationship options
Option name | Description
--- | ---
backref | 
primaryjoin | 
lazy | 
uselist | 
order_by | 
secondary | 
secondaryjoin | 