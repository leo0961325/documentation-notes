
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

