# SSL - HTTPS

- 2018/11/20
- [SSL For Free](https://www.sslforfree.com/)


# Apache 手動篇

1. DNS 設好 A 紀錄

Name   | Type | Value       | TTL
------ | ---- | ----------- | ---
`FQDN` | A    | (PUBLIC IP) | 60

2. 啟動你的 Web Server, 開防火牆, Permission, SELinux(if Enforcing)
3. 修改你的 `/etc/hosts` (假設為 `demo`)
4. 前往 [SSL For Free](https://www.sslforfree.com/), 填寫 FQDN (`demo.DOMAIN`)
5. Manual Verification
    1. Download File (檔案裏頭一堆看不懂的 `HASH`), 假設該檔名為 Zr2Q7
    2. 放到 Web Server 站台的 {DocumentRoot}/.well-known/acme-challenge/Zr2Q7
    3. 啟動你的 Web Server
    4. 開防火牆, 權限, SELinux(if Enforcing)
    5. 瀏覽器進入你的 Web Server (http://YOUR_FQDN/.well-known/acme-challenge/Zr2Q7), 應該能看到一堆 `HASH`
    6. 點選 `Download SSL Certificate`
        1. 將 Certificate 存成 `xxx.crt`
        2. 將 Private Key 存成 `yyy.key`
        3. 將 CA Bundle 存成 zzz.crt (不知道啥場合用得到它...)
    7. yum install -y mod_ssl
    8. 編輯 `/etc/httpd/conf.d/ssl.conf`
        1. SSLCertificateFile 設定為 `xxx.crt` 的完整路徑
        2. SSLCertificateKeyFile 設定為 `yyy.key` 的完整路徑
    9. 重啟 httpd
    10. https://YOUR_FQDN   新鮮的 https 出爐~

