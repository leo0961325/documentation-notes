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
            cls.__obj = super().__new__(cls, *args, **kwargs)

        return cls.__obj
