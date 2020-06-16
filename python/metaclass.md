# metaclass

- 2020/06/16
- [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python?rq=1)

永遠記得, Python 裏頭的任何東西, 都是 object

```py
class ObjectCreator:
    pass

obj = ObjectCreator()
print(obj)  # <__main__.ObjectCreator object at 0xC669B0>
```

甚至連上面範例的 ObjectCreator, 它是 Class, 同時也是 Object.

既然 ObjectCreator 是個 Object(Instance), 我們就可以:

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


