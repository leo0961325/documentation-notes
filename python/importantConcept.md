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


