# Python 重要概念

- 2019/03/18


## classmethod vs staticmethod

- [classmethod vs staticmethod](https://zhuanlan.zhihu.com/p/28010894)

這問題好久之前看過了, 印象中當時讀了一直看不懂是在衝三小, 就不理他了. 結果問題找上門了...


```py
class A(object):
    def m1(self, n):
        print('self', self)

    @classmethod
    def m2(cls, n):
        print('cls:', cls)

    @staticmethod
    def m3(n):
        print(n)

a = A()
a.m1(1)     # self <__main__.A object at 0x0000014A1B1D95F8>
A.m2(1)     # cls: <class '__main__.A'>
A.m3(1)     # 1

#
```

每個 `python class` 都會有下列屬性:

attribute     | description
------------- | -------------------------
\_\_name__    | class 名稱
\_\_bases__   | class 的 父類別 們 (父類別1, 父類別2,)
\_\_dict__    | C1範例

----------------------------------------------------------

- C1範例

```python
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
