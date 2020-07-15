
## Higher-Order Functions 高階函式

若 functionA 接收 functionB 當成參數, 或者 functionA 會回傳一個 functionB, 則 functionA 稱為 高階函式. ex: sorted, map, filter, reduce



## `map(func, iterable)`

接收兩個參數, 會將第二個參數(iterable), 逐一丟到 func 裏頭, 最終會回傳一個 

```py
from typing import Iterable
def factional(n):
    return 1 if n < 2 else n * factional(n-1)

ff = factional
mm = map(factional, range(6))  # <map object at 0x0000022AC6C78908>
list(mm)  # [1, 1, 2, 6, 24, 120]
isinstance(mm, Iterable)  # True
```


## `all(iterable)`
- 若 iterable 全為 True, 則為 True



## `any(iterable)`
- 若 iterable 其一為 True, 則為 True

