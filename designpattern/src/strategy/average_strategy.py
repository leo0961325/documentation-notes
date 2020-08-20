"""
你參加過很多次考試, 人家要看你的 "平均" 成績
但是平均, 是哪種平均啊?
  簡單平均?
  移動平均?
  截尾平均?
  ...??
  
總之計算成績(算平均), 就是一種計算的策略, 而策略應該保持可擴充
"""
from abc import ABCMeta, abstractmethod


class IAverage(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self, grades) -> int:
        pass


class SimpleAverage(IAverage):
    def calculate(self, grades: list) -> int:
        return sum(grades) / len(grades)


class MovingAverage(IAverage):
    def calculate(self, grades, period: int = 3) -> int:
        return sum(grades[-3:]) / period


class TrimmedAverage(IAverage):
    _tail: int = 1
    def calculate(self, grades) -> int:
        total = sum(grades[self._tail: -self._tail])
        num = len(grades) - self._tail * 2
        return total / num
    
    def set_tail(self, tail: int = 0) -> None:
        if tail < 0:
            raise Exception(f'截尾筆數不得為 < 0')
        self._tail = tail


class Calculator:
    # 只能拿來計算平均的廢物類別
    _strategy = None
    _grade = []
    
    def add(self, grade):
        self._grade.append(grade)
    
    @property
    def grade(self):
        return self._strategy.calculate(grades=self._grade)
    
    def average_strategy(self, method: IAverage) -> None:
        self._strategy = method
