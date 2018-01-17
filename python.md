
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

# 離開許你環境
$ source deactivate ve
```

---
Python中, 任何資料夾內如果有包含`__init__.py`的話, 這個資料夾就被視為是一個`package`, 如此一來就可以被 import
