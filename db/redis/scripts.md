# Redis
- 2018/05/11

```sh
# 連到遠端 redis
redis-cli -h <host> -p <port> -a <password>
```

# Native Api
## [data type:](https://redis.io/topics/data-types)
1. [Strings](http://www.runoob.com/redis/redis-strings.html)
2. [Lists](http://www.runoob.com/redis/redis-lists.html)
3. Sets
4. [Hashes](http://www.runoob.com/redis/redis-hashes.html)
5. Sorted sets
6. Bitmaps and HyperLogLogs


## Examples

### 1. [Strings](http://www.runoob.com/redis/redis-strings.html)
```sh
> set a 5
OK
> get a
"5"

# getset key value
> getset db mysql
(nil)
> getset db mongo
"mysql"
> getset db redis
"mongo"
> get db
"redis"

# getrange key start end
> getrange db 0 3
"redi"

# getbit key offset
# (pass)

# mget key [key ...]
> set key1 "hello"
OK
> set key2 "world"
OK
> mget key1 key2 key3
1) "hello"
2) "world"
3) (nil)

# setbit key offset value
# (pass)

# setex key seconds value
# 設定變數存活秒數
# ttl 可以查到還可活多久
> setex mykey 60 redis
OK
> ttl mykey
(integer) 55
> get mykey
"redis"
> ttl mykey
(integer) 46

# setnx key value
# 不存在時, 以唯讀方式寫入(之後無法複寫)
> setnx job "coding"
(integer) 1
> setnx job "accounting"
(integer) 0
> get job
"coding"

# setrange key offset value
# 從第 offset字開始, 覆蓋掉原本的東西
> set key1 "0123456789"
OK
> setrange k 3 xxx
(integer) 10
> get k
"012xxx6789"

# strlen key
# 查字串長度
> set k "0123456789"
OK
> strlen k
(integer) 10
> strlen tony
(integer) 0

# mset key value [key value ...]
# 一次設定多個 key-value
> mset name1 'tony' name2 'tiffany'
OK

# msetnx key value [key value ...]
# 所有 key都設置成功 回傳 1; 反之其一失敗, 則全部 rollback, 回傳 0
> msetnx kk1 v1 kk2 v2
(integer) 1

# psetex key milliseconds value
# 變數存活時間 (多久後到期)
> psetex live_10_seconds 10000 hi
# 10秒後, live_10_seconds 將會變成 (nil)

# pttl key
# 查看 key還可存活多久(毫秒); 已經過期的話, 顯示「(integer) -2」; 可永久存活的變數, 顯示「(integer) -1」
> pttl live_10_seconds
(integer) 5541
> set live_forever 100
OK
> pttl live_forever
(integer) -1

# incr key
# +=1 的概念
> incr x
(integer) 1
> incr x
(integer) 2

# incrby key increment
# 遞增整數
> incrby y 500
(integer) 500

# incrbyfloat key increment - http://www.runoob.com/redis/strings-incrbyfloat.html
# 遞增小數
> incrbyfloat g 5.5
"5.5"

# decr key
# 每次 -1
> decr minus_1
(integer) -1
> decr minus_1
(integer) -2

# decrby key decrement
> decrby minus_me 100
(integer) -100

# append key value
# 對字串作 附加, 回傳子串長度
> append qq 100
(integer) 3
>append qq hi
(integer) 5
> get qq
"100hi"
```


### 2. [Lists](http://www.runoob.com/redis/redis-lists.html)
> list, redis的簡易字串列表, 依照加入順序排序. 可以 加在 最左邊 or 最右邊
```sh
# lpush key value [value ...]
# 加入 value 到 key 的最左邊
> lpush db mysql
(integer) 1
> lpush db mongodb
(integer) 2
> lpush db redis
(integer) 3
> lrange db 0 5
1) "mysql"
2) "mongodb"
3) "redis"

# rpush key value [value ...]
# (同 lpush)

# blpop key [key ...] timeout
# 此指令會 block I/O! 等待 timeout秒. 彈出後, 資料不放回; 取得列表 「第 1 個」
# 時間到後, 拿不到東西則回傳「(nil)」
> blpop db 30
1) "db"
2) "redis"
> lrange db 0 5
1) "mongodb"
2) "mysql"

# brpop key [key ...] timeout
# (同 blpop); 取得列表 「最後一個」

# BRPOPLPUSH SOURCE DESTINATION TIMEOUT
# 從列表中 取出加到另外一個列表(等待 timeout秒)
> b`rpoplpush` msg reciver 500
# 此時, block住了!
# 開另一個 redis-cli
> lpush msg hi
# 原本那個 terminal 就瞬間擷取 msg的 hi, 並且把它 "hi" 加到 reciver. 並顯示等待了 47.04秒
"hi"
(47.04s)
> lrange reciver 0 5
1) "hi"
> lrange msg 0 5
(empty list or set)

# RPOPLPUSH SOURCE DESTINATION
# (同 BRPOPLPUSH), 但馬上執行, 無值顯示 (nil)

# lindex key value
> lpush g1 hello
(integer) 1
> lpush g1 world
(integer) 1
> lrange g1 0 5
1) world
2) hello
> lindex g1 0
"world"
> lindex g1 1
"hello"
> lindex g1 -1
"hello"
> lindex g1 -2
"world"

# linsert key BEFORE|AFTER pivot value
# 把 value 塞到 key 裡的 pivot 前/後
# 成功後回傳 列表長度
# 回傳  0 表示找不到 pivot位置 (插入失敗)
# 回傳 -1 表示找不到  key 或者此 key 為 空列表 (插入失敗)
> rpush uu hello
(integer) 1
> rpush uu world
(integer) 1
> linsert uu before world there
(integer) 3
> lrange uu 0 5
1) "hello"
2) "there"
3) "world"

# llen key
> llen uu
(integer) 3

# lpop key
# 回傳並彈出 key中 第1個
> lpop uu
"hello"

# lpushx key value
# 把值加入到「已存在」列表的第 1個
> lpushx key_that_doesnot_exists 1
(integer) 0
> lpush uu 3
(integer) 3
> lrange uu 0 5
1) "3"
2) "there"
3) "world"

# lrem key count value
# 移除 key中, 與 value相同的值, 移除 count個
# count > 0, 表示從列表 第一個開始找起; count < 0, 表示從列表 最後一個 往前找起; count = 0, 移除全部.
> lpush aa 1 2 3 1 2 3 1 2 3
(integer) 9
> lrem aa -2 1
(integer) 2
> lrange aa 0 -1
1) "3"
2) "2"
3) "1"
4) "3"
5) "2"
6) "3"
7) "2"

# lset key index value
# 利用 index位置, 該 列表內的值
> rpush ss a b c d e
(integer) 5
> lrange ss 0 5
1) "a"
2) "b"
3) "c"
4) "d"
5) "e"
> lset ss 3 xx
OK
> lrange ss 0 5
1) "a"
2) "b"
3) "c"
4) "xx"
5) "e"

# LTRIM KEY START STOP
# 修剪列表, 只保留索引內的範圍
> rpush dd a b c d e f g
(integer) 7
> ltrim dd 2 5
OK
> lrange dd 0 -1
1) "c"
2) "d"
3) "e"
4) "f"

# RPOP KEY
> rpush ff one two three
(integer) 3
127.0.0.1:6379> lrange ff 0 5
1) "one"
2) "two"
3) "three"
127.0.0.1:6379> rpop ff
"three"
> lrange ff 0 5
1) "one"
2) "two"

# RPUSHX KEY VALUE
# 用來把值放到「已存在」的 key 列表最右方(最新一筆)
> rpush yy "A001"
(integer) 1
> rpush yy "A002"
(integer) 2
> rpushx yyyyy "A003"
(integer) 0
> lrange yy 0 -1
1) "A001"
2) "A002"
> lrange yyyyy 0 -1
(empty list or set)
```


### 3. Sets
### 4. [Hashes](http://www.runoob.com/redis/redis-hashes.html)
> String類型的 key-value 映射表. 適合用來儲存 `物件`
```sh
# hmset key field value [field value ...] 
> hmset k1 f1 v1 f2 v2 f3 v3
OK

# hgetall key
> hgetall k1
1) "f1"
2) "v1"
3) "f2"
4) "v2"
5) "f3"
6) "v3"

# hdel key field [field ...]
# 刪除
> hdel k1 f1
(integer) 1
> hgetall k1
1) "f2"
2) "v2"
3) "f3"
4) "v3"

# hexists key value
> hexists k1 f1
(integer) 0
> hexists k1 f2
(integer) 1

# hget key value
> hget k1 f1
(nil)
>hget k1 f2
"v2"

# hincrby key field increment
# 同 incrby

# hincrbyfloat key field increment
# 同 incrbyfloat

# hkeys key
# 查看 hash key中所有 keys
> hset kk f1 v1
OK
> hset kk f2 v2
OK
> hkeys kk 
1) "ff"
2) "f1"
3) "f2"

# hlen key
> hlen kk
(integer) 3

# hmget key field [field ...]
> hmget kk f1 f2 f3
1) "v1"
2) "v2"
3) (nil)

# hmset key field value [key value ...]
> hmset qq f1 hi f2 hello f3 bye
1) "hi"
2) "hello"
3) "bye"

# hsetnx key field value
# (同 setnx)

# hvals key
> hgetall my
1) "f1"
2) "foo"
3) "f2"
4) "bar"
> hvals my
1) "foo"
2) "bar"

# hscan key cursor  [MATCH pattern] [COUNT count]
# 沒範例...
```


### 5. Sorted sets

### 6. Bitmaps and HyperLogLogs




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