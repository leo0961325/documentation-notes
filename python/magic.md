# Python dunder methods


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
- 方法的第一個參數, 必須是 `cls`, 方法簽署為: `def __new__(cls, xxx)`
- 此方法必須回傳 Class Instance(通常為 cls 的 Instance)
- 如果此方法沒回傳 Instance, 則 `__init__` 將不會被調用


## `__name__`
- 類別方法 (實例無此方法)
- 回傳 類別的名稱

```python
### __name__ 用途
class C:
    pass

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


## `__get__(self, instance, owner)`
- 若物件有 `__get__` 則此類別 實作了 描述器(Descriptor) 協定
- 若僅有 `__get__`, 也可稱為 `nonoverriding descriptor(非覆寫式描述器)` or `nondata descriptor(非資料描述器)`
- 這是三種 Descriptor 裡面, 唯一可以被 class 自己來調用的方法 (這也說明了為何只有 `__get__` 裡面有 owner)
- 

## `__set__(self, instance, value)`
- 若物件有 `__set__` 則此類別 實作了 描述器(Descriptor) 協定
- 若物件同時有 `__set__`, `__get__`, `__delete__`, 則稱此類別為 data descriptor(資料描述器)`
- 若物件同時有 `__set__`, 則稱此類別為 `覆寫式描述器(overriding descriptor)`


## `__delete__(self, instance)`
- 若物件有 `__delete__` 則此類別 實作了 描述器(Descriptor) 協定
- 若物件同時有 `__set__`, `__get__`, `__delete__`, 則稱此類別為 data descriptor(資料描述器)`


## `__class__`
- 每個 instance of object 都有個 `__class__` 屬性, 參考至 instance 建構時所使用的 class
- 而 class 本身也有個 `__class__`, 它參考的就是 `<class 'type'>`
- 每個 class 也是個 object, 是 type 類別的 instance


## `__getattr__`
- 如果要取得物件內不存在的屬性時, 會透過這個方法

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


## `__getattribute__`
- 對 `實體屬性` 的所有參考, 都會通過 `特殊方法 __getattribute__`
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

用來控制特定物件他可擁有的特性名稱

```py
class People:
    __slots__ = ('name', 'age')


a = People()
a.name = 'tony'
a.height = 170
# AttributeError: 'People' object has no attribute 'height'
```


## `__dict__`
- 其他屬性映射, 回傳 dictionary ((C1範例))

```python
### C1範例
class C1:
    x = 23
    C1.y = 8
    def m1(self):
        C1.z = 5
        w=6

print(C1.__dict__)
"""
{
    '__module__': '__main__',
    'x': 23,
    'm1': <function C1.m1 at 0x7fa35243f1e0>,
    '__dict__': <attribute '__dict__' of 'C1' objects>,
    '__weakref__': <attribute '__weakref__' of 'C1' objects>,
    '__doc__': None
}
"""
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