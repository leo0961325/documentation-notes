# asynchronous 非同步架構

如果一支程式經常 存取磁碟 (CPU總是得等待磁碟回覆才能接著作事), 那表示這支程式是 `I/O bound` 的程式碼. 改善效率的解法, 把此程式改成 `非同步 (async)`, 改完後, 此程式就變成 `非阻斷 (nonblocking)`, 可以大幅增進效能. 而 `非同步async 架構`, 有時候也被稱為 `事件驅動(event-driven) 架構`, 

非同步的架構分為三類:
1. 多工 (multiplexed async architecture)
2. 事件 (callback-based)
3. 協程 (coroutine-based)

## 1. 多工 multiplexed

程式碼會不斷追蹤 `I/O channels`, 如果程式處理中的 `I/O` 還沒完成, 那麼程式就進入了 `block`, 直到 I/O channel 完成, 才會喚醒 `blocking wait`, 程式才會繼續作後續的工作.

Python有許多 低階模組 支援多工的非同步架構, 但建議使用高階的 `selectors模組`



## 2. 事件 event



## 3. 協程 coroutine










---
---
---

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


# uvloop: Blazing fast Python networking

- 2019/04/22
- https://magic.io/blog/uvloop-blazing-fast-python-networking/
- `event loop` 為 `asyncio` 的核心
- `uvloop` 基於 `libuv` 用 Cython 來寫的
    - `libuv` 為跨平台的異步 I/O lib, 也被 nodejs 所用
- `uvloop` 實作所有 asyncio event loop APIs
