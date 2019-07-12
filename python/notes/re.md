# regex

regex 有兩種方式, 在 一大堆字當中, 尋找模式
1. 匹配 (match)     : `起始為` ... 才算
2. 搜尋 (search)    : 只要文字當中 `含有` ... 就算


```py
import re
r = re.compile(r'[0-9]+')        # 解析準則
mo = r.search('hello^^123')
print(mo.group())
# '123'
```