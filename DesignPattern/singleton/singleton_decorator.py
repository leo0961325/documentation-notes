"""
獨體模式的不同實作方式
- S1 : 使用 decorator
- S2 : 改寫 __new__
"""

def singleton(cls, *args, **kwargs):
    __instance = {}  # 可以用來保存多種類別實例

    def wrapper(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return wrapper


@singleton
class S1:
    pass


class S2:
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls, *args, **kwargs)

        return cls.__obj


def main():
    # Instance 1
    s1 = S1()
    s2 = S1()
    print(type(s1), id(s1))
    print(type(s2), id(s2))

    # Instance 2
    s3 = S2()
    s4 = S2()
    print(type(s3), id(s3))
    print(type(s4), id(s4))


if __name__ == "__main__":
    main()
