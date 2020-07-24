# Collection

- 一個 instance 可以是個 Container, Container 可以是底下的東西(但他們互斥)
    - sequence
    - mapping
    - set
- 上述的 Container, 為了最大的實用性, 最好具備底下的特殊方法:
    - `__getitem__`
    - `__setitem__`
    - `__delitem__`
    - `__len__`
    - `__contains__`
    - `__iter__`
