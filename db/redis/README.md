# redis

- [官方](https://redis.io/topics/quickstart)
- [官方Config](https://redis.io/topics/config)
- [官方cli](https://redis.io/topics/rediscli)
- [Redis bind IP](https://dotblogs.com.tw/colinlin/2017/06/26/150257)
- [Flask SSE官方 - redis](http://flask-sse.readthedocs.io/en/latest/quickstart.html)


### 跨 Host使用 redis
- 更改組態裏頭的 config的 bind
```conf
# bind 127.0.0.1
bind 0.0.0.0
```