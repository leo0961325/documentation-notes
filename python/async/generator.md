# generator

- 2019/07/29

![generator](/img/generator.png)

## yield

- iterate 是資料處理的基礎 (一次一個) ; Iterator 已經被實作到 python 之中
- yield 關鍵字可建構 generator, 它具備 iterator 的功能
- 每個 generator 都是一種 iterator

```python
### demo_generator_range.py

range(5)            # range(0, 5)
type(range(5))      # <class 'range'>
list(range(5))      # [0, 1, 2, 3, 4]

# range(5) 取得的是類似 generator 的物件
```

```python
### demo_sentence.py
# 流暢的 Python p.412
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):       #
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):     # 可以改變 Sentence instance 印出來的樣子
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('Thank god in Friday')
print(s)    # Sentence('Thank god in Friday')

for ww in s:
    print(ww)
# Thank
# god
# in
# Friday
```

上面範例的 Sentence 是可迭代的. 當 解釋器 `__get__` 需要 iterator x 的時候, 它會呼叫 iter(x)

物件是否實作 `__iter__`
  - Y: 用它取得 iterator
  - N: 是否實作 `__getitem__`
    - Y: 建立 iterator, 依序由 index=0 開始迭代
    - N: TypeError
