
- 2020/03/27
- [docker-gitea](https://hub.docker.com/r/gitea/gitea/)
- [git-gitea](https://github.com/go-gitea/gitea)


```bash
###
$# docker pull gitea/gitea:latest


### 測試
$# docker run --rm \
    --name mygitea \
    -p 10022:22 \
    -p 10080:3000 \
    gitea/gitea:latest


### 正式
$# docker run -d \
    --name mygitea \
    -p 10022:22 \
    -p 10080:3000 \
    -v /Users/tony/docker_data/mygitea:/data \
    gitea/gitea:latest

### http://localhost:10080
# 隨便註冊吧
# id: tony@localhost.com
# pd: 1qaz@WSX
# 2020/02/15 的現在, 不知為啥的常常跟我說錯誤但其實是註冊成功...

```


### 測試備註

id: work_id
pd: 1qaz@WSX
