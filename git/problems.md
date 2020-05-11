# 疑難雜症

- 2019/08/12
- https://blog.darkthread.net/blog/vs2017-git-ssl-issue/

公司內部 Gitlab 換憑證, 導致無法作 git pull

```bash
$# git pull
fatal: unable to access 'https://git.company.tw/python-team/proj.git/': SSL certificate problem: unable to get local issuer certificate

$# git config --global http.sslBackend schannel
# git config --global http.sslVerify false  # 把SSL驗證關掉, 也就是說如果網域被導向到其他, 你也不會知道, 所以不安全

$# git pull
# 即可正常
```



********************************

- 2020/03/30

要嘗試 clone 專案, 發生錯誤: **Peer's Certificate issuer is not recognized.**

```bash
$# git clone https://HOST/PROJECT_OWNER/PROJECT.git demo
Cloning into 'demo'...
fatal: unable to access 'https://HOST/PROJECT_OWNER/PROJECT.git': Peer's Certificate issuer is not recognized.
```

參考: [這裡](https://stackoverflow.com/questions/19461833/what-does-this-error-message-imply-fatal-unable-to-access-httpsurl-peers)

```bash
### 比較不建議的做法
$# env GIT_SSL_NO_VERIFY=true git clone https://HOST/PROJECT_OWNER/PROJECT.git

```
