# zabbix

- 2019/07/23
- 監控用的


```bash
/etc/
    /zabbix/
        /zabbix-server.conf         # zabbix 設定主檔
```

# 結構

```bash
/zabbix/                        # zabbix-server 監控的軟體
    /zabbix_server.conf             # zabbix-server 設定主檔
```

#

admin 可做 Configuration 及 Administration


# zabbix_get

- [zabbix_get安装和使用](https://blog.csdn.net/u012062455/article/details/81777079)
- 2019/07/30

```bash
### zabbix-server 上安裝 zabbix-get
$# rpm -ivh http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-release-3.2-1.el7.noarch.rpm
$# yum install -y zabbix-get.x86_64

### Usage
$# zabbix_get -s 127.0.0.1 -p 10050 -k "system.cpu.load[all,avg15]"
0.060000

$# zabbix_get -s 127.0.0.1 -p 10050 -k "mysql.version"
mysql  Ver 14.14 Distrib 5.7.27, for Linux (x86_64) using  EditLine wrapper
```
