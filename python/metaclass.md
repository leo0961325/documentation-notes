# Metaclass

- 2020/06/16
- [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python?rq=1)

**The main purpose of a metaclass is to change the class automatically, when it's created.**

基本上, 知道上面這句就已經足夠了!!! 因為 99% 以上的 Python 使用者不會來使用 metaclass 這東西

> Metaclasses are deeper magic that 99% of users should never worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why).

------------------------------

```py
class ObjectCreator:
    pass

obj = ObjectCreator()
print(obj)  # <__main__.ObjectCreator object at 0xC669B0>
```

甚至連上面範例的 ObjectCreator, 它是 Class, 同時也是 Object.

既然 ObjectCreator 是個 Object/Instance, 我們就可以:

- 把物件指派給變數: `a = ObjectCreator`
- 複製它
- 為它增加屬性: `ObjectCreator.name = 'Tony'`
- 把它當成 function 裏頭的參數: `my_func(ObjectCreator)`


## 動態的建立 classes

```py
def class_factory(name):
    if name == 'bird':
        class Bird:
            pass
        return Bird
    else:
        class Fish:
            pass
        return Fish


myClass = class_factory('bird')
```

但上面的方式, 也不算是真真正正的 動態產生

**在 Python 底層, 當我們使用了 `class`, Python 便會自動建立這個 Class Object**

那如何真正的達成 動態產生, 得先認識 `type` 這東西

```py
print(type(1))  # <type 'int'>
print(type('a'))  # <class 'str'>
print(type(ObjectCreator))  # <class 'type'>
print(type(ObjectCreator()))  # <class '__main__.ObjectCreator'>
```

`type` 這東西的特殊能力, 可以用來 動態產生 Class

如果吃飽太閒, 可以去[官網](https://docs.python.org/3.7/library/functions.html#type)好好了解 type

> type 的方法簽屬: `type(name, bases, attrs)`
>   name 為 str, 表示 Class 的名稱
>   bases 為 tuple, 表示繼承自那些 Classes
>   attrs 為 dict, 表示它裏頭的屬性

```py
# 如果你真他媽太閒活得厭煩, 不然 type 內的 name 與 指派的變數, 請用一樣好嗎?
# ↓↓↓↓           ↓↓↓↓↓
MyClass = type('MyClass', (), {})
print(MyClass)  # <class '__main__.MyClass'>
print(MyClass())  #<__main__.MyClass object at 0xCDC66AC8>
```

所以說

```py
class Hello:
    name = 'Tony'
```

Python 底層幫你做了

```py
Hello = type('Hello', (), {'name': 'Tony'})
```

然後他就跟一個如你所知的 Class, 可以指定屬性, 設定方法, 或是去繼承...

等等, 怎麼設定方法?  很簡單, 看下面

```python
def good_night(self):
    print(self.name)

Hello = type('Hello', (), {'name': 'Tony', 'good_night': good_night})
hello = Hello()
hello.good_night()  # Tony
```

或者, 上面太複雜的話, 直接使用下面的方式:

```py
Hello.good_night = good_night
```


## metaclasses

```py
MyClass = MetaClass()
myObject = MyClass()
```

我們又知道, 我們可以用 `type` 來產生和上面一樣的效果

```py
MyClass = type('MyClass', (), {})
```

這是因為 `type` 這個 function, 本質上就是一個 `metaclass`. 也就是說, Python 使用 `tpye` 這個 metaclass 在底層幫你建立所有 Class

那為何是 `type` 而不是 `Type`?

```py
age = 30
age.__class__  # <type 'int'>
name = 'Tony'
name.__class__  # <class 'str'>
c = ObjectCreator
c.__class__  # <class 'type'>

age.__class__.__class__  # <type 'type'>
name.__class__.__class__  # <type 'type'>
c.__class__.__class__  # <type 'type'>
```

`metaclass` 只是個用來建立 class object 的東西, 也可以稱他為 'class factory(類別工廠)'

`type` 就是 Python 底層使用的 built-in metaclass


## `__metaclass__` 屬性

### Python2

用法如下:

```py
class Qoo(Orz):
    __metaclass__ = ...
```

`class Qoo(object)` 並未真正在記憶體裡面建立 `Qoo`

Python 會去尋找 class 裏頭有沒有定義 `__metaclass__`. 
- 若有找到, 會使用它來建立 class
- 若沒找到, 它會在 MODULE level 尋找看看有沒有 `__metaclass__`
  - 有找到, 會使用它來建立 class
  - 沒找到, 會去找父類別(Orz) 的 metaclass 來建立 class

而 `__metaclass__` 裏頭可以放些什麼? 基本上就是放 **能建立 class 的東西** (ex: `type`)


### Python3

```py
class Qoo(metaclass=xxx):
    ...
```

此外也可透過下面的方式, 來為 metaclass 添增屬性

```py
class Qoo(metaclass=xxx, kwarg1=value1, kwarg2=value2):
    ...
```

回到一開頭寫的, **The main purpose of a metaclass is to change the class automatically, when it's created.**

以下來舉個智障的例子來說明, `__metaclass__` 到底能幹麻 以及 怎麼使用: 

現在希望能把 class 的所有屬性(魔術方法 && 私有方法除外), 全部轉大寫, ex:

```py
class People:
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
```

可透過改寫 `__metaclass__` 的方式, 來讓 height, weight, age 全部變成大寫 (夠智障的需求吧)

```py
def upper_attr(class_name, class_parents, class_attrs):

    uppercase_attrs = {
        kk if kk.startswith('__') else kk.upper(): vv
        for kk, vv in class_attrs.items()
    }

    return type(class_name, class_parents, uppercase_attrs)


# 底下這行的用法屬於 Python2, Python3 不會理它了
# __metaclass__ = upper_attr


# Python3 改成底下這樣
class People(metaclass=upper_attr):
    age = 30

print(hasattr(People, 'age'))  # False
print(hasattr(People, 'AGE'))  # True
```

而上面那樣雖說看起來比較直觀, 但因為種種原因(懶得列了), 用下面那樣會更好(更加的 python):

```py
class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, attrs):
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in attrs.items()
        }
        return super(UpperAttrMetaclass, cls).__new__(
            cls, clsname, bases, uppercase_attrs)


class People(metaclass=UpperAttrMetaclass):
    age = 30


print(hasattr(People, 'age'))  # False
print(hasattr(People, 'AGE'))  # True
```

---------------

關於 metaclass 最常見的 use case: Django ORM

```py
class People(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
```

裡面敲敲地修改了 metaclass (類別建構過程被改寫)

```py
### 底下這個無法直接使用 (必須要在 django 的情境下才可)
tony = People(name='Tony', age=30)
print(tony.age)  # It won't return an IntegerField object. It will return an int, and can even take it directly from the database. 
```

原因就在於, `models.Model` 定義了 `__metaclass__`, 並把 People class 的建構, 轉成 complex hook to database field


## Finally

classes 就是能建構 Instance 的 Objects

Classes 本身也是 Instances (也就是 metaclasses)

```py
class Qoo:
    pass

print(id(Qoo))  # 37575416
```

Python 的世界中, 任何東西都是物件. 任何東西既是 **instances of classes** 同時也是 **instances of metaclasses**

↑ 除了 `type` (`type` 就是它本身的 metaclass)

metaclass 其實是個相當複雜的東西, 沒事別用. 如果真需用到的話, 可使用下列技術來代替:

- monkey patching
- class decorators

99% 的情境, 都可使用以上兩個技術來代替

但是 98% 的情境, 根本連上面兩個都不會用到

所以, 98% 以上的情境, 本篇確實是廢文.
