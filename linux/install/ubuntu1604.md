# Ubuntu16.04


## apt 無法執行動作 (被lock住的解法)
- [更新套件被占用](http://hep1.phys.ntu.edu.tw/~phchen/apfel/linux/install/problem-solving.txt)
- 2018/04/23

更新套件庫或安裝套件遇到「無法將 /var/lib/dpkg/lock 鎖定」 解法
```sh
# 若出現 /var/lib/dpkg/lock 鎖定 - open (11: 資源暫時無法取得)
# 原因是使用 apt-get, aptitude, synaptic, software-center …等等的程式還沒有關閉

# 如果忘記是那個程式沒關的話，可使用 lsof(list open files) 找出是那個程序佔用檔案, 再用手動關閉或是使用指令的方法, 殺掉正在執行程序

# 1. 用 lsof 找出目前是那個程序在使用 /var/lib/dpkg/lock

$ sudo lsof /var/lib/dpkg/lock
# 從訊息可看出目前是 aptitude 在佔用 /var/lib/dpkg/lock, 可以找找看是不是剛使用 aptitude, 如果有的話等程式跑完應該就可 更新/安裝了

COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
aptitude 8891 root    4uW  REG   6,47        0 248214 /var/lib/dpkg/lock

# 2. 若找出來的程序是己經沒在執行又遺忘在那開啟的話, 直 kill~. 而這裡是 aptitude 它的 PID 為 8891, 殺掉就能正常使用

$ sudo kill 8891

# 如果出現
E: dpkg was interrupted, you must manually run 'sudo dpkg --configure -a' to correct the problem. 

# 就輸入
$ sudo dpkg --configure -a
```



## install mysql5.7
[MySQL官方教學](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#apt-repo-fresh-install)

```sh
1. 連到這裡  https://dev.mysql.com/downloads/file/?id=472914
抓官方的repo

2.加入官方repo
sudo dpkg -i mysql-apt-config_0.8.8-1_all.deb

3. 更新一下apt
sudo apt-get -y update

4. 安裝mysql server
sudo apt-get -y install mysql-server

5. 服務
sudo service mysql status
sudo service mysql stop
sudo service mysql start

```

---

## MongoDB3.4
[官方教學](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition)

安裝
```sh
1. 加入官方public key
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

2. 建立16.04版的list file (這啥鬼...)
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

3. update
sudo apt-get update

4. 安裝
sudo sudo apt-get install -y mongodb
```

## Docker
- 2018/01/30

[官方教學](https://docs.docker.com/install/linux/docker-ce/ubuntu/#os-requirements)

```sh
$ sudo apt-get update

$ sudo apt-get install docker-ce

$ apt-cache madison docker-ce
# 生產環境底下, 避免永遠都預設使用最新版

$ sudo apt-get install docker-ce=<VERSION>

$ sudo usermod -aG docker <userName>
# 使目前使用者能使用 Docker ((重新登入!!))
```

## vim
-2018/01/30

[Linux 安裝 vim](https://www.phpini.com/linux/linux-install-vim)

把 vim想像成有顏色的 vi
```sh
$ sudo apt -y install vim

$ cd

$ vi .vimrc
```
[參考這篇](https://askubuntu.com/questions/296385/backspace-in-insert-mode-in-vi-doesnt-erase-the-character), 在 `.vimrc` 加入這幾行
```
set nocompatible
set backspace=2
```