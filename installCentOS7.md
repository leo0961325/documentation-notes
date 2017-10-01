# CentOS7 安裝雜七雜八的備註
- 我的版本是 CentOS Linux release 7.3.1611 (Core) 

```
$ uname -a
Linux tonydt 3.10.0-693.2.2.el7.x86_64 #1 SMP Tue Sep 12 22:26:13 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```

---

## - Google Chrome
- 2017/09/23
- [老灰鴨的筆記本](http://oldgrayduck.blogspot.tw/2016/04/linuxcentos-7-google-chrome.html)


1. 增加本地repo參考

```
# sudo touch /etc/yum.repos.d/google-chrome.repo
```

2. 新增下列內容
```
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
```

3. 安裝穩定版Google Chrome
```
# sudo yum -y install google-chrome-stable
```


---
## Docker
- 
- [Linux 技術手札](https://www.phpini.com/linux/rhel-centos-7-install-docker)

1. 安裝Docker
```sh
$ sudo yum -y update 
$ sudo yum -y install docker docker-registry 
```

2. 設定目前使用者, 對Docker具有Power User的權限
```sh
$ cat /etc/group | grep docker
dockerroot:x:983:

$ sudo groupadd docker
$ sudo usermod -aG docker $USERNAME

$ cat /etc/group | grep docker
dockerroot:x:983:
docker:x:1001:tony                 <-已經讓目前的使用者加到docker的群組了
```

3. 設定docker服務
```
$ systemctl start docker           <-立刻啟用
$ systemctl enable docker          <-重新開機後才啟用
$ systemctl status docker.service 
(建議這邊run完後, 重新登入 or 重新開機)
```

4. 測試執行docker
```
$ docker run hello-world
((如果看到一大堆歡迎使用Docker之類的廢話, 就表示OK了))

$ docker --version
Docker version 1.12.6, build c4618fb/1.12.6
```

---
## MySql 5.7 (有問題! 別用)
[Linux 技術手札 - 安裝MySQL 5.7](https://www.phpini.com/linux/rhel-centos-fedora-install-mysql-5-7)

1. 安裝MySQL
```sh
wget http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm
sudo yum install -y mysql57-community-release-el7-7.noarch.rpm
sudo yum install -y mysql-community-server
```

2. MySQL服務
```sh
systemctl status mysqld
systemctl enable mysqld
systemctl start mysqld
```

---
## MySql 5.6
- 
- [Linux 技術手札](https://www.phpini.com/mysql/rhel-centos-yum-install-mysql)

1. 新增本地repo
```
$ sudo rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm 
```

2. 安裝MySQL Server
```
$ sudo yum -y install mysql-community-server 
```

3. 啟動MySQL服務
```
systemctl enable mysqld 
systemctl start mysqld 
systemctl status mysql.service 
```

4. 其他備註
```sql
更改 root密碼
> SET PASSWORD FOR 'root'@'localhost' = '<newPassWord>';

建立使用者
> CREATE USER '<new-user>'@'<host>' IDENTIFIED BY '<newPassWord>';

賦予讀取權限
> GRANT ALL PRIVILEGES ON newdatabase.* TO '<new-user>'@'localhost';
```

---
## net-tools in docker
docker內, 若無法使用網路服務, 安裝它吧

- ifconfig
bash: ifconfig: command not found

- yum install net-tools

- ifconfig
-> success!



---
## docker-mysql
- 2017/10/01
- 前提, 已經下載並安裝好
	1. Docker
	2. MySQL

[Severalnines Blog - MySQL Docker Container](https://severalnines.com/blog/mysql-docker-containers-understanding-basics)


1. 下載及安裝MySQL image, 建立Container, 設定root密碼
```sh
$ docker run -d --name=<containerName> --env="MYSQL_ROOT_PASSWORD=<password>" mysql 
```

2. 看mysql啟動的Log
```sh
$ docker logs <containerName>
```

3. 取得每次啟動的docker ip
```sh
$ docker inspect <containerName> | grep IPAddress
```

4. 連進去Container囉!!
```sh
$ mysql -u <user> -p <password> -h <ip> -P <port>
```

5. 關閉MySQL Container
$ docker stop <containerName>

6. 將來再進去(Container要在, 只是還沒被啟動 docker ps -a要有)
$ docker start <containerName>

---
## mongoDB in docker


$ docker run --name mongo -it mongo /bin/bash

$ sudo docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
docker.io/mongo         latest              88b7188af865        23 hours ago        358.3 MB
...

可以直接取得每次啟動的docker ip
$ docker inspect <containerName> | grep IPAddress

進入 docker 的 mongo
$ mongo --port <port> --host <ip>


---
## install mongoDB 3.2 (只要改3.2為3.4, 也可裝3.4版)
http://blog.topspeedsnail.com/archives/6005

$ sudo vim /etc/yum.repos.d/mongodb-org.repo
[mongodb-org]
name=MongoDB 3.2 Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc


$ sudo yum install mongodb-org

啟動mongoDB
$ systemctl start mongod.service
$ systemctl enable mongod.service

啟動後,檢查mongoDB是否正在運行
$ ps auxw | grep mongod
$ systemctl status mongod 

加入下面兩行, 不再顯示警告訊息
$ sudo vi /etc/rc.local
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag

加入下面1行
$ sudo vim /etc/security/limits.d/20-nproc.conf 	
mongod   soft  nproc   64000

$ systemctl restart mongod
重啟後, 就不會有亂七八糟的警告訊息了

---
## vs code
https://code.visualstudio.com/docs/setup/linux

$ sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc

$ sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

$ yum check-update

$ sudo yum -y install code

---
## jdk1.8
徐老師的hadoop講義的安裝方式(下載java的rpm包來安裝)

手動到官方網站下載jdk(上課時徐老師給的載點掛掉了...2017/09/20)

$ sudo rpm -ivh jdk-8u144-linux-x64.rpm

$ sudo ln -s /usr/java/jdk1.8.0_144/ /usr/java/java

$ sudo vi .bashrc
export JAVA_HOME=/usr/java/java
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib/rt.jar
export PATH=$JAVA_HOME/bin:$PATH

$ java -version
java version "1.8.0_144"
Java(TM) SE Runtime Environment (build 1.8.0_144-b01)
Java HotSpot(TM) 64-Bit Server VM (build 25.144-b01, mixed mode)

---
## install Python
$ wget <python>

$ tar xf <python>.tar.xz
$ cd <python>

$ ./configure --enable-loadable-sqlite-extensions \
              --enable-shared \
              --prefix="\opt\python3"
$ make
$ sudo make install
$ ldconfig

安裝完後,開始設定環境變數（略）

底下開始安裝python3的pip
$ wget -0 /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py"
$ export PYTHON_PIP_VERSION=9.0.1
$ python3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION"
$ pip3 install --no-cache-dir --upgrade --force-reinstall "pip==$PYTHON_PIP_VERSION"

---
## install Anaconda (python3.6.1)
https://www.continuum.io/downloads

$ wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh

$ su bash ./Anaconda3-4.4.0-Linux-x86_64.sh

$ cd 

加入環境變數
$ vi .bashrc
export anaconda_HOME="/opt/anaconda3/"
export PATH=$anaconda_HOME/bin:$PATH

$ source .bashrc

$ python --version
Python 3.6.1 :: Anaconda 4.4.0 (64-bit)

---
## install Redis
https://redis.io/download

$ wget http://download.redis.io/releases/redis-3.2.9.tar.gz
$ tar xzf redis-3.2.9.tar.gz
$ cd redis-3.2.9
$ make

啟動方式:
terminal1 $ src/redis-server
terminal2 $ src/redis-cli

---
## install scala

1.到官方網站下載scala-SDK.xxx.tar.gz後

$ tar zxf scala-SDK.xxx.tar.gz

加入環境變數
$ vi .bashrc
export scala_HOME="/home/tony/scala-2.12.2"
export PATH=$scala_HOME/bin:$PATH 

---
## Git (CentOS7預設有git, 但是版本是1.8.x版)
- 2017/09/23
- [How To Install Git on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-centos-7)
- 

1. CentOS7原本就有Git, 但是版本老舊
```
$ git --version
git version 1.8.3.1
```

2. 安裝相依性套件
```
$ sudo yum groupinstall "Development Tools"
$ sudo yum install -y gettext-devel openssl-devel perl-CPAN perl-devel zlib-devel
```

3. 決定要裝哪種版本

    [查看想下載的版本](https://github.com/git/git/releases)

4. 開始下載&&編譯 ( 以2.14.1版為例 )
```
$ wget https://github.com/git/git/archive/v2.14.1.tar.gz -O git.tar.gz

$ tar -zxf git.tar.gz

$ cd git-2.14.1/

$ make configure
GIT_VERSION = 2.14.1
    GEN configure
```

```
說明文件中, 遺漏了重要的 "--with-curl"會導致無法上傳下載, 在此補上

$ sudo yum -y install curl-devel

$ ./configure --prefix=/usr/local --with-curl

$ sudo make install

重新啟動terminal後
$ git --version
git version 2.13.2
```

5. 安裝完後的疑問

    原本的```git version 1.8.3.1```, 好像還沒被刪除耶...

    改天再來找找它究竟被安裝在哪邊@___@


---
## PostgreSQL9.6 (安裝的不是很成功)
- 2017/07/??
- [PostgreSQL官方網站](https://www.postgresql.org/download/linux/redhat/)

1. 安裝Repo
```
$ yum install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

$ sudo yum install -y postgresql96
$ sudo yum install -y postgresql96-server

```

2. 啟動叢集
```
$ /usr/pgsql-9.6/bin/postgresql96-setup initdb
```

3. 啟動服務
```
# systemctl enable postgresql-9.6
# systemctl start postgresql-9.6
# systemctl status postgresql-9.6.service
```

---
## GeoDjango (非常大一包.... __安裝失敗__)
- 2017/07/??
- [官方教學 - GeoDjango Installation]
(https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/)
```
1.安裝python and Django
2.安裝Spatial libraries
3.安裝Geospatial database

1.（略)
yum -y install gdal

2.安裝Spatial Database
官方建議使用PostgreSQL with PostGIS
https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/geolibs/

安裝順序如下
 - GEOS
 - PROJ.4
 - GDAL
 - PostgreSQL
 - PostGIS

- 安裝GEOS(C++ library for geometric operation, GeoDjango的預設地理操作函式庫)
$ wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
$ tar xjf geos-3.4.2.tar.bz2
$ cd geos-3.4.2
$ ./configure
$ make
$ sudo make install 
$ sudo ldconfig       <- 用來確認動態函式庫的連結資訊
$ cd ..

- 安裝PROJ.4
$ wget http://download.osgeo.org/proj/proj-4.9.1.tar.gz
$ wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz
$ tar xzf proj-4.9.1.tar.gz
$ cd proj-4.9.1/nad
$ tar xzf ../../proj-datumgrid-1.5.tar.gz
$ cd ..
$ ./configure
$ make
$ sudo make install
$ cd ..

- 安裝GDAL
$ wget http://download.osgeo.org/gdal/1.11.2/gdal-1.11.2.tar.gz
$ tar xzf gdal-1.11.2.tar.gz
$ cd gdal-1.11.2
$ ./configure
$ make # Go get some coffee, this takes a while.
$ sudo make install
$ cd ..


- 安裝PostGIS
$ sudo yum -y install libxml2-devel
$ svn checkout http://svn.osgeo.org/postgis/trunk/ postgis-2.3.4dev
$ wget http://postgis.net/stuff/postgis-2.3.4dev.tar.gz
$ tar zxf postgis-2.3.4dev.tar.gz

下式改為PostgreSQL的pg_config所在位置
$ ./configure --with-pgconfig=/usr/pgsql-9.4/bin/pg_config


登入PL-SQL
$ sudo su - postgres / sudo -u postgres -i
```

---
最近更新日期 2017/09/23, by TonyCJ

