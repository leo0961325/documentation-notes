# 疑難雜症

- 2019/08/12
- https://blog.darkthread.net/blog/vs2017-git-ssl-issue/

公司內部 Gitlab 換憑證, 導致無法作 git pull

```bash
$# git pull
fatal: unable to access 'https://git.tgfc.tw/python-team/dayu.git/': SSL certificate problem: unable to get local issuer certificate

$# git config --global http.sslBackend schannel
# git config --global http.sslVerify false  # 把SSL驗證關掉, 也就是說如果網域被導向到其他, 你也不會知道, 所以不安全

$# git pull
# 即可正常
```
