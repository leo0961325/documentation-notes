# gitea

- 2020/01/29
- [Install gitea](https://gist.github.com/appleboy/36313a525fbef673f8aefadb9c0f8247)
- [YT](https://www.youtube.com/watch?v=shxiz_bos3I&t=1942s)

```bash
### 建立 git 這個使用者 && 安裝 git
### 開 3000 port

### 2020/01/29 目前最新 1.9.6 (抓 amd64 for centos7)
(git)$ wget https://dl.gitea.io/gitea/1.9.6/gitea-1.9.6-linux-amd64 gitea
# 版本參考這邊 https://dl.gitea.io/gitea/

### hosting service
$ ./gitea web

### http://YOUR-GITEA-DOMAIN:3000/install
### 1. Domain 改成 ip 或 domain-name
### 2. Application URL 的 localhost 也要改

```


```bash
### 使用 caddy 換 port
$ wget https://github.com/caddyserver/caddy/releases/download/v1.0.2/caddy_v1.0.2_linux_amd64.tar.gz -O caddy.tar.gz
# 自己來換版本了 https://github.com/caddyserver/caddy/tags
# 教學 0.9.5 舊版 Caddy 使用 ACME1 已經無法做 letsencrypt 認證了
$ mkdir caddy && tar -zxvf caddy.tar.gz -C caddy
```



```bash
###
$# vim Caddyfile
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
### 這是 https
#demo.gitea.com {
#  proxy / 127.0.0.1:3000
#}

# 這是 http
http://demo.gitea.com {
  proxy / 127.0.0.1:3000
}
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
```
