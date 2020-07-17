"""
獅子吃肉, 從中恢復體力
"""
from abc import ABCMeta, abstractmethod


class Swallowable(metaclass=ABCMeta):
    @abstractmethod
    def pass_nutrients(self) -> int:
        pass


class Michael(Swallowable):
    def pass_nutrients(self):
        return 10


class Bruce(Swallowable):
    def pass_nutrients(self):
        return 5


class Poison(Swallowable):
    def pass_nutrients(self):
        return -999


class Lion:
    def __init__(self):
        self._power = 1

    def eat_food(self, food: Swallowable) -> None:
        self._power += food.pass_nutrients()

    def get_power(self) -> int:
        return self._power
