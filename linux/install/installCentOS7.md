# CentOS7 安裝備註

我的使用環境如下
```
$ uname -a
Linux tonynb 3.10.0-514.el7.x86_64 #1 SMP Tue Nov 22 16:42:41 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

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
CentOS Linux release 7.3.1611 (Core)

$ rpm --query centos-release
centos-release-7-3.1611.el7.centos.x86_64
```



---
## Google Chrome
- 2017/11/25
> [老灰鴨的筆記本](http://oldgrayduck.blogspot.tw/2016/04/linuxcentos-7-google-chrome.html)

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



---
## Docker CE
- 2017/11/25
> [Official Docker](https://docs.docker.com/engine/installation/linux/docker-ce/centos/#install-using-the-repository)

1. Dependancy package && Install
```
$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

$ sudo yum install -y docker-ce
```

2. Authority
```
$ cat /etc/group | grep docker
docker:x:983:

$ sudo groupadd docker
$ sudo usermod -aG docker $USERNAME

$ cat /etc/group | grep docker
docker:x:983:tonynb
```

3. Service
```
$ sudo systemctl start docker           <-立刻啟用
$ sudo systemctl enable docker          <-重新後啟用
$ sudo systemctl status docker
```

4. Test (重新登入)
```
$ docker --version
Docker version 17.09.0-ce, build afdb6d4

$ docker run hello-world
Hello, World.
```



---
## MySQL CE
- 2017/11/26
> [Official MySQL](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)


1. 先到這邊手動下載[repo rpm](https://dev.mysql.com/downloads/repo/yum/), 再執行剛剛下載的那包rpm(版本不同, 底下指令也跟著不同)
```
$ sudo rpm -Uvh mysql57-community-release-el7-11.noarch.rpm 
```

2. 安裝MySQL Server(若要選擇不同的Release Series, 要再進去網頁熟讀第2點), 否則直接使用下列指令, 安裝最新版本(目前為5.7)
```
$ sudo yum install -y mysql-community-server
```

3. 啟動MySQL服務
```
$ sudo systemctl enable mysqld 
$ sudo systemctl start mysqld 
$ sudo systemctl status mysqld
```

4. 取得暫時密碼登入
```
$ sudo grep 'temporary password' /var/log/mysqld.log

$ mysql -uroot -p
```

5. 移除密碼複雜性驗證 && 更改密碼 && 建立使用者
```

> ALTER USER 'root'@'localhost' IDENTIFIED BY '<new password>';

> uninstall plugin validate_password;

> CREATE USER 'tony'@'%' IDENTIFIED BY '<password>';

> GRANT ALL ON *.* TO 'tony'@'%';
```



---
## Docker - MySQL
- 2017/10/01
- 前提, 已經下載並安裝好
	1. Docker
	2. MySQL

> [Severalnines Blog - MySQL Docker Container](https://severalnines.com/blog/mysql-docker-containers-understanding-basics)


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
## MongoDB CE
- 2017/11/26
> [Official MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)

1. repo [決定自己要哪個版本]()
```
$ sudo vi /etc/yum.repos.d/mongodb-org-3.4.repo

[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
```

2. install
```
$ sudo yum install -y mongodb-org
```

3. service
```
$ sudo ystemctl start mongod.service
$ sudo systemctl enable mongod.service
$ systemctl status mongod.service
```

4. other
```
$ mongodb --version
MongoDB shell version v3.4.10
git version: 078f28920cb24de0dd479b5ea6c66c644f6326e9
OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
allocator: tcmalloc
modules: none
build environment:
    distmod: rhel70
    distarch: x86_64
    target_arch: x86_64

$ ps auxw | grep mongod
mongod   10015  0.9  1.2 976812 45716 ?        Sl   14:23   0:01 /usr/bin/mongod -f /etc/mongod.conf
tonynb   10146  0.0  0.0 112672   964 pts/1    S+   14:25   0:00 grep --color=auto mongod
```



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
## Visual Studio Code
- 2017/11/27
> [Official vscode](https://code.visualstudio.com/docs/setup/linux)

1. repo && install
```
$ sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc

$ sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

$ sudo yum -y install code
```






---
## install Anaconda (python3.6.1)
- 2017/11/26
> [Official Anaconda](https://www.continuum.io/downloads)


1. Download && Install
```
$ wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh

$ su bash ./Anaconda3-5.0.1-Linux-x86_64.sh
```

2. Environment 
```
$ vi .bashrc
export anaconda_HOME="/opt/anaconda3/"
export PATH=$anaconda_HOME/bin:$PATH

$ source .bashrc

$ python --version
Python 3.6.3 :: Anaconda, Inc.
```



---
## Redis
- 2017/11/26 (2018/05/15 update)
- [Official Redis](https://redis.io/download)
- [cc not found 解法1](https://stackoverflow.com/questions/35634795/no-acceptable-c-compiler-found-in-path-while-installing-the-c-compiler)
- [cc not found 解法2](https://unix.stackexchange.com/questions/287913/cc-command-not-found-when-compiling-a-pam-module-on-centos?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- [jemalloc not found 的解說1](https://blog.csdn.net/bugall/article/details/45914867)
- [jemalloc not found 的解說2](http://www.ywnds.com/?p=6957)

1. Download && Install
```sh
$ wget http://download.redis.io/releases/redis-4.0.2.tar.gz

$ tar xzf redis-4.0.2.tar.gz

$ mv redis-4.0.2.tar.gz ~/.

$ ~/cd redis-4.0.2

$ make

# 如果 make 有問題, 再往下看---------------
# *** 如果出現「cc not found」
# 我直接把超大一包的'Development Tools'裝近來(殺雞用牛刀, 但可用!)
$ sudo yum groupinstall 'Development Tools'

# *** 如果出現「jemalloc/jemalloc.h: No such file or directory」
# 解法: 
# 1. 編譯時, 使用「make MALLOC=libc」來迫使 Redis使用 libc(比起 jemalloc 不那麼有效率) 取代 Redis預設的 jemalloc(應該是 記憶體管理的模組)
# 2. 安裝 jemalloc 

# 底下採用 解法2 -> 安裝 jemalloc
$ # a. 安裝 EPEL
$ # b. 安裝 jemalloc
$ # c. 完成後, 再執行 「make MALLOC=/usr/local/jemalloc/lib」編譯. (不曉得為何 make test 依然發生錯誤), 不過可正常使用了
# -------------------------------------------
```

2. Create redis-server - Terminal 1
```sh
$ src/redis-server
```

3. Run redis-client - Terminal 2
```sh
$ src/redis-cli
```


---
## Git (CentOS7 default git v-1.8 )
- 2017/11/26

> [How To Install Git on CentOS 7](https://blacksaildivision.com/git-latest-version-centos) 

1. Dependancy
```
$ sudo yum install autoconf libcurl-devel expat-devel gcc gettext-devel kernel-headers openssl-devel perl-devel zlib-devel -y
```

2. [Choose a version](https://github.com/git/git/releases) ( 以2.14.3版為例 )
```
$ wget https://github.com/git/git/archive/v2.14.3.tar.gz
```

3. Install
```
$ tar zxf git-2.14.3.tar.gz

$ cd git-2.14.3/

$ make clean

$ make configure
GIT_VERSION = 2.14.3
    GEN configure

$ ./configure --prefix=/usr/local

$ make

$ sudo make install

$ git --version
git version 2.14.3
```






---
## net-tools
- 2017/11/26
> [centos7 最小化安装 無 ifconfig,netstat 的安装](http://www.cnblogs.com/cocoajin/p/4064547.html)

```
$ ifconfig
bash: ifconfig: command not found

$ yum install -y net-tools

$ ifconfig
success!
```



---
## VLC
- 2017/11/26

> [How to Install EPEL on CentOS 7](https://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/)

> [How To Install VLC On CentOS 7](https://www.unixmen.com/install-vlc-centos-7/)

> [install vlc on CentOS7](https://stackoverflow.com/questions/29443096/how-to-install-vlc-on-centos7-from-terminal)


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



## teamviewer
- 2018/02/07

> [Install TeamViewer on CentOS 7 / RHEL 7](https://community.teamviewer.com/t5/Knowledge-Base/How-to-install-TeamViewer-Host-for-Linux/ta-p/6318?_ga=2.2833328.1279667713.1518017393-1552891207.1518017393)

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


---
## 7zip
- 2017/11/26
> [e Learning](http://elearning.wsldp.com/pcmagazine/extract-7zip-centos-7/)

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



---
## install nginx
- 2018/03/19
- [Official](http://nginx.org/en/linux_packages.html#stable)
- [參考這邊](https://dotblogs.com.tw/grayyin/2017/05/18/183117)

1. 增加 yum repo
```sh
$ sudo vi /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=1
enabled=1
```
2. 到 [這邊](http://nginx.org/keys/nginx_signing.key) 把 GPG-keys Copy
```sh
$ vi nginx_signing.key
# 把 keys內容貼上

$ sudo rpm --import nginx_signing.key
```
3. 安裝~
```sh
$ sudo yum install -y nginx

$ sudo systemctl start nginx

$ sudo systemctl enable nginx
```

4. 其他補充及設定
```sh
$ nginx -v
nginx version: nginx/1.13.9

# 設定檔位置
$ sudo vi /etc/nginx/nginx.conf

# 預設主機配置  
$ sudo vi /etc/nginx/conf.d/default.conf
```


---
## install Apache
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


---
## install nginx
- 2018/03/13
- [安裝 Nginx](http://nginx.org/en/linux_packages.html#stable)

```sh
# 1. 建立 repo
$ sudo vi /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/         
# baseurl=http://nginx.org/packages/OS/OSRELEASE/$basearch/   # 看官方說明吧
gpgcheck=1
enabled=1

# 2. 增加 RPM package的 數位簽章
# 到這 Copy~~ 
# http://nginx.org/keys/nginx_signing.key
$ vi nginx_signing.key
# 貼上去, 在執行匯入
$ sudo rpm --import nginx_signing.key

# 3. 安裝
$ sudo yum install -y nginx
```


---
## install scala (不完整)
- 2017/06/??

> [Official Scala](https://www.scala-lang.org/download/)

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




---
## install Python (不完整)
```sh
$ wget <python>

$ tar xf <python>.tar.xz
$ cd <python>

$ ./configure --enable-loadable-sqlite-extensions \
              --enable-shared \
              --prefix="\opt\python3"
$ make
$ sudo make install
$ ldconfig
```

安裝完後,開始設定環境變數（略）

底下開始安裝python3的pip
```sh
$ wget -0 /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py"
$ export PYTHON_PIP_VERSION=9.0.1
$ python3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION"
$ pip3 install --no-cache-dir --upgrade --force-reinstall "pip==$PYTHON_PIP_VERSION"
```




---
## Install jdk1.8 
- 2018/03/21
> [Official Orical jdk](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)


1. 移除 open-jdk...!!?? 網路上有阿貓阿狗會教, 把 open-jdk移除後, 再來安裝 oracle-jdk, 但是這樣會把 libore-office的依賴套件也一併移除(沒辦法使用 Linux的 Excel了QAQ). 所以我不這麼作. 因此, 第一步, 啥都不用作!

2. Donwload && Install
```sh
$ wget http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.tar.gz

$ tar -zxf jdk-8u161-linux-x64.tar.gz
$ sudo mv jdk1.8.0_161/ /opt/jdk1.8
$ echo 'export java_HOME="/opt/jdk1.8/"' >> ~/.bashrc
$ echo 'export PATH=$java_HOME/bin:$PATH' >> ~/.bashrc

# 重起 terminal後
$ which java
/opt/jdk1.8/bin/java

$ which javac
/opt/jdk1.8/bin/javac

$ java -version
java version "1.8.0_161"
Java(TM) SE Runtime Environment (build 1.8.0_161-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.161-b12, mixed mode)
```


---
## Install KVM
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


---
## Install wget
- 2018/05/15
安裝最輕量化的 CentOS7, 沒有 `wget`這東西

```sh
$ sudo yum install wget
```


## Install gcc
- 2018/05/15
- [cc: Command not found](https://unix.stackexchange.com/questions/287913/cc-command-not-found-when-compiling-a-pam-module-on-centos?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
```sh
# 不知道這是不是一個好的解法... 一口氣安裝超級大一包

```