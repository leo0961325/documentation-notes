# Ubuntu16.04

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
