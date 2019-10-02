# redis

- [官方](https://redis.io/topics/quickstart)
- [官方Config](https://redis.io/topics/config)
- [官方cli](https://redis.io/topics/rediscli)
- [Redis bind IP](https://dotblogs.com.tw/colinlin/2017/06/26/150257)
- [Flask SSE官方 - redis](http://flask-sse.readthedocs.io/en/latest/quickstart.html)

# login

密碼登入

```bash
$# redis-cli -h <HOST> -p <PORT> -a
<PASSWORD>
```



### 跨 Host使用 redis
- 更改組態裏頭的 config的 bind
```conf
# bind 127.0.0.1
bind 0.0.0.0
```


# Redis-GUI

參考 [redis-desktop-manager](https://redisdesktop.com/pricing)


# Redis-CLI

```bash
### Usage
# redis-cli -h <HOST> -p <PORT> -a <PASSWORD>

### 查看 目前狀態
$# redis-cli --stat
------- data ------ --------------------- load -------------------- - child -
keys       mem      clients blocked requests            connections
41         1.46M    29      0       778682 (+0)         2054
41         1.46M    29      0       778683 (+1)         2054
41         1.46M    29      0       778684 (+1)         2054
# 以上, 每秒鐘會跳一個

### 列出所有 keys
$# keys '*'
```