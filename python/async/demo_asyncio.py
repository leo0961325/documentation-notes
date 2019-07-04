"""
### Python 3.5 以後的玩法
async def delayed_result(delay, result):    <- 此為 generator function
    await from asyncio.sleep(delay)
    ...

### Python 3.4(含) 以前的玩法
@asyncio.coroutine
def delayed_result(delay, result):          <- 此為 coroutine function
    yield from asyncio.sleep(delay)
    ...
"""
import asyncio


async def delayed_result(delay, result):  # 此函式 為 v3.4 以前的寫法, 此為一個產生器
    print(22)
    await asyncio.sleep(delay) # 先返還 執行權, 在此會交付 「coroutine 物件」
    print(33)
    return result


lp = asyncio.get_event_loop()   # lp 為 asyncio.windows_events._WindowsSelectorEventLoop
print(11)
print(asyncio.iscoroutinefunction(delayed_result))      # 可判斷此 fn 是否為 coroutinefunction or generatorfunction
dd = delayed_result(1.5, 99)    # 1.5 秒後, 回傳 99
print(44)
print(type(dd))

x = lp.run_until_complete(dd)
# 等到 dd (其為 asyncio.Future) 完成時, run_until_complete 會回傳 dd(future) 的 結果 or 它拋出的例外

print(55)
print(x)

"""
11
True
44
<class 'coroutine'>
22  # 過 1.5 秒後, 才會繼續往下印
33
55
99
"""
