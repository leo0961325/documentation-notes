# CentOS6.9 安裝備註
- 這個有點舊了, 2017/05 以前的東西, 將來「若吃飽太閒」, 再回來整裡

```sh
$ cat /etc/redhat-release
CentOS release 6.9 (Final)

$ uname -a
Linux tony 2.6.32-696.1.1.el6.x86_64 #1 SMP Tue Apr 11 17:13:24 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```

--------------------------------------------
讓使用者成為pu
```
$ su
# chmod u+w /etc/sudoers
# vim /etc/sudoers
於ALL=(ALL)   ALL下一行增加
<user>=(ALL)   ALL
:wq
# chmod u-w /etc/sudoers
重新登入terminal即可
```
--------------------------------------------
安裝git
https://www.liquidweb.com/kb/how-to-install-git-on-centos-6/

$ sudo yum update

$ yum install git

$ git --version

$ git config --global user.name "<userName>"

$ git config --global user.email "<email>"
--------------------------------------------
安裝python3.5
www.jianshu.com/p/6199b5c26725

佈置環境
$ sudo yum groupinstall 'Development Tools'
$ sudo yum install zlib-devel bzip2-devel  openssl-devel ncurses-devel

下載python3.5.2
$ wget  https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz

編譯
$ tar Jxvf  Python-3.5.2.tar.xz
$ cd Python-3.5.2
$ ./configure --prefix=/usr/local/python3
$ sudo make
$ make install

設定環境變數
$ echo 'export PATH=$PATH:/usr/local/python3/bin' >> ~/.bashrc

替換掉python2
$ sudo rm   /usr/bin/python (非必要!!! 盡量不要...)
$ sudo ln -sv  /usr/local/bin/python3.5 /usr/bin/python

更新yum配置
$ ll /usr/bin | grep python
$ sudo vim /usr/bin/yum
#!/usr/bin/python改为#!/usr/bin/python2.6，保存退出。 (非必要!!! 盡量不要...)

往後, $ python3.5即可執行3.5.2
(因為已經建立了python3.5的軟連結, 並將他加到.bashrc)

安裝pip
$ wget https://bootstrap.pypa.io/get-pip.py

(底下這一步會有權限問題...思考一下就能解了)
$ python3 get-pip.py 

--------------------------------------------
安裝Oracle-Java 1.8
(徐凡耘老師上課資料)

下載及安裝jdk1.8
$ http://ftp.wsisiz.edu.pl/pub/pc/pozyteczne%20oprogramowanie/java/jdk-8u131-linux-x64.rpm
$ sudo rpm -ivh jdk-8u131-linux-x64.rpm

$ 建立軟連結
$ sudo ln -s /usr/java/jdk1.8.0_131/ /usr/java/java

加入連結目標
$ sudo vi /etc/profile
export JAVA_HOME=/usr/java/java
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib/rt.jar
export PATH=$PATH:$JAVA_HOME/bin

$ java -version

--------------------------------------------
安裝7zip for CentOS 6
https://techglimpse.com/unzip-7z-archive-linux-install-extract/

$ wget ftp://195.220.108.108/linux/dag/redhat/el7/en/x86_64/dag/RPMS/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm

$ sudo rpm -ivh rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm

--------------------------------------------
Install VLC Media Player
https://www.tecmint.com/install-vlc-media-player-in-rhel-centos-fedora/

$ sudo rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

$ sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el6/x86_64/nux-dextop-release-0-2.el6.nux.noarch.rpm

$ yum info vlc

$ sudo yum install vlc

$ vlcv

$ sudo yum update vlc

--------------------------------------------
Install Google Chrome
https://www.tecmint.com/install-google-chrome-on-redhat-centos-fedora-linux/

$ sudo yum update google-chrome-stable

$ sudo touch /etc/yum.repos.d/google-chrome.repo

$ sudo echo "[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" > /etc/yum.repos.d/google-chrome.repo

$ yum info google-chrome-stable

$ sudo yum install google-chrome-stable

--------------------------------------------
安裝VS Code (好像要安裝完Chrome後才能裝...)
https://code.visualstudio.com/docs/setup/linux

$ sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc

$ sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

$ yum check-update

$ sudo yum install code

.......GG 

--------------------------------------------
安裝selenium
http://seleniumhq.github.io/selenium/docs/api/py/index.html
https://github.com/mozilla/geckodriver/releases

--------------------------------------------
geckodriver
http://seleniumhq.github.io/selenium/docs/api/py/index.html
selenium for python用, 建立軟連結到 /usr/local/bin


--------------------------------------------
安裝中文字型
$ sudo yum install cjkuni-*
--------------------------------------------
--------------------------------------------
--------------------------------------------
