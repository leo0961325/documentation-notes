# Python magic methods

## `__bases__`
- 回傳 父類別們 (tuple)
- 類別專屬的屬性 (實例無此屬性)
- 此屬性無法被 unbind

```python
### __bases__ 用途
class Traffic: pass

class Tools: pass

class Car(Traffic, Tools): pass

Car.__bases__ # (<class '__main__.Traffic'>, <class '__main__.Tools'>)
```


## `__class__`
- 每個 instance of object 都有個 `__class__` 屬性, 參考至 instance 建構時所使用的 class
- 而 class 本身也有個 `__class__`, 它參考的就是 `<class 'type'>`
- 每個 class 也是個 object, 是 type 類別的 instance
- 可使用 `instance.__class__` 或 `type(instance)` 來看出, instance 從哪個類別建構出來的
- 此屬性無法被 unbind

```py
class Demo: pass

print(Demo)    # <class '__main__.Demo'>
type(Demo)     # <class 'type'>
d = Demo()
d.__class__    # <class '__main__.Demo'>
d.__class__()  # <__main__.Demo object at 0x7f87b123edd0>
```


## `__delete__(self, instance)`
- object 若有綁定 `__delete__`, 則此物件稱之為 `Descriptor(描述器)` / `覆寫式描述器(Overriding Descriptor)` / `Data Descriptor(資料描述器)` (實作了 描述器協定)
- 如果 instance.attr1 與 `instance.__dict__['attr1']` 同名, 則**前者**優先


## `__dict__()`
- `class A: pass` 背後, (除非有定義 `__slots__`) 否則會自動創建 `__dict__`(類別or實例 都會有這個屬性), 用以紀錄它所擁有的 特性
    - 它是 class 用來保存其他屬性的 映射物件(mapping object, 即它的 namespace)
    - 它在 class 之中是 read only
- 其他屬性映射, 回傳 dictionary ((Example C1))
- 所有 object 都有個 built-in `__dict__` attribute. 可在裡面查看到 object 自行定義的所有屬性
- 建議使用 `vars(instance)` 來查看它的屬性, 而非使用赤裸裸的 `instance.__dict__`

```python
### Example C1
class Vehicle:
    def __init__(self, color):
        self.color = color

class Car(Vehicle):
    wheels: int = 4

cc = Car(color='blue')
print(cc.color)           # blue
print(cc.__dict__)        # {'color': 'blue'}
print(type(cc).__dict__)  # {'__module__': '__main__', '__annotations__': {'wheels': <class 'int'>}, 'wheels': 4, '__doc__': None}
```


## `__get__(self, obj, type=None) -> value`
- 類別若有綁定 `__get__`, 則此物件稱之為 `Descriptor(描述器)` (實作了 描述器協定)
    - self:        Descriptor instance
    - obj:         Descriptor 所 attached to 的 Object
    - type(owner): Descriptor 所 attached to 的 Object
- 實例取得屬性的查找順序, 參考底下的 *從類別取得屬性*
- 如果 `instance.attr1` 與 `instance.__dict__['attr1']` 同名, 則**後者**優先 (與 `__set__` 比較)
    - Non-Data Descriptors, 
- 三種 Descriptor 方法裡面, 唯一可以被 class 自己來調用的方法 (這也說明了為何只有 `__get__` 裡面有 owner (←有待驗證))

```py
class V:
    def __get__(self, obj, type=None):
        pass

class X:
    v = V()

x = X()
x.v  # 基本上會使用 type(v).__dict__['v']
```


## `__getattr__(self, name)`
- 若尋找實例屬性, ex: `x.y`, 依照正常的尋找流程都查不到, 正要拋出 AttributeError 前, 若有定義此方法, 則會使用 `x.__getattr__('y')`
    - 可把它理解成, 拋出 AttributeError 前的最後一到防線

```py
class People:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, item):
        return f'沒 {item} 這東西'

p = People('tony')
print(p.age)  # 沒 age 這東西
```


## `__getattribute__(self, name)`
- 對於任何尋找實例屬性, ex: C 類別實例x, `x.y` 的所有請求, 都會呼叫 `x.__getattribute__('y')`
    - 此結果必然 raise AttributeError, 不然就是得 取得 && 回傳屬性值, 取得的方式可能是底下幾種:
        - `x.__dict__`
        - `C.__slots__`
        - `C 的類別屬性`
        - `x.__getattr__`
        - `透過 type(y).__get__`
- 若覆寫此方法, 會阻止自動調用 Descriptors
    - 若這麼做, 會使屬性的存取變得緩慢 (覆寫的程式碼, 會在每次存取這種屬性時被執行)
- 調用 `instance` 屬性 or 方法 之前, 都會先來調用 `__getattribute__`
- 由 `object` 實作 `__getattribute__`

```python
### __getattribute__ 用途: 覆寫子類別, 隱藏繼承而來的類別屬性, 讓子類別成為不再具有 append 的 list
class listNoAppend(list):
    def __getattribute__(self, name):
        if name == 'append':
            raise AttributeError(name)
        return list.__getattribute__(self, name)


a = [1, 2, 3, 4, 888]
uu = listNoAppend(a)
print(uu) # [1, 2, 3, 4, 888]
uu.pop()
print(uu) # [1, 2, 3, 4]
uu.append(888) # ..... AttributeError: append
```


## `__doc__`
- 抓 類別說明 (instance or class 皆可使用)

```python
### __doc__ 用途
class C:
    '''沒有用的東西'''
    pass

print(C.__doc__) # 沒有用的東西
```


## `__init__(self, *args, **kwds)`
- 建構式
- 用途為: binding(繫結)
- 用來定義 **物件建立後** 的初始化方式


## `__mro__`
- class 在尋找指定的屬性 or 方法, 會根據此屬性內的 tuple 中的順序來尋找
- MRO: Method Resolution Order
- 此為 RO 屬性


## `__name__`
- `class A: pass`, 背後會隱含的建立 `__name__()`, 用來取得 class 名稱 'A'
- 類別方法 (實例無此方法)
- 回傳 類別的名稱
- 每個模組其實也都有個 `__name__` 屬性, 模組被 import 後, 這東西會是模組名稱
    - 若直接執行那個模組, `__name__` 則會變成 `__main__`
- 可使用 `sys.modules[__name__]` 來取得目前模組物件
- 此屬性無法被 unbind

```python
### __name__ 用途
class C: pass

C.__name__ # 'C'
```


## `__new__(cls, *args, **kwds)`
- 用來定義 **物件如何被建構**
- 方法的第一個參數, 必須是 `cls`, 方法簽署為: `def __new__(cls, *args, **kwds)`. 此為類別方法.
    - ex: `x=C(23)`, 等同於 `x=C.__new__(C, 23)`. (之後開始使用 `type(x).__init__(x, 23)` 作初始化)
- 此方法必須回傳 Class Instance(通常為 cls 的 Instance)
- 如果此方法沒回傳 Instance, 則 `__init__` 將不會被調用


## `__prepare__()`
- metaclass 專屬的方法.
- 因為這個東西很底層, 99.9999% 的情況下幾乎碰不到, 就不多做記錄了.


## `__set__(self, instance, value)`
- object 若有綁定 `__set__`, 則此物件稱之為 `Descriptor(描述器)` / `覆寫式描述器(Overriding Descriptor)` / `Data Descriptor(資料描述器)` (實作了 描述器協定)
    - 若物件只有 `__get__` 而無 `__set__`, 則稱為 `Non-Data Descriptor(非資料描述器)`
- 如果 `instance.attr1` 與 `instance.__dict__['attr1']` 同名, 則**前者**優先 (與 `__get__` 比較)
    - Data Descriptors 永遠都會覆寫 instance dictionaries (`instance.__dict__['xxx']` 啦)
- 若要讓物件成為 ReadOnly Descriptor, 可在 `__set__()` 內拋出 AttributeError
- *Example A*: o.x 設值時, 會優先觸發 `C.__setattr__()`, 若找不到, 才去觸發 `X.__set__()`
    - 若 有 `C.__setattr__()`, 會印出 WW
    - 若 無 `C.__setattr__()` && 有 `X.__set__()`, 會印出 QQ

```py
### Example A
class X:
    def __get__(self, *_): pass
    def __set__(self, *_): print('QQ')  # X 是個 覆寫式描述器

class C:
    # def __setattr__(self, name, value): print('WW')
    x = X()

o = C()
o.x = 8

# 假設 C 無 __setattr__(), 則 o.x 會呼叫 type(o).x.__set(o, 23)
```


## `__set_name__(self, owner, name)`
- Python3.6 以上適用.
- Descriptor Protocol 定義的方法
- 如果初始化 Descriptor, 此方法會自動被調用.

```python
class NN:
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name)
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class FF:
    nn = NN()

xx = FF()
yy = FF()
xx.nn = 3
print(xx.nn)  # 3
print(yy.nn)  # 0
```


## `__setattr__()`


## `__slots__`
- `x=C()`, 若 C 之中有定義了 `__slots__`, 那 x 就不會在有 `x.__dict__`, 爾後如果呼叫了 x 不存在的屬性, 便會拋出 Exception
- 用來控制特定物件他可擁有的特性名稱, 其值為 tuples
- `__slots__` 不會限制特性

```py
class People:
    __slots__ = ('name', 'age')


a = People()
a.name = 'tony'
a.height = 170
# AttributeError: 'People' object has no attribute 'height'
```


# Functions

## Generator
- 它繼承了 Iterator
- function 內如果有 yield, 那它便是個 generator function


## getattr

試圖取得 obj 的屬性時, 順序如下:

- 會從 `obj.__dict__` 尋找相符的屬性名稱
  - 若有找到 && 是個 Descriptor, 
    - 取值使用 `__get__`
    - 設值使用 `__set__`, 若無此方法, AttributeError
    - 刪值使用 `__delete__`, 若無此方法, AttributeError
  - 若有找到 && 只有 `__get__`
    - 從 instance 的 `__dict__` 尋找相符屬性名稱

```python
class People:
    def __init__(self, name):
        self.name = name

p = People('tony')

p.name
# 等同於
getattr(p, 'name')
```



## hashable
- 實例化後, 整個執行期間, hash(obj) 都不會變動 (immutable 必為 hashable)
- 需實作 `__hash__()` && `__eq__()`



## iterable
- 物件若實作了 `__iter__()`, 它就是個 iterable, 就可以回傳 iterator(它實作了 iterable 介面)
- 可使用 `qq = iter(obj)` 來取的 iterator, 後續可使用 `next(qq)` 逐一取出
- 取完後, 會拋出 StopIteration


## Iterator
- 迭代器物件, 它實作了 iterable 介面 && 並實作了 `__next__()`


# Other

## 從類別取得屬性
類別屬性(name) 的查找順序:
1. 若 `'name' in C.__dict__`, 則從 `C.__dict__['name']` 取出它的值 v, 然後若
    - v 為 Descriptor, 則回傳 `type(v).__get__(v, None, C)` 的結果
    - v 非 Descriptor, 則回傳 C.name 的值, 即 v
2. 若 `'name' not in C.__dict__`, 則 `C.name` 的動作會 委派(delegate) 到它的父類別們(依照MRO)去尋找.
3. 若無, 拋出 AttributeError




## 從實例取得屬性
實例屬性(name) 的查找順序:
1. 若 'name' 出現在 C(或父類別們)裡頭, 且 name 的值(v) 恰巧為 覆寫式描述器, 則 `x.name` 會得到 `type(v).__get__(v, x, C)` 的結果
2. 若 `'v' in x.__dict__`, 則回傳 `x.__dict__['name']` 的結果
3. `C.name` 的動作會 委派(delegate) 到他的父類別們去尋找
    - 當其結果(v) 被找到, 且為 Descriptor, 則回傳 `type(v).__get__(v, x, C)`
    - 非為 Descriptor, 則回傳 v 的值
4. 看是否有定義 `__getattr__(x, 'name')`, 若有則從中取值
5. 拋出 AttributeError

```py
class C(D, E, F):
    name = XX

x = C()
x.name
```


## 設定 物件 or 類別 屬性
除非該屬性值為 descriptor 或者該類別有定義 `__setattr__`, 否則只會在 `__dict__` 之中加入 key-value
