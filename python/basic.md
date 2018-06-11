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
__init__(self)
類別實體化後執行

__get__(self)
類別內, 若有定義這個, 則稱此類別為 "描述器(descriptor)"

__set__(self)
類別內, 若有定義這個, 則稱此類別為 "覆寫式描述器(overriding descriptor)"


__setattr__(self)


__class__(self)
回傳自己的類別


__dict__(self)
其他屬性映射, 回傳 dictionary


__get__(self) 卻沒 __set__(self)
稱為 "非覆寫式描述器"


__doc__(self)
抓出 string literal, """(這裡的東西)"""

__name__(self)
抓出 className



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