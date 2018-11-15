

# SSHTunnel

- 2018/09/29

在 localhost`A` 透過 `C` 訪問 `B`

- A: 169.254.10.30
- B: 169.254.10.10 (先安裝 `httpd`)
- C: 169.254.10.20

語法 : `ssh -L 本地Port:目的IP:目的Port user@跳板IP`

```sh
# 透過 tony@169.254.10.20 訪問 169.254.10.10:80, 並將結果回傳到本地的 8088 port (在A電腦執行)
$ ssh -L 8088:169.254.10.10:80 tony@169.254.10.20

# 瀏覽器~~ 「localhost:8088」 就看到網頁了~~
# 但是不知道為什麼　curl會出現
# curl: (7) Failed to connect to localhost port 8088: Connection refused
```


# 非正規 Port

```sh
### 1. 改組態
$# grep -n Port /etc/ssh/sshd_config
17:#Port 22
18:Port 6868
101:#GatewayPorts no

### 2. 重啟SSHD
$# systemctl restart sshd
$# systemctl status sshd

### 3. SELinux
$# semanage port -a -t ssh_port_t -p tcp 22
$# semanage port -l -C
SELinux Port Type       Proto    Port Number
ssh_port_t              tcp      6868

### 4. 防火牆
$# firewall-cmd --add-port=6868/tcp
$# firewall-cmd --add-port=6868/tcp --permanent
```


