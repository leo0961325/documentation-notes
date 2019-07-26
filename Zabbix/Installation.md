# Docker-Zabbix

- [Docker-zabbix/zabbix-appliance](https://hub.docker.com/r/zabbix/zabbix-appliance)
- 2019/07/23
- 監控用的

```bash
### Server image
$# docker pull zabbix/zabbix-appliance:centos-4.0.10

### Server run
$# docker run --name zabapp \
    -p 7777:80 \
    -p 7778:10051 \
    -d zabbix/zabbix-appliance:centos-4.0.10
# 80 為 Web GUI 管理介面
# 10051 用作資料傳遞(接收)


### Agent image
$# docker pull zabbix/zabbix-agent:centos-4.0-latest

### Agent run
$# docker run --name zab-agent \
    -e ZBX_HOSTNAME="zabagent" \
    -e ZBX_SERVER_HOST="zabapp" \
    -d zabbix/zabbix-agent:centos-4.0-latest
# -v 外頭, 先準備好一份 Agent Config
# ZBX_HOSTNAME: Container hostname ; 設定檔的 Hostname
# ZBX_SERVER_HOST(default: zabbix-server): Zabbix Server/Proxy 的 IP or DNS. 設定檔的 Server
# (預設) 10050 用作資料傳遞(傳送)

### firewall
$# firewall-cmd --add-port=7777/tcp
$# firewall-cmd --add-port=7778/tcp


### 查看 log
$# docker logs zabapp

### 版本
$# zabbix_server --version
zabbix_server (Zabbix) 4.2.4
Revision 059af02 26 June 2019, compilation time: Jul 18 2019 12:41:59

Copyright (C) 2019 Zabbix SIA
License GPLv2+: GNU GPL version 2 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it according to
the license. There is NO WARRANTY, to the extent permitted by law.

This product includes software developed by the OpenSSL Project
for use in the OpenSSL Toolkit (http://www.openssl.org/).

Compiled with OpenSSL 1.1.1c  28 May 2019
Running with OpenSSL 1.1.1c  28 May 2019
```

id: Admin
pd: zabbix
