# OpenSSL
- 2018/08/06
- [金鑰與憑證的管理](http://ijecorp.blogspot.com/2014/03/openssl.html)
- [OpenSSL官網](https://www.openssl.org/)



# 名詞

- TLS : Transport Layer Security
- SSL : Secure Sockets Layer
- CA : Certification Authority, 憑證授權中心
- CSR : Certificate Signing Request, 憑證簽署請求



# enable https

要讓 `Web Service` 能夠支援 `SSL`, 必須要作下面幾件事情:
1. 產生 `Private Key`
2. 產生 `CSR`, 並將此 CSR 傳給 `CA`
3. 把 CA 所提供的 `憑證(Certificate)` 安裝在 Web Server


## 利用 OpenSSL 來達成 (CentOS7)

```sh
# 使用 openssl 產生 private key, 金鑰長度為 2048 bits 
$ openssl genrsa -out foobar.key 2048
# 底下會要你輸入 private key 的一堆基本資料... 包含 private key 密碼
# 產生出來的 foobar.key 又稱為 "RSA private key"

# 使用 RSA private key 加密生成 未經簽屬的 憑證(CSR)
$ openssl req -new -key foobar.key -out foobar.csr
# 然後又是要你輸入一堆此CA憑證的基本資料
# 產生出來的 foobar.csr 為 要送到CA機構去申請的文件檔

# 可用來檢查 CSR 的內容是否正確(不太懂...)
$ openssl req -text -in CSR.csr -noout

# 僅產生 私有憑證(不開放到公網域) - 自我簽署憑證
$ openssl x509 -req -days 3650 -in CSR.csr -signkey private.key -out self-signed.crt
# 會產生一個 pem格式的憑證內容, 放在 self-signed.crt
# 

# 直接從 private key 產生 自我簽屬憑證
$ openssl req -new -x509 -days 365 -key private.key -out self-signed-2.crt
```
