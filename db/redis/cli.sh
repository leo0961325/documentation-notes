

REDIS_PASSWORD=

### 看 redis 連線狀況
redis-cli -a {REDIS_PASSWORD} --stat

### 列出所有 'server-*' 的 keys
redis-cli -a {REDIS_PASSWORD} keys server-*
