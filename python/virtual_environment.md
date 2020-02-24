# Python3 控制虛擬環境


## pipenv

- 比較新一代的虛擬環境管控




```bash
### 一開始, 使用 global pip 安裝 pipenv 於特定 project dir
proj$ pip install pipenv

### 安裝套件
proj$ pipenv install Sanic
Creating a virtualenv for this project…
Pipfile: D:\tmp\ssanic\Pipfile
Using c:\users\tony\appdata\local\programs\python\python37\python.exe (3.7.3) to create virtualenv…
[====] Creating virtual environment...Already using interpreter c:\users\tony\appdata\local\programs\python\python37\python.exe
Using base prefix 'c:\\users\\tony\\appdata\\local\\programs\\python\\python37'
New python executable in C:\Users\tony\.virtualenvs\ssanic-qZ1hHV8u\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: C:\Users\tony\.virtualenvs\ssanic-qZ1hHV8u
Creating a Pipfile for this project…
Installing Sanic…
Adding Sanic to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (acb8a0)!
Installing dependencies from Pipfile.lock (acb8a0)…
  ================================ 5/5 - 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
# 結束後, proj 內會出現:
# Pipfile : 紀錄安裝了那些套件
# Pipfile.lock

###
proj$
```

## virtualvenv

- 古老的虛擬環境管控方式

```bash
### virtualenv
pip install virtualenv virtualenvwrapper    # 是 pip 而非 pip3

echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv -p /usr/local/bin/python3 <ENV_NAME>
mkdir ~/<ENV_NAME>
cd <ENV_NAME>
setvirtualenvproject .

workon <ENV_NAME>
deactivate <ENV_NAME>

```

## 使用 pyenv 控管python版本

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