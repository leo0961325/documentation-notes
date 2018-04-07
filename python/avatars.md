# 頭像
[Gravatar](https://en.gravatar.com/)
[python gravatar](https://en.gravatar.com/site/implement/images/python/)

- 2018/04/07
- 好像行不通...

URL如下:
1. http://www.gravatar.com/avatar/\<hash>
2. https://secure.gravatar.com/avatar/\<hash>

```py
>>> import hashlib

>>> hashlib.md5('l26884133@yahoo.com.tw'.encode('utf8')).hexdigest()
'f0ec92d88cb3fe0da8b275fae75358b9'
```


