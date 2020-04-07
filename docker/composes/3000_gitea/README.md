
- 2020/03/27
- [docker-gitea](https://hub.docker.com/r/gitea/gitea/)
- [git-gitea](https://github.com/go-gitea/gitea)
- [gitea container 參數](https://hub.docker.com/r/webhippie/gitea)


## 使用 docker run

```bash
### 2020/03/27 的今天, :1 為最新的穩定版本
$# docker pull gitea/gitea:1


### 測試 (使用 docker run)
$# docker run --rm \
    --name mygitea \
    -p 2222:22 \
    -p 3000:3000 \
    gitea/gitea:1


### 正式
$# docker volume create mygitea_1
$# docker run -d \
    --restart=always \
    --name mygitea \
    -p 2222:22 \
    -p 3000:3000 \
    -v mygitea_1:/data \
    gitea/gitea:1

### http://localhost:3000
# 隨便註冊吧
# id: tony@localhost.com
# pd: 1qaz@WSX
# 2020/03/27 的現在, 不知為啥的常常跟我說錯誤但其實是註冊成功...
```

# 記得到 web 時, 一定要改 `Gitea Base URL` (不可為 localhost)


## 使用 docker-compose

1. 單純作為 repository : `docker-compose up -d`
2. 與 gitlab 串接 CI/CI : `docker-compose -f docker-compose-gitlab.yml up -d`
3. 與 jenkins 串接 CI/CI
4. 與 drone 串接 CI/CI

```bash
### 開始運作
$# docker-compose up -d

### 停止, 啟動 compose (containers)
$# docker-compose stop
$# docker-compose start

### 整個砍掉 (stop & kill service, 但是 volumes 依然存在)
$# docker-compose down

### 看狀況
$# docker-compose logs -f
```


# SELinux Problem

- [](https://github.com/gidcs/gitea-selinux-policy/blob/master/README.md)

install gitea selinux policy

```bash
### 基本上用這個就可以了 (如果有用 nginx 反代 80 -> 3000)
$# semanage port -a -t http_port_t -p tcp 3000


### 底下這個網路上查到的, 不知道在幹嘛, 可能底層問題再來用吧
$# curl -o gitea.te https://raw.githubusercontent.com/gidcs/gitea-selinux-policy/master/gitea.te
$# checkmodule -M -m -o gitea.mod gitea.te
$# semodule_package -o gitea.pp -m gitea.mod
$# semodule -i gitea.pp
$# rm -f gitea.*
```
