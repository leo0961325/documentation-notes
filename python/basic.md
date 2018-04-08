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
