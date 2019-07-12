# 基礎 python
- 2018/04

```py
isinstance(obj, type)

>>> a = 0b010
>>> a
2


>>> a = 0o010
>>> a
8

>>> a = 0x010
>>> a
16
```


> \_\_init__, 念法: `dunder init`


```py
__class__(self)
回傳自己的類別
```

```py
__qq
私有變數 qq


_qq
範疇內的私有名稱(僅慣例, Python compilor沒要求)
```

# *args 與 **params

## 1. *args 用法

args : 可以是 `list` 及 `tuple`

```py
a = [1, 2, 3]
b = (5, 6, 7)

def ss(*nums):
    tt = 0
    for i in nums:
        tt += i
    return tt

ss(*a)
ss(*b)
```

## 2. **params 用法

params : 只可以是 `dict`

```py
a = {'name': 'tony', 'age': 18}

def pp(**params):
    print(params)

pp(**a)
```


# [base64](https://docs.python.org/3.6/library/base64.html)

```py
>>> import base64
>>> s='tony:password123'.encode()
>>>
>>> q = base64.b64encode(s)
>>> q
b'dG9ueTpwYXNzd29yZDEyMw=='
>>>
>>> base64.b64decode(q)
b'tony:password123'
```
