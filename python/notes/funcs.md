# 一些有趣的函數

[maketrans](http://www.pythonchallenge.com/pc/def/map.html)
```py
# 快速把 abc...wxyz -> cde...yzab
a="hi"
trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print(a.translate(trans))
# jk
```