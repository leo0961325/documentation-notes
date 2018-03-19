# 使用 pyenv 控管python版本

[來源: https://github.com/pyenv/pyenv/wiki](https://github.com/pyenv/pyenv/wiki "pyenv home")

##### 2017/08/27

## 1. 安裝pyenv

### 安裝pyenv為例

1. 下載相關套件

    $ sudo curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

    - for Ubuntu

        $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev

    - for CentOS

        $ yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel

2. 設定環境變數 

    $ echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bashrc

    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc

    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc


## 2. 使用pyenv安裝及切換python版本

    $ pyenv install 3.5.1       安裝python3.5.1

    $ pyenv local 3.5.1         設定目前資料夾底下使用的python版本

    $ pyenv install 3.6.1       安裝python3.6.1

    $ pyenv uninstall 3.5.1     解壓縮python3.5.1

    $ pyenv global 3.6.1        設定目前使用者使用的python版本

    $ python --version          用來查看pyenv目前控管的那些python版本


## 4. 在特定python版本下,安裝套件

    $ pip install xxx


## 5. 切換不同開發環境時, 釋出及安裝相關套件

    - for user A

        $ pip freeze > requirement.txt

    - for user B
        
        $ pip install -r requirement.txt (就可以安裝req.txt裡頭的套件)