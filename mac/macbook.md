# printscreen

- command + shift + 3 > 畫面儲存到桌面 （printscreen)
- command + 
- command + shift + 4 > 選取區塊, 存到桌面

# 安裝 homebrew

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


```

# 製作 Open With VSCode

- https://blog.csdn.net/u013069892/article/details/83147239

![](./img/macbook_service_quick_start.png)

1. command + space
2. automator
3. 快速動作 > 選擇
4. (左)工具程式 > (中)執行Shell工序指令 拖拉到右邊
5. (上)工作流程接收目前的 > 檔案夾
6. (上)位置 > Finder
7. 裡面輸入
```bash
for f in "$@"
do
    open -a "Visual Studio Code" "$f"
done
```


```bash
### ~/.bash_profile
alias ls='ls -G'
alias ll='ls -lG'
alias lla='ll -a'

PS1='[\u@\h \W]\$ '
```


```bash
### ~/.vimrc
set expandtab
set tabstop=4
set shiftwidth=4
set nu
set ai
set autoindent
set nocompatible
```



```bash
==> openssl
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

openssl is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have openssl first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile

For compilers to find openssl you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl/include"
```


```bash
### 自簽憑證位置
/Users/tony/Library/Application Support/Certificate Authority
```
