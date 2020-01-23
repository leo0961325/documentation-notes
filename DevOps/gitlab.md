# Gitlab in Docker

- 2019/05/16
- [Docker install GitLab](https://docs.gitlab.com/omnibus/docker/)
- [CentOS7 install GitLab](https://about.gitlab.com/install/#centos-7)

運行 GitLab Docker image 有多種方式

- Docker Engine 運行 image
- Cluster 中, 安裝 GitLab
- Docker-compose 安裝 GitLab

# 法1. CentOS

- 2019/05/17
- 不知為啥... 今年1月一直卡, 現在不知不覺就可以使用了

```bash
sudo yum install -y curl policycoreutils-python openssh-server
sudo systemctl enable sshd
sudo systemctl start sshd
sudo firewall-cmd --permanent --add-service=http
sudo systemctl reload firewalld

sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix

curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash

### 會執行一陣子
sudo EXTERNAL_URL="https://gitlab.example.com" yum install -y gitlab-ce
# URL 可自行修改

```

# 法2. Docker

```bash
### 下載官方 Image
$# docker pull gitlab/gitlab-ce
# version : gitlab-ce=11.10.4-ce.0

### Run image
$# docker run --detach \
  --hostname gitlab.example.com \
  --publish 28080:80 \
  --publish 22222:22 \
  --name gitlab-157 \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab:Z \
  --volume /srv/gitlab/logs:/var/log/gitlab:Z \
  --volume /srv/gitlab/data:/var/opt/gitlab:Z \
  --env GITLAB_OMNIBUS_CONFIG="external_url 'http://gitlab157.com'; gitlab_rails['lfs_enabled'] = true;" \
  gitlab/gitlab-ce:latest
# 記得 hike 自己的 /etc/hosts 設好名稱解析
# GitLab 資料都放在 「/srv/gitlab」
# 「:Z」確保 Docker process 具備 SELinux 的權限
# 設定主檔在 「/srv/gitlab/config/gitlab.rb:/etc/gitlab/gitlab.rb」
#「--publish 2222:22」 是因為 22 port 已經被 vm 的 ssh 占用
# 關於 env 那邊, 可在執行 Container 時, 就先定義好 external_url
# 另 lfs_enalbed 是允許 Git Large File Storage (movie, image, DB, ...)
# 不知道為什麼「--publish 443:443」 一直無法... 拔掉後就可順利了...

###
$# docker ps
CONTAINER ID  IMAGE                    COMMAND            CREATED        STATUS      PORTS                                                          NAMES
f764b9875ea3  gitlab/gitlab-ce:latest  "/assets/wrapper"  8 seconds ago  ...PASS...  0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:222->22/tcp  gitlab

### 初始化程序要等上一陣子... 追蹤 Log
$# docker logs -f gitlab

### 進入 Container (好像沒啥用...)
$# docker exec -it gitlab /bin/bash

### 編輯 external_url 為 gitlab.example.com
$# vim /srv/gitlab/gitlab.rb    # (系統內部)
$# vim /etc/gitlab/gitlab.rb    # (Container內部)
```

- 若想收到 GitLab 寄來的信件, 得設定 [SMTP](https://docs.gitlab.com/omnibus/settings/smtp.html)
- 若想做成 https, 得設定 [HTTPS](https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https)
- 關於組態的更多設定檔[看這](https://docs.gitlab.com/omnibus/settings/configuration.html)

設定完成之後, 得做 reconfigure

```bash
### re-run Container
$# docker restart gitlab
# 這個似乎會有問題... 發現 port mapping... 都不見了

### 強制移除 Container
$# docker rm gitlab --force
# 記得東西還在 /srv/gitlab
```

###### HTTP Response 422 : Bad Cookie 問題... 清空 storage 即可


# Docker gitlab

- 2020/01/15
- macbook
- https://docs.gitlab.com/ee/ci/quick_start/
- https://docs.gitlab.com/runner/install/docker.html

```bash
### GitLab
$# docker pull gitlab/gitlab-ce

### Run (Windows)

### Run (Macbook)
$# docker run --detach \
  --hostname mygitlab.com \
  --publish 12200:22 \
  --publish 18000:80 \
  --publish 14430:443 \
  --name mygitlab \
  --restart always \
  --volume ~/DockerVolumes/mygitlab/etc:/etc/gitlab \
  --volume ~/DockerVolumes/mygitlab/log:/var/log/gitlab \
  --volume ~/DockerVolumes/mygitlab/opt:/var/opt/gitlab \
  --env GITLAB_OMNIBUS_CONFIG="external_url 'http://mygitlab.com'; gitlab_rails['lfs_enabled'] = true;" \
  gitlab/gitlab-ce:latest

### Run (Linux)
$# docker run --detach \
  --hostname gitlab.example.com \
  --publish 12200:22 \
  --publish 18000:80 \
  --publish 14430:443 \
  --name mygitlab \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab:Z \
  --volume /srv/gitlab/logs:/var/log/gitlab:Z \
  --volume /srv/gitlab/data:/var/opt/gitlab:Z \
  --env GITLAB_OMNIBUS_CONFIG="external_url 'http://mygitlab.com'; gitlab_rails['lfs_enabled'] = true;" \
  gitlab/gitlab-ce:latest
# 記得 hike 自己的 /etc/hosts 設好名稱解析
# GitLab 資料都放在 「/srv/gitlab」
# 「:Z」確保 Docker process 具備 SELinux 的權限
# 設定主檔在 「/srv/gitlab/config/gitlab.rb:/etc/gitlab/gitlab.rb」
#「--publish 2222:22」 是因為 22 port 已經被 vm 的 ssh 占用
# 關於 env 那邊, 可在執行 Container 時, 就先定義好 external_url
# 另 lfs_enalbed 是允許 Git Large File Storage (movie, image, DB, ...)
```


# Docker Gitlab-Runner

```bash
### 2020/01/15
### GitLab-Runner
$# docker pull gitlab/gitlab-runner
# v12.6.0 (ac8e767a)

### 如何使用
$# docker run --rm -it gitlab/gitlab-runner --help


### Run (Macbook)
$# docker run -d --name gitlab-runner --restart always \
  -v /Users/Shared/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest

```