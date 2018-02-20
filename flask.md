# Python Flask
- 2018/02/17

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