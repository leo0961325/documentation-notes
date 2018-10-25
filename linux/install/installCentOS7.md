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

1. Dependancy package && Install
```sh
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2

$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

$ sudo yum install -y docker-ce
```

2. Authority
```sh
$ cat /etc/group | grep docker
docker:x:983:

$ sudo usermod -aG docker $USER

$ cat /etc/group | grep docker
docker:x:983:tonynb
```

3. Service
```sh
$ sudo systemctl start docker           <-立刻啟用
$ sudo systemctl enable docker          <-重新後啟用
$ systemctl status docker
```

4. Done
```sh
$ docker --version
Docker version 18.03.1-ce, build 9ee9f40

# 無法執行的話, 重新登入就可以了
$ docker run hello-world
Hello, World.
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



# Git (CentOS7 default git v-1.8 )
- 2017/11/26
-  [How To Install Git on CentOS 7](https://blacksaildivision.com/git-latest-version-centos) 
- [Choose a version](https://github.com/git/git/releases) ( 以2.14.3版為例 )

1. Dependancy
```sh
# 所需套件
$# yum install -y autoconf libcurl-devel expat-devel gcc gettext-devel kernel-headers openssl-devel perl-devel zlib-devel

# 下載
$ wget https://github.com/git/git/archive/v2.14.3.tar.gz

# Install
$ tar zxf v2.14.3.tar.gz
$ cd git-2.14.3/
$ make clean
$ make configure
GIT_VERSION = 2.14.3
    GEN configure

$ ./configure --prefix=/usr/local
$ make

$# sudo make install

$ git --version
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
$ curl http://nginx.org/keys/nginx_signing.key > nginx_signing.key
$ sudo rpm --import nginx_signing.key

# 2. 建立 Yum Repo
$ sudo vim /etc/yum.repos.d/nginx.repo
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



# Install jdk1.8 (不完整)

- 2018/03/21
- [Official Orical jdk](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)


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





# 備註

- $basearch : x86_64 (位元架構)
- $releasever : CentOS7 的 7 (大版本號)
