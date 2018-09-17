

# Install python by tar ball
- 2018/02/23
```sh
$ wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz

$ tar xf Python-3.5.2.tar.xz

# 編譯及安裝
$ ./configure --prefix=/opt/python352
$ make
$ sudo make install 

# 改變擁有者
$ sudo chown -R tonynb:tonynb /opt/python352

# 建立呼叫指令
$ mkdir ~/bin
$ ln -s /opt/python352/bin/python3.5 ~/bin/py

# 環境變數
$ echo 'alias py="/opt/python352/bin/python3.5"' >> ~/.bashrc
# or
$ echo 'export python_home=~/bin/' >> ~/.bashrc
$ echo 'export PATH=$python_home:$PATH' >> ~/.bashrc

```


```sh
$ pip install --upgrade setuptools
```



[Anaconda多环境多版本python配置指导](https://www.jianshu.com/p/d2e15200ee9b)

進入虛擬環境 (安裝完anaconda後)
```sh
### Python 虛擬環境
$ conda create -n <Env Name>        # Linux   用法
$ python -m venv <Env Name>         # Windows 用法

# 印出所有的虛擬環境
$ conda env list
# conda environments:
#
ve                       /opt/anaconda3/envs/ve
root                  *  /opt/anaconda3

# 進入虛擬環境
$ source activate <Env Name>        # Linux 用法
$ source vemt/bin/activate          # Windows 用法

# 離開虛擬環境
$ source deactivate <Env Name>

# 移除
$ conda env remove -n <Env Name>

# Using pip in an environment
$ conda install -n <Env Name> pip

$ which pip
~/anaconda3/envs/<Env Name>/bin/pip
```


## 使用 python3 的 virtualenv 及 virtualenvwrapper
```sh
# 進入 su
apt-get install -y python3-pip python3-dev		# 抓 python3用的 pip
pip3 install --upgrade pip						# 升級 pip3
pip3 install virtualenv virtualenvwrapper		# 用 pip3 安裝 虛擬環境
# 請確定安裝後, 最後面有出現「Successfully installed ...」的字樣
```

### 2. 設定
```sh
# 進入 su
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv -p /usr/bin/python3 bis
mkdir bis
cd bis
setvirtualenvproject .
```

---
Python中, 任何資料夾內如果有包含`__init__.py`的話, 這個資料夾就被視為是一個`package`, 如此一來就可以被 import


---

# shebang
```py
#! /usr/bin/python
# coding: utf-8

```

# pip
```sh
$ pip freeze

$ pip freeze -l     # 只顯示目前環境安裝的套件

$ pip freeze > requirement.txt

$ pip install -r requirement.txt
```

# 函式範例
```py
>>> a = 1
>>> type(a)
<class 'int'>
>>>
>>> isinstance(a, int)
True

>>> dict.fromkeys('hello', 2)
{'h': 2, 'e': 2, 'l': 2, 'o': 2}

>>> 
```

# configureParser

- configureParser.py
```py
import configparser

# 讀取外部組態檔
def getConfig(iniPath):
    config = configparser.ConfigParser()
    config.read(iniPath)
    dbhost = config.get('Section_A', 'sql_dbhost')
    user = config.get('Section_A', 'sql_id')
    passwd = config.get('Section_A', 'sql_pd')
    return dbhost, user, passwd
#

def mainFunction():
    iniPath = './house.ini'
    dbhost, user, passwd = getConfig(iniPath)
#
```

- house.ini
```ini
[Section_A]
sql_dbhost=localhost
sql_pport=3306
sql_id=tony
sql_pd=12345687


[Section_B]
# 放其他的...
```

# 環境變數

```py
import os
os.environ['PATH']
```