# pymongo

```sh
$ pip freeze | grep pymongo
pymongo==3.5.1
```

```py
>>> a = datetime.datetime.utcnow()
>>> a
datetime.datetime(2017, 11, 30, 7, 55, 57, 756000)

# 塞到 MongoDB後
>>> insert({ 'dt': a })
```

```mongo
ISODate("2017-11-30T07:55:57.756Z")
```