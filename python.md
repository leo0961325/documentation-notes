

### Install python by tar ball
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




[Anaconda多环境多版本python配置指导](https://www.jianshu.com/p/d2e15200ee9b)

進入虛擬環境 (安裝完anaconda後)
```
# 印出所有的虛擬環境
$ conda info --envs
# conda environments:
#
ve                       /opt/anaconda3/envs/ve
root                  *  /opt/anaconda3

# 進入虛擬環境
$ source activate ve
$ source vemt/bin/activate

# 離開許你環境
$ source deactivate ve
```

---
Python中, 任何資料夾內如果有包含`__init__.py`的話, 這個資料夾就被視為是一個`package`, 如此一來就可以被 import


---

### shebang
```py
#! /usr/bin/python
# coding: utf-8

```

### 函式範例
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
