# Python dunder methods


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


## `__set__`
- 類別物件內, 若有定義這個, 則稱此類別為 `覆寫式描述器(overriding descriptor)` or `data descriptor(資料描述器)`(比較老舊的稱呼)


## `__get__`
- 類別物件內, 若有定義此方法, 則此類別稱為 `descriptor(描述器)`
- 若為唯讀(無 `__set__`), 則稱為 `nonoverriding descriptor(非覆寫式描述器)` or `nondata descriptor(非資料描述器)`


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

- 物件有 `__iter__()`, 就是個 iterable, 他就可以回傳 iterator
- 可使用 `iter(obj)`