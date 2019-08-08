# [Data Types](https://redis.io/topics/data-types)
- 2018/05/11

```sh
# 連到遠端 redis
redis-cli -h <host> -p <port> -a <password>
```

Native Data Type 分為底下 6 類

1. Strings
2. Lists
3. Sets
4. Hashes
5. Sorted sets
6. Bitmaps and HyperLogLogs


# python-redis
- [redis.Redis 與 redis.StrictRedis](https://my.oschina.net/paiooo/blog/717705)

```py
>>> import redis
>>> r = redis.StrictRedis(host='localhost', port=6379, db=0)
# a="Hello", 存活10秒鐘
>>> r.setex('a',10,"Hello")
```

```py
# 設定 kk, 其值為10, 分數為 20
>>> zadd('kk', 10, 20)
1

>>> r.zrange('kk', 0, 5)
['20']

>>> r.zrange('kk', 0, 5,withscores=True)
[('20', 10.0)]
```