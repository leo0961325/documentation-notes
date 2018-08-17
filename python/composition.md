# Composition 合成
- 2018/08/13
- [繼承(Inheritance) vs 合成(Composition)](https://study.holmesian.org/learn-python-the-hard-way/ex44.html)

> 大部分使用`继承`的场合都可以用`合成`取代，而多级继承则需要不惜一切地避免之。


```py
class Parent():
    def say(self):
        print('Hello')

class Child(Parent):
    def say(self):
        print('Yo')
        super(Child, self).say()

dad=Parent()
son=Child()
dad.say()
son.say()
# Hello      # dad
# Yo         # son
# Hello      # son
```