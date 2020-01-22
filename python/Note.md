
## 接收 function 作為簡單的介面, 而非使用類別

> 有些 python API 允許接收一個 function 來自訂行為. 這些 `掛接器(hooks)` 會在 API 執行的時候, 被用來回呼(callback) 你的程式碼.
  ex: list 的 sort 接收選擇性的 key 引數, 它被用來決定每個索引用於排序的值.
  如下範例, sort() 內的 function 則生為 `掛接器(hooks)`

```py
>>> names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
>>> names.sort(key=lambda x: len(x))
>>> print(names)
['Plato', 'Socrates', 'Aristotle', 'Archimedes']

```



# 異部

- 2020/01/22
- https://realpython.com/python-concurrency/#cpu-bound-synchronous-version

```py
import asyncio
import aiohttp

# ... 略...

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:  # <- context manager
    # Inside that context manager, it creates a list of tasks using asyncio.ensure_future(), which also takes care of starting them. Once all the tasks are created, this function uses asyncio.gather() to keep the session context alive until all of the tasks have completed.
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    # ... 略...
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))  # py3.7, 可使用 asyncio.run(XXX) 來代替
    # ... 略...
```
