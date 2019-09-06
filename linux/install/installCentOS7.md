# CentOS7 安裝備註

我的使用環境如下

```sh
$ uname -a
Linux tonynb 3.10.0-514.el7.x86_64 \#1 SMP Tue Nov 22 16:42:41 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

$ hostnamectl
   Static hostname: tonynb
         Icon name: computer-laptop
           Chassis: laptop
        Machine ID: 6e935c5d22124158bd0a6ebf9e086b24
           Boot ID: 3262e51d23a9478dbc268f562556a74c
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-514.el7.x86_64
      Architecture: x86-64

$ cat /etc/centos-release
CentOS Linux release 7.5.1804 (Core)

$ rpm --query centos-release
centos-release-7-5.1804.4.el7.centos.x86_64
```

- RHEL (RedHat Enterprise Linux) :
- EPEL (Extra Packages for Enterprise Linux) : 幾乎都是 RedHat 的實驗品... 正式 Server 別裝這些...



# yum

```sh
# 可查線上 repo 可安裝的套件(但是得給完全相同的名字才能查(可用regex))
$ yum list 'http*'

# (同上) 但可用關鍵字來查詢 (套件名稱, 套件說明)
$ yum search all 'web server'

# 給完整名稱, 查線上套件安裝資訊
$ yum info httpd

# 到 YUM Server 查 安裝在哪個位置的工具叫啥 or 該工具相關的套件
$ yum provides /var/www/html
$ yum provides semanage

# 查本地已經安裝的 Linex Kernels
$ yum list kernel

# 移除本地已安裝的套件 && Dependcies
$# yum remove httpd

# 查線上可安裝的群組套件
$ yum group list # 或 yum grouplist

# 可用關鍵字來查詢線上 群組套件名稱, 群組套件說明
$ yum groups info "Server with GUI"

# 增加 「yum repo 檔」 到 /etc/yum.repo.d/xxx.repo  (沒事別用這個...)
$# sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```


# Apache - kafka

- [看這邊](../../other/kafka.md)



# DotNet Core

- 2019/01/03
- https://dotnet.microsoft.com/download/linux-package-manager/centos/sdk-current

```sh
rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm
yum install dotnet-sdk-2.2

dotnet --version
```


# Google Chrome

- 2017/11/25
- [老灰鴨的筆記本](http://oldgrayduck.blogspot.tw/2016/04/linuxcentos-7-google-chrome.html)

1. repo
```
$ sudo touch /etc/yum.repos.d/google-chrome.repo

[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
```

2. Install
```
sudo yum -y install google-chrome-stable
```



# Docker CE

- 2017/11/25
- 2018/07/01 update
- [Official Docker](https://docs.docker.com/engine/installation/linux/docker-ce/centos/#install-using-the-repository)


```sh
### root
# 安裝
$# yum install -y yum-utils device-mapper-persistent-data lvm2
$# yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$# yum install -y docker-ce

### Normal User
# 確認權限
$ cat /etc/group | grep docker
docker:x:983:

$ sudo usermod -aG docker ${USER}

$ cat /etc/group | grep docker
docker:x:983:tonynb

# 服務
$ sudo systemctl start docker           <-立刻啟用
$ sudo systemctl enable docker          <-重新後啟用
$ systemctl status docker

# 完成
$ docker version
Client:
 Version:           18.06.1-ce
 API version:       1.38
 Go version:        go1.10.3
 Git commit:        e68fc7a
 Built:             Tue Aug 21 17:23:03 2018
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          18.06.1-ce
  API version:      1.38 (minimum version 1.12)
  Go version:       go1.10.3
  Git commit:       e68fc7a
  Built:            Tue Aug 21 17:25:29 2018
  OS/Arch:          linux/amd64
  Experimental:     false


# 無法執行的話, 重新登入就可以了
$ docker run hello-world
Hello, World.
```


## Docker-compose

- 2019/01/11
- [Install Docker Compose](https://docs.docker.com/compose/install/)

```sh
$# curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$# chmod +x /usr/local/bin/docker-compose
$# docker-compose --version
docker-compose version 1.23.2, build 1110ad01
```


## Docker-machine
- [Install Docker Machine](https://docs.docker.com/machine/install-machine/)

```sh
### root
# v0.14 Docker Machine
base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo install /tmp/docker-machine /usr/local/bin/docker-machine

# v0.15 Docker Machine
curl -L https://github.com/docker/machine/releases/download/v0.15.0/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
    chmod +x /tmp/docker-machine &&
    sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
```


## docker - bash completion

- [Docker-Machine Tab-Completion]()
```sh
### root
$# vim /etc/bash_completion.d/docker-machine-prompt.bash
base=https://raw.githubusercontent.com/docker/machine/v0.14.0
for i in docker-machine-prompt.bash docker-machine-wrapper.bash docker-machine.bash
do
  sudo wget "$base/contrib/completion/bash/${i}" -P /etc/bash_completion.d
done
# 內容如上 ----------------------------------

$# source /etc/bash_completion.d/docker-machine-prompt.bash

# To enable the docker-machine shell prompt, add $(__docker_machine_ps1) to your PS1 setting in ~/.bashrc.
$ echo "PS1='[\u@\h \W$(__docker_machine_ps1)]\$ '" >> ~/.bashrc
```


# bash_completion

 - 2019/07/03
 - https://www.tecmint.com/install-and-enable-bash-auto-completion-in-centos-rhel/

```bash
$# yum install -y bash-completion bash-completion-extras
$# locate bash_completion.sh
$# source /etc/profile.d/bash_completion.sh
```

# Ansible

- 2019/01/12
- [Ansible tar file](https://releases.ansible.com/ansible-tower/setup-bundle/)
- 2G+ RAM (建議 4G+)
- 20G Disk
- 64 bits os

### 1. Download && Install

```sh
$# wget https://releases.ansible.com/ansible-tower/setup-bundle/ansible-tower-setup-bundle-3.0.3-1.el7.tar.gz
$# tar -zxf ansible-tower-setup-bundle-3.0.3-1.el7.tar.gz
$# cd ansible-tower-setup-bundle-3.0.3-1.el7/

$# vim inventory
### 先設定好 inventory 裏頭的 3 組密碼

$# ./setup.sh   # 會檢查 Disk, RAM ...
# 好像會偷偷幫你安裝 PostgreSQL, redis, httpd...
# ~~~ 會安裝一陣子~~~

The setup process completed successfully.   # ← successfully
Setup log saved to /var/log/tower/setup-2019-01-12-17:53:43.log
You have new mail in /var/spool/mail/root
# 安裝完後, 要看到上面的訊息才算 OK
```

### 2. Setup

安裝完後, 就可透過網頁看到 Ansible Tower 的管理頁面了~

```sh
### Step 1. 改密碼~
$# tower-manage changepassword admin
Changing password for user 'admin'
Password:
Password (again):
Password changed successfully for user 'admin'

### Step 2. 然後就可以登入網頁
# 因為是個人, 所以選擇申請個人版(只能管理 10 nodes 以下)
# 且無法使用 LDAP
# 填妥收信後, 就可以收到 Licenses 了~
```

```sh
### PKI
$# ssh-keygen -f tower_rsa
$# ssh-copy-id -i ~/.ssh/tower_rsa.pub <RemoteUser>@<RemoteIP>
$# ssh -i ~/.ssh/tower_rsa <RemoteUser>@<RemoteIP>
# 將來便可使用 Public Key 方式連線
```


# ELK - elasticsearch

- 2019/01/12

### 1. 使用 yum 安裝

```sh
$# rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
$# vim /etc/yum.repos.d/elasticsearch.repo
###### 內容如下 ######
[elasticsearch-6.x]
name=Elasticsearch repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
###### 內容如上 ######

$# yum install elasticsearch
```

### 2. 使用 rpm 安裝

```sh
### Download
$# wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.5.4.rpm

### Install
$# rpm -ivh elasticsearch-6.5.4.rpm
warning: elasticsearch-6.5.4.rpm: Header V4 RSA/SHA512 Signature, key ID d88e42b4: NOKEY
Preparing...                          ################################# [100%]
Creating elasticsearch group... OK
Creating elasticsearch user... OK
Updating / installing...
   1:elasticsearch-0:6.5.4-1          ################################# [100%]
### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using systemd
 sudo systemctl daemon-reload
 sudo systemctl enable elasticsearch.service
### You can start elasticsearch service by executing
 sudo systemctl start elasticsearch.service
Created elasticsearch keystore in /etc/elasticsearch

$# systemctl start elasticsearch
$# systemctl enable elasticsearch
$# systemctl status elasticsearch
```


# ELK - kibana

- 2019/01/24
- [Install Kibana with RPM](https://www.elastic.co/guide/en/kibana/current/rpm.html)

```sh
$# rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

$# vim /etc/yum.repos.d/kibana.repo
###### 內容如下 ######
[kibana-6.x]
name=Kibana repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
###### 內容如上 ######

$# yum install kibana
```

# ELK - logstash

- [Install Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

```sh
$# rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

$# vim /etc/yum.repos.d/logstash.repo
###### 內容如下 ######
[logstash-6.x]
name=Elastic repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
###### 內容如上 ######

$# yum install -y logstash
```

# ELK - metricbeat

- [Install Metricbeat](https://www.elastic.co/guide/en/beats/metricbeat/6.5/setup-repositories.html)
- [各種 Logstash 之下的 Beats](https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-elastic-stack.html)

```sh
$# rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch

$# vim /etc/yum.repos.d/elastic.repo
###### 內容如下 ######
[elastic-6.x]
name=Elastic repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
###### 內容如上 ######

$# yum install -y metricbeat

### enalbe
$# systemctl enable metricbeat
$# chkconfig --add metricbeat
```

# ELK - Filebeat

- [How To Install Elasticsearch, Logstash, and Kibana (ELK Stack) on CentOS/RHEL 7](https://www.tecmint.com/install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-rhel-7/)

```sh
$# rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch

$# vim /etc/yum.repos.d/filebeat.repo
###### 內容如下 ######
[filebeat]
name=Filebeat for ELK clients
baseurl=https://packages.elastic.co/beats/yum/el/$basearch
enabled=1
gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch
gpgcheck=1
###### 內容如上 ######

$# yum install filebeat

### Config
$# vim /etc/filebeat/filebeat.yml
```



# MySQL Community 5.7

- 2018/09/14
- [Official MySQL](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)

1. 安裝 MySQL

```sh
# 1. 編寫 yum repo 檔
$ sudo vim /etc/yum.repos.d/mysql-community.repo
###### 內容如下 ######
[mysql57-community]
name=MySQL 5.7 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=http://repo.mysql.com/RPM-GPG-KEY-mysql
###### 內容如上 ######

# 2. Check Repo && Install
$# yum repolist | grep mysql
mysql57-community/x86_64     MySQL 5.7 Community Server      287

$# yum install -y mysql-community-server

# 3. 啟動 && 設定 root 密碼~
$# systemctl start mysqld.service

$# grep 'temporary password' /var/log/mysqld.log

$ mysql -uroot -p
# 前面取得的密碼登入
```

2. 更改密碼~

```sql
--;# 登入 MySQL 後, 立馬改密碼
ALTER USER 'root'@'localhost' IDENTIFIED BY '<new password>';

--;# 自己看看要不要移除 密碼政策
uninstall plugin validate_password;

--;# 建立 User
CREATE USER 'tony'@'%' IDENTIFIED BY '<password>';
GRANT ALL ON *.* TO 'tony'@'%';

-- Example
create user 'demo'@'localhost' identified by '00';
grant all on *.* to 'demo'@'localhost';
```



# MongoDB CE

- 2017/11/26
- [Official MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)

```sh
# 1. 編寫 Yum repo 檔
$# vim /etc/yum.repos.d/mongodb-org-3.4.repo
###### 內容如下 ######
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
###### 內容如上 ######

# 2. Check Repo && Install
$# yum repolist | grep mongo
mongodb-org-3.4/7       MongoDB Repository        90

$# yum install -y mongodb-org

# 3. 啟動~
$# systemctl start mongod.service

$ mongod --version
db version v3.4.17
git version: 7c14a47868643bb691a507a92fe25541f998eca4
OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
allocator: tcmalloc
modules: none
build environment:
    distmod: rhel70
    distarch: x86_64
    target_arch: x86_64

$ ps auxw | grep mongod
mongod  8562  1.1  1.0 972408 41188 ?      Sl  20:43  0:01 /usr/bin/mongod -f /etc/mongod.conf
tony    9499  0.0  0.0 112708   968 pts/2  S+  20:45  0:00 grep --color=auto mongod
```



# Visual Studio Code

- 2018/09/14
- [Official vscode](https://code.visualstudio.com/docs/setup/linux)

```sh
# 1. 編寫 Yum Repo
$# vim /etc/yum.repos.d/vscode.repo
###### 內容如下 ######
[code]
name=Visual Studio Code
baseurl=https://packages.microsoft.com/yumrepos/vscode
enabled=1
gpgcheck=1
gpgkey=https://packages.microsoft.com/keys/microsoft.asc
###### 內容如上 ######

# 2. Check Repo && Install
$# yum repolist | grep code
code        Visual Studio Code       44

$# yum -y install code
```


# install Anaconda (python3.6.1)

- 2017/11/26
- [Official Anaconda](https://www.continuum.io/downloads)

1. Download && Install

```sh
$ wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh

$ bash ./Anaconda3-5.0.1-Linux-x86_64.sh
# 安裝在使用者家目錄就好了~~  省麻煩阿~~
```

2. 設環境變數
```sh
echo "export anaconda_HOME=\"/home/${USER}/anaconda3\"" >> ~/.bashrc
echo 'export PATH=$anaconda_HOME/bin:$PATH' >> ~/.bashrc

$ python --version
Python 3.6.3 :: Anaconda, Inc.
```



# Redis

- 2017/11/26 (2018/05/15, 2018/09/02 update)
- [Official Redis](https://redis.io/download)
- [cc not found 解法1](https://stackoverflow.com/questions/35634795/no-acceptable-c-compiler-found-in-path-while-installing-the-c-compiler)
- [cc not found 解法2](https://unix.stackexchange.com/questions/287913/cc-command-not-found-when-compiling-a-pam-module-on-centos?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- [jemalloc not found 的解說1](https://blog.csdn.net/bugall/article/details/45914867)
- [jemalloc not found 的解說2](http://www.ywnds.com/?p=6957)
- [Linode - Install and Configure Redis on CentOS 7](https://www.linode.com/docs/databases/redis/install-and-configure-redis-on-centos-7/)


```sh
# 安裝 Redis
$ sudo yum install epel-release
$ sudo yum install redis
$ sudo systemctl start redis
```



# Git (CentOS7 default repo -> git v-1.8 太舊了~~)
- 2017/11/26
- [How To Install Git on CentOS 7](https://blacksaildivision.com/git-latest-version-centos)
- [Choose a version](https://github.com/git/git/releases) ( 以2.14.3版為例 )
- [Choose a version 有時候Github會掛掉...](https://mirrors.edge.kernel.org/pub/software/scm/git/)

1. Dependancy
```sh
# 所需套件
$# yum install -y autoconf libcurl-devel expat-devel gcc kernel-headers openssl-devel perl-devel zlib-devel gettext-devel
# 上頭的 gettext-devel 會安裝 git 1.8.3
# 其實可以不安裝它... 只是最後, git 會被安裝在 /usr/local/bin/git
# root 環境變數裡面沒有它, 所以 root 要再設個軟連結~

# 下載 (v2.14.3)
$ wget https://github.com/git/git/archive/v2.14.3.tar.gz

# (v2.14.5)
$ wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.14.5.tar.gz
# (v2.19)
$ wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.19.1.tar.gz

# Install (v2.14.3)
$ tar zxf v2.14.3.tar.gz
$ cd git-2.14.3/
$ make clean
$ make configure
GIT_VERSION = 2.14.3
    GEN configure

$ ./configure --prefix=/usr/local
$ make
$# make install

$ git --version
git version 2.14.3
# DONE

# Install (v2.19)
$ mkdir git2.19
$ tar zxf git-2.19.1.tar.gz
$ cd git-2.19.1
$ make configure
GIT_VERSION = 2.19.1
    GEN configure

$ ./configure --prefix=/usr/local
$ make
$# make install
```

一般使用者可使用 git 了!!

但是 root 找不到 git, 解法如下:

```sh
$# git
bash: git: command not found...

$# echo $PATH
/usr/local/sbin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

$# ln -s /usr/local/bin/git /usr/local/sbin/git

$# which git
/usr/local/sbin/git

$# git --version
git version 2.14.3
```



# 語言套件

- 2018/10/04


```sh
# 想要輸入中文的話, 裝這些吧
$# yum install ibus* cjk*
```



# net-tools

- 2017/11/26
- [centos7 最小化安装無網路服務](http://www.cnblogs.com/cocoajin/p/4064547.html)

```
$ ifconfig
bash: ifconfig: command not found

$ yum install -y net-tools

$ ifconfig
success!
```



# VLC

- 2017/11/26
- [How to Install EPEL on CentOS 7](https://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/)
- [How To Install VLC On CentOS 7](https://www.unixmen.com/install-vlc-centos-7/)
- [install vlc on CentOS7](https://stackoverflow.com/questions/29443096/how-to-install-vlc-on-centos7-from-terminal)

1. Install EPEL
```
$ wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
$ sudo rpm -ivh epel-release-latest-7.noarch.rpm
```

2. Install
```
$ sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm

$ sudo yum install vlc

$ vlc --V
VLC media player 2.2.5.1 Umbrella (revision 2.2.5-70-gaeea04d843)
vlc: unknown option or missing mandatory argument `-V'
Try `vlc --help' for more information
```



# teamviewer

- 2018/02/07
- [Install TeamViewer on CentOS 7 / RHEL 7](https://community.teamviewer.com/t5/Knowledge-Base/How-to-install-TeamViewer-Host-for-Linux/ta-p/6318?_ga=2.2833328.1279667713.1518017393-1552891207.1518017393)

```sh
$ wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

$ sudo yum install /tmp/epel-release-latest-7.noarch.rpm

$ wget https://download.teamviewer.com/download/linux/teamviewer.i686.rpm       # 32bits
$ wget https://download.teamviewer.com/download/linux/teamviewer.x86_64.rpm     # 64bits

$ sudo yum install teamviewer_13.0.6634.i686.rpm
# 不知道未啥... 我的無法安裝x86_64... 只好安裝這個32位元的

$ uname -m
x86_64
```



# 7zip
- 2017/11/26
- [e Learning](http://elearning.wsldp.com/pcmagazine/extract-7zip-centos-7/)

1. Dependancy && Install
```
$ sudo yum install -y epel-release

$ sudo yum install -y p7zip
```

2. Unzip
```
$ 7za x <fileName>
<password>
```



# Install Nginx

- 2018/03/19
- [Official](http://nginx.org/en/linux_packages.html#stable)
- [參考這邊](https://dotblogs.com.tw/grayyin/2017/05/18/183117)

```sh
# 1. 匯入 GPG-Key
$# curl http://nginx.org/keys/nginx_signing.key > nginx_signing.key
$# rpm --import nginx_signing.key

# 2. 建立 Yum Repo
$# vim /etc/yum.repos.d/nginx.repo
###### 內容如下 ######
[nginx]
name=Nginx Repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=1
enabled=1
###### 內容如上 ######

### 3. Repolist && Install
$ yum repolist | grep nginx
nginx/x86_64      Nginx Repo         108

$# yum install -y nginx

$ nginx -v
nginx version: nginx/1.14.0

$# nginx -t
$# nginx -s reload
$# systemctl start nginx
```



# Install tcping

- 2019/08/16
- 用來檢測域名可否正常訪問

```bash
$# vim /etc/yum.repos.d/tcping.repo
[tcping]
name=tcping repo
baseurl=https://download-ib01.fedoraproject.org/pub/epel/7/$basearch/
gpgcheck=0
enabled=1

$# yum repolist | grep tcping
tcping/x86_64            tcping repo                                      13,341

$# yum install -y tcping

### usage
$# tcping -t 5 www.google.com 80
www.google.com port 80 open.
```



# Install Apache

- 2018/02/27
- [安裝Apache, MySQL, PHP](https://www.phpini.com/linux/redhat-centos-7-setup-apache-mariadb-php)

```sh
$ sudo yum install -y httpd

$ sudo systemctl start httpd
$ sudo systemctl enable httpd

$ httpd -v
Server version: Apache/2.4.6 (CentOS)
Server built:   Oct 19 2017 20:39:16
```
進入瀏覽器, 「localhost」就可以看到網頁了~


# Install Postgresql

- 2019/05/16
- [How to install PostgreSQL 11 on CentOS7](https://tecadmin.net/install-postgresql-11-on-centos/)

```sh
### 安裝 Postgresql 11
$# rpm -Uvh https://yum.postgresql.org/11/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
$# yum install -y postgresql11-server

### init db
$# /usr/pgsql-11/bin/postgresql-11-setup initdb

### start
$# systemctl start postgresql-11.service
$# systemctl status postgresql-11.service

### Log in
$# psql -h <host> -p <port> -U <username> -W <password> <database>
```

```sql
-- 登入後的 Shell
DB=# \dn+
                          List of schemas
  Name   |  Owner   |  Access privileges   |      Description
---------+----------+----------------------+------------------------
 public  | postgres | postgres=UC/postgres+| standard public schema
         |          | =UC/postgres         |

DB=# \t
```


# install scala (不完整)
- 2017/06/??
- [Official Scala](https://www.scala-lang.org/download/)

1. **Install JRE first**

2. Download tar-ball
```
$ wget https://github.com/scala/scala/archive/v2.12.4.tar.gz
```

3. Install
```
$ tar zxf scala-2.12.4.tar.gz

$ cd

$ vi .bashrc
export scala_HOME="/home/tony/scala-2.12.4"
export PATH=$scala_HOME/bin:$PATH
```


# Install Python3.7 on CentOS7.6

- 2019/05/10
- [CentOS 7 下 安装 Python3.7](https://segmentfault.com/a/1190000015628625)

```sh
### 必要套件
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
# libffi-devel 專門給 python3.7

### 為了要安裝「python-pip」
yum -y install epel-release

### 安裝 pip
yum install -y python-pip

### 下載 Python3.7.3 tar ball
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz

tar zxf Python-3.7.3.tgz
cd Python-3.7.3
./configure --enable-optimizations --enable-loadable-sqlite-extensions

### 開始 Compile
make -j 2 && make install
# -j 2: 使用Core

### root 環境變數 (一般使用者可直接使用...)
echo 'PYTHON_HOME=/usr/local/bin' >> ~/.bash_profile
echo 'PATH=${PYTHON_HOME}:${PATH}' >> ~/.bash_profile

### pipenv
pip3 install pipenv


### virtualenv
pip install virtualenv virtualenvwrapper    # 是 pip 而非 pip3

echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv -p /usr/local/bin/python3 <ENV_NAME>
mkdir ~/<ENV_NAME>
cd <ENV_NAME>
setvirtualenvproject .

workon <ENV_NAME>
deactivate <ENV_NAME>

```


# install Python (不完整)

```sh
$ wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz

$ tar xf <python>.tar.xz
$ cd <python>

$ ./configure --enable-loadable-sqlite-extensions --enable-shared --with-ssl --prefix="~/python3"
$ make
$ sudo make install
$ ldconfig
```

安裝完後,開始設定環境變數（略）

底下開始安裝python3的pip
```sh
$ wget -O get-pip.py "https://bootstrap.pypa.io/get-pip.py"
$ export PYTHON_PIP_VERSION=9.0.1
$ python3 get-pip.py "pip==$PYTHON_PIP_VERSION"
$ pip3 install --no-cache-dir --upgrade --force-reinstall "pip==$PYTHON_PIP_VERSION"
```



# Install jdk1.8

- 2018/03/21
- [Official Orical jdk](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

兩種方法:

1. 拔掉 OpenJDK => OracleJRE,JDK
2. 純安裝(用環境變數來抓)

## 1. 連同 openjdk-JRE 一起拔掉, 換成 Oracle jdk

- [How to remove OpenJDK and install Oracle JDK](https://support.cafex.com/hc/en-us/articles/200874471-How-to-remove-OpenJDK-and-install-Oracle-JDK)

```sh
### rpm ================================
$# rpm -qa | grep jdk
# ↑ 慢慢移掉...

### 下載 rpm
$# wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.rpm
# ↑ 到官方網址, 勾選同意 license 之後, 取代要下載的網址(版本更新的話)

### 安裝
$# rpm -ivh jdk-8u201-linux-x64.rpm

### tar ball ===========================
#下載 tarball
$# wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz
# ↑ 到官方網址, 勾選同意 license 之後, 取代要下載的網址(版本更新的話)

$# tar -zxf jdk-8u201-linux-x64.tar.gz
$# mv jdk1.8.0_201/ ~/.
$# echo 'export JAVA_HOME=/root/jdk1.8.0_201' >> /etc/bashrc
$# echo 'export PATH=${JAVA_HOME}/bin:${PATH}' >> /etc/bashrc

$# java -version
java version "1.8.0_191"
Java(TM) SE Runtime Environment (build 1.8.0_191-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.191-b12, mixed mode)

$# javac -version
javac 1.8.0_191
```


## 2. 單純安裝其他版本(不動 JRE)

```sh
$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/tony/.local/bin:/home/tony/bin

$ java -version
openjdk version "1.8.0_161"
OpenJDK Runtime Environment (build 1.8.0_161-b14)
OpenJDK 64-Bit Server VM (build 25.161-b14, mixed mode)
# 安裝之前~

$ wget https://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz
# ↑ 無法直接使用... 網頁上需要點選 Accept License 才能下載XD 發Q~

$ mkdir ~/bin
$ tar -zxf jdk-8u191-linux-x64.tar.gz
$ mv jdk1.8.0_191/ ~/bin
$ echo 'export jdk_HOME="$HOME/bin/jdk1.8.0_191"' >> ~/.bashrc
$ echo 'export PATH=$jdk_HOME/bin:$PATH' >> ~/.bashrc

# 重起 terminal後
$ which java
~/bin/jdk1.8.0_191/bin/java

$ which javac
~/bin/jdk1.8.0_191/bin/javac

$ java -version
java version "1.8.0_191"
Java(TM) SE Runtime Environment (build 1.8.0_191-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.191-b12, mixed mode)

$ javac -version
javac 1.8.0_191
```






# Install KVM

- 2018/04/22
- [Install KVM Hypervisor](https://www.linuxtechi.com/install-kvm-hypervisor-on-centos-7-and-rhel-7/)
- CentOS用的 VirtualBox....

```sh
# 檢測 CPU是否支援 硬體虛擬化
$ grep -E '(vmx|svm)' /proc/cpuinfo
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch invpcid_single intel_pt tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp
# (會出現很多東西, 上面只是其中一項, 但我不知道這是啥), 看起來, 如果不是啥都沒有的話, 那應該就有支援 虛擬化了!!

$ sudo yum install -y qemu-kvm qemu-img virt-manager libvirt libvirt-python libvirt-client virt-install virt-viewer bridge-utils

$ lsmod | grep kvm
kvm_intel             174250  0
kvm                   570658  1 kvm_intel
irqbypass              13503  1 kvm

$ sudo systemctl start libvirtd

# 開始使用^O^
$ sudo virt-manager
```



# VirtualBox

- 2018/08/19
- [官網](https://www.virtualbox.org/wiki/Linux_Downloads)
- [RPM Resource libSDL-1.2.so.0](https://rpmfind.net/linux/rpm2html/search.php?query=libSDL-1.2.so.0()(64bit))

```sh
# 授權
$ wget https://www.virtualbox.org/download/oracle_vbox.asc
$ sudo rpm --import oracle_vbox.asc

# VirtualBox 相依套件
$ wget https://rpmfind.net/linux/centos/7.5.1804/os/x86_64/Packages/SDL-1.2.15-14.el7.x86_64.rpm
$ sudo rpm -Uvh SDL-1.2.15-14.el7.x86_64.rpm

# 抓主檔 && 安裝
$ wget https://download.virtualbox.org/virtualbox/5.2.18/VirtualBox-5.2-5.2.18_124319_el7-1.x86_64.rpm
$ sudo rpm -Uvh VirtualBox-5.2-5.2.18_124319_el7-1.x86_64.rpm
正在準備…                       ################################# [100%]
Updating / installing...
   1:VirtualBox-5.2-5.2.18_124319_el7-################################# [100%]

Creating group 'vboxusers'. VM users must be member of that group!

$ systemctl status vboxautostart-service
```



# gcc, make

- 2018/06/16
- [bash - make command not found](https://stackoverflow.com/questions/21700755/bash-make-command-not-found)
- [cc: Command not found](https://unix.stackexchange.com/questions/287913/cc-command-not-found-when-compiling-a-pam-module-on-centos?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

發生 `bash make command not found` ==> 無法編譯 tarball 阿~~~

```sh
# 不知道這是不是一個好的解法... 一口氣安裝超級大一包
$ sudo yum groupinstall "Development Tools"

# Note : "Development Tools" => yum CentOS
# Note : "build-essential" => apt Ubuntu
```



# 解壓縮

- [Linux 解壓縮 rar](https://www.phpini.com/linux/linux-extract-rar-file)
- 2018/06/16

```sh
$ sudo yum install unrar

$ unrar e <file.rar>    # 解壓縮到當前目錄
$ unrar l <file.rar>    # 列出壓縮黨內的目錄
$ unrar t <file.rar>    # 測試壓縮檔是否完整
# 有密碼的話, 後面在接著輸入
```



# Node.js

- 2018/09/14
- [官網](https://nodejs.org/en/)

```sh
$ wget https://nodejs.org/dist/v10.7.0/node-v10.7.0-linux-x64.tar.xz        # 10.7
$ wget https://nodejs.org/dist/v8.11.3/node-v8.11.3-linux-x64.tar.xz        # 8.11

$ tar xJf node-v10.7.0-linux-x64.tar.xz     # 解壓縮xz 10.7
$ tar xJf node-v8.11.3-linux-x64.tar.xz     # 解壓縮xz 8.11

$ cd node-v10.7.0-linux-x64/
$ cd node-v8.11.3-linux-x64/

$ mkdir ~/bin
$ ln -s /home/tony/Downloads/node-v8.11.3-linux-x64/bin/node ~/bin/node # v8.11

$ node --version
v8.11.3
```



# PhantomJS

- [Install PhantomJS on CentOS](https://www.bonusbits.com/wiki/HowTo:Install_PhantomJS_on_CentOS)

```sh
$ sudo yum install fontconfig freetype freetype-devel fontconfig-devel libstdc++

$ wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2

$ sudo mkdir -p /opt/phantomjs

$ tar jxf phantomjs-1.9.8-linux-x86_64.tar.bz2

$ rm phantomjs-1.9.8-linux-x86_64.tar.bz2
$ sudo mv phantomjs-1.9.8-linux-x86_64/* /opt/phantomjs/
$ rmdir phantomjs-1.9.8-linux-x86_64/
$ ln -s /opt/phantomjs/bin/phantomjs ~/bin/phantomjs
```



# Go lang

- 2018/09/14

```sh
# Download && untar
$ wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz

$ tar -C ~/. -xzf go1.11.linux-amd64.tar.gz

$ echo "export PATH=/home/${USER}/go/bin:\$PATH" >> ~/.bashrc

$ go version
go version go1.11 linux/amd64
```


# supervisor

- 2019/05/02

```sh
$# yum install -y supervisor
```


# chromedriver

```bash
### selenium 用
echo "Installing Chromedriver..."
wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo cp chromedriver /usr/local/bin
```


# fuser

- 2019/07/19

```bash
### 這個套件包含了 fuser
$# yum install -y psmisc
```


# zabbix-agent

- 2019/07/24
- [How to Install Zabbix Agent on CentOS/RHEL 7/6](https://tecadmin.net/install-zabbix-agent-on-centos-rhel/)

```bash
### 安裝 (2019/07 選擇 4.0 LTS)
$# rpm -Uvh http://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-agent-4.0.10-1.el7.x86_64.rpm
$# yum install zabbix-agent

### Config
$# vim /etc/zabbix/zabbix_agentd.conf
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#Server=[zabbix server ip]
#Hostname=[ Hostname of client system ]

Server=192.168.2.158,192.168.1.200  # ← 誰可以監控我
Hostname=vm157                      # ← 我這台 Agent 叫啥
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

$# systemctl start zabbix-agent

### 防火牆, SELinux...
```

# zabbix-server

- 2019/07/24
- [官網](https://www.zabbix.com/documentation/4.0/manual/installation/install_from_packages/rhel_centos)
- [How to Install Zabbix Server 4.0 on CentOS 7](https://computingforgeeks.com/how-to-install-zabbix-server-4-0-on-centos-7/)
- [How To Install Zabbix Server 3.4 on CentOS/RHEL 7/6](https://tecadmin.net/install-zabbix-network-monitoring-on-centos-rhel-and-fedora/)

Zabbix-Server 是一整包的東西... 它包含了:

- zabbix-server
- database(mysql/postgres)
- monitor GUI(php, apache)

```bash
### 安裝
$# rpm -ivh https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
$# yum-config-manager --enable rhel-7-server-optional-rpms
$# yum -y install zabbix-server-mysql zabbix-web-mysql

### 若要使用 zabbix-proxy...
$# yum install zabbix-proxy-mysql

$# systemctl start mysqld
```

```bash
### mysql 部分 (安裝完後)
mysql> CREATE DATABASE zabbixdb CHARACTER SET UTF8;
mysql> GRANT ALL PRIVILEGES on zabbixdb.* to zabbix@localhost IDENTIFIED BY 'password';
mysql> FLUSH PRIVILEGES;
$# zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uroot -p zabbixdb
$# zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -uroot -p zabbixdb
# 建立 zabbix server 存資料的地方 && 倒 schema 進去

$# vim /etc/zabbix/zabbix_server.conf
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
  DBHost=localhost
  DBName=zabbixdb
  DBUser=zabbix
  DBPassword=password
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

$# systemctl start zabbix-server
```


# Redis GUI

- 2019/08/06
- [Win 及 Mac 似乎要 License, 但 Linux 似乎不用...?](https://github.com/uglide/RedisDesktopManager)
- [How to install RedisDesktopManager on CentOS](https://snapcraft.io/install/redis-desktop-manager/centos#install)
- [Redis Desktop Manager - Quick Start](http://docs.redisdesktop.com/en/latest/quick-start/)

```bash
### Install
$# yum install -y snapd
$# systemctl start snapd

$# ln -s /var/lib/snapd/snap /snap

$# snap install redis-desktop-manager

### 如果發生下面的錯誤訊息 ----
error: cannot perform the following tasks:
- Download snap "core" (7396) from channel "stable" (Get https://fastly-global.cdn.snapcraft.io/download-origin/fastly/99T7MUlRhtI3U0QFgl5mXXESAiSwt776_7396.snap?token=1567663200_c1175619102aaa846a99bebd0325ea39d4555194: x509: certificate has expired or is not yet valid)
# ---------------------------
# 作時間校正後, 即可安裝. 參考 https://stackoverflow.com/questions/55234385/how-to-ignore-certificates-check-in-snap-on-ubuntu

### 時間校正
$# systemctl start chronyd
$# chronyc sources -v
# 以上是透過 time server 作校時, 視情況用手動
```


# 備註

- $basearch : x86_64 (位元架構)
- $releasever : CentOS7 的 7 (大版本號)
