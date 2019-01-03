# 網路工具

## Linux - nslookup

某書說已不建議再使用


## Linux - traceroute

列出 ICMP 封包從 本機 -> 目的主機 中間經過的路徑(路由器), 但中繼路由器可能因為安全性考量, 而關閉這功能(導致無法回應)

```sh
traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  gateway (192.168.124.254)  2.963 ms  2.900 ms  2.860 ms
 2  * * *
 3  * * *
# ... 後略...
```

## Linux - dnsdomainname

```sh
$# dnsdomainname
tony.com

# 而 DNS Domain 建議作法是設在(如果不用 DNS 的話...)
# /etc/hosts
# xxx.xxx.xxx.xxx   os7.tony.com    os7    XXXXX    .....
# IP                FQDN            HOST1  HOST2    ...
# 外加
$# hostnamectl set-hostname os7
```

## Linux - hostname

```sh
# 可查 Domain
$# hostname
os7

# 可查 FQDN
$# hostname -f
os7.tony.com
```

## Linux - mail

```sh
$# mail -s "README" tony@tony.com
(信件內容~~~)
.           # ← 表示結束 or 按「Ctrl + D」

EOT

$# 
```


## Linux - dig

名稱查詢命令

Type  | Description
----- | ----------------
A     | IP
MX    | 郵件伺服器
NS    | 名稱伺服器
PTR   | IP 反查名稱
CNAME | 別名

```sh
# dig 指令工具所屬的套件
$# yum install -y bind-utils
# CentOS7 應該有預設安裝好了吧...

$# dig @[Name Server] [FQDN 或 Domain] [TYPE]

$# dig www.pchome.com.tw

; <<<>> DiG 9.9.4-RedHat-9.9.4-72.el7 <<<>> www.pchome.com.tw
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<<- opcode: QUERY, status: NOERROR, id: 5419
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:
;www.pchome.com.tw.             IN      A                       # 提出的查詢問題

;; ANSWER SECTION:
www.pchome.com.tw.      300     IN      A       210.59.230.39   # 查詢到的回答

;; Query time: 25 msec
;; SERVER: 192.168.2.115#53(192.168.2.115)                      # 本地使用的 DNS
;; WHEN: Mon Dec 24 14:06:44 CST 2018
;; MSG SIZE  rcvd: 62

```
