# Python magic methods


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

## `__init__`
- 建構式
- 用途為: binding(繫結)
- 用來定義 **物件建立後** 的初始化方式


## `__new__`
- 用來定義 **物件如何被建構**
- 方法的第一個參數, 必須是 `cls`, 方法簽署為: `def __new__(cls, xxx)`. 此為類別方法.
- 此方法必須回傳 Class Instance(通常為 cls 的 Instance)
- 如果此方法沒回傳 Instance, 則 `__init__` 將不會被調用


## `__name__`
- `class A: pass`, 背後會隱含的建立 `__name__()`, 用來取得 class 名稱 'A'
- 類別方法 (實例無此方法)
- 回傳 類別的名稱
- 每個模組其實也都有個 `__name__` 屬性, 模組被 import 後, 這東西會是模組名稱
    - 若直接執行那個模組, `__name__` 則會變成 `__main__`
- 可使用 `sys.modules[__name__]` 來取得目前模組物件

```python
### __name__ 用途
class C: pass

C.__name__ # 'C'
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


## `__bases__`
- 回傳 父類別們 (tuple)

```python
### __bases__ 用途
class Traffic:
    pass

class Car(Traffic):
    pass

Car.__bases__ # (__main__.Traffic,)
```

## `__get__(self, instance, type=None) -> value`
- object 若有綁定 `__get__`, 則此物件稱之為 `Descriptor(描述器)` / `Non-Data Descriptor(非資料描述器)` (實作了 描述器協定)
    - self 為 Descriptor instance
    - obj  為 Descriptor 所 attached to 的 Object
    - type(owner) 為 Descriptor 所 attached to 的 Object
- 若使用 a.x, 首先會先尋找 `a.__dict__['x']`, 再者尋找 `type(a).__dict__['x']`(父類別們)
- 如果 instance.attr1 與 `instance.__dict__['attr1']` 同名, 則**後者**優先
    - Non-Data Descriptors, 
- 三種 Descriptor 方法裡面, 唯一可以被 class 自己來調用的方法 (這也說明了為何只有 `__get__` 裡面有 owner (←有待驗證))


## `__set__(self, instance, value)`
- object 若有綁定 `__set__`, 則此物件稱之為 `Descriptor(描述器)` / `覆寫式描述器(Overriding Descriptor)` / `Data Descriptor(資料描述器)` (實作了 描述器協定)
- 如果 instance.attr1 與 `instance.__dict__['attr1']` 同名, 則**前者**優先
    - Data Descriptors 永遠都會覆寫 instance dictionaries (`instance.__dict__['xxx']` 啦)
- 若要讓物件成為 ReadOnly Descriptor, 可在 `__set__()` 內拋出 AttributeError


## `__delete__(self, instance)`
- object 若有綁定 `__delete__`, 則此物件稱之為 `Descriptor(描述器)` / `覆寫式描述器(Overriding Descriptor)` / `Data Descriptor(資料描述器)` (實作了 描述器協定)
- 如果 instance.attr1 與 `instance.__dict__['attr1']` 同名, 則**前者**優先


## `__class__`
- 每個 instance of object 都有個 `__class__` 屬性, 參考至 instance 建構時所使用的 class
- 而 class 本身也有個 `__class__`, 它參考的就是 `<class 'type'>`
- 每個 class 也是個 object, 是 type 類別的 instance
- 可使用 `instance.__class__` 或 `type(instance)` 來看出, instance 從哪個類別建構出來的

```py
class Demo: pass

print(Demo)    # <class '__main__.Demo'>
type(Demo)     # <class 'type'>
d = Demo()
d.__class__    # <class '__main__.Demo'>
d.__class__()  # <__main__.Demo object at 0x7f87b123edd0>
```


## `__getattr__`
- 如果要取得物件內不存在的屬性時, 會透過這個方法
    - 如果 C 為特定類別 && `C.__dict__` 不存在屬性 x, 而調用 C.x 時, 會轉而透過呼叫 `C.__getattr__()` 來看看是否有 x
    - 承上, 若沒定義此方法 && `C.__dict__` 又找不到, 則拋出 AttributeError 

```py
class People:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        return f'沒 {item} 這東西'

p = People('tony')
print(p.age)
# 沒 age 這東西
```


## `__mro__`
- class 在尋找指定的屬性 or 方法, 會根據此屬性內的 tuple 中的順序來尋找
- MRO: Method Resolution Order
- 此為 RO 屬性



## `__getattribute__()`
- 對 `實體屬性` 的所有參考, 都會通過 `特殊方法 __getattribute__`
- Descriptors 都被此方法所調用, 若覆寫此方法, 會阻止自動調用 Descriptors
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


## `__dict__()`
- `class A: pass` 背後, (除非有定義 `__slots__`) 會自動創建 `__dict__`(類別or實例 都會有這個屬性), 用以紀錄它所擁有的 特性
    - 它是 class 用來保存其他屬性的 映射物件(mapping object, 即它的 namespace)
    - 它在 class 之中是 read only
- 其他屬性映射, 回傳 dictionary ((C1範例))
- 所有 object 都有個 built-in `__dict__` attribute. 可在裡面查看到 object 自行定義的所有屬性
- 建議使用 `vars(instance)` 來查看它的屬性, 而非使用赤裸裸的 `instance.__dict__`

```python
### C1範例
class Vehicle:
    can_fly: bool = False
    weels: int = 0
    def __get__(self, object, type=None):
        return 'yellow'

class Car(Vehicle):
    weels: int = 0
    vv = Vehicle()
    def __init__(self, color):
        self.color = color

cc = Car(color='blue')
print(cc.color)           # blue
print(cc.__dict__)        # {'color': 'blue'}
print(type(cc).__dict__)  # {'__module__': '__main__', '__annotations__': {'weels': <class 'int'>}, 'weels': 0, '__init__': <function Car.__init__ at 0x7fb46fa440e0>, '__doc__': None}
```


## `__prepare__()`
- metaclass 專屬的方法.
- 因為這個東西很底層, 99.9999% 的情況下幾乎碰不到, 就不多做記錄了.


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


# Functions

## getattr

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


## Generator

- 它繼承了 Iterator
- function 內如果有 yield, 那它便是個 generator function
- 