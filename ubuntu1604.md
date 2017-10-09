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
