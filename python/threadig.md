# 並行 與 平行
## threading moduel - 多執行緒
- [threading](https://docs.python.org/3/library/threading.html)
- python 具有 [GIL](https://itw01.com/2TQBELW.html), 所以`少用它來做密集運算`

```py
import threading
class Haha(threading.Thread):
    def __init__(self, a):
        pass
    def run(self):  # ~原始的業務邏輯~
        pass

Haha(5).start() # ~執行緒邏輯~
```


### 阻斷
遇到 Block時, 自動讓出執行權


### Daemon 執行緒
```py
threading.Thread(target=None, daemon=True) # 此時為背景執行
```


### 安插執行續
```py
tb = threading.Thread(target=do_me_first)
tb.start()
tb.join()           # 插隊囉~~
# or tb.join(5)     # 給你插隊 5秒鐘做事
```


### 停止執行緒
```py
class Some:
    def gg(self):   # 執行緒 停止, 重啟, 暫停 的邏輯, 依需求實作
        pass    # 自行實作

    def run(self):
        pass

s = Some()
t = threading.Thread(target=s.run)
t.start()
# ...
s.gg()   # 停止執行續(注意是 s 而非 t)
```
