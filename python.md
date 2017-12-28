
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
