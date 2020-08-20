"""
工廠方法模式

落實專業分工

TrainingCamp 變成抽象的概念(類似學校)
分為 MageTrainingCamp && WarrierTrainingCamp
分別用來生產 Mage && Warrier
"""
from abc import ABCMeta, abstractmethod


class Hero(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass
    

class Mage(Hero):
    def attack(self):
        return -9999
    
    
class Warrier(Hero):
    def attack(self):
        return -1


class TrainingCamp(metaclass=ABCMeta):
    """
    尊重專業的訓練單位.
    """
    @abstractmethod
    def train(self, career: str, name: str) -> Hero:
        pass
    
    
class MageTrainingCamp(TrainingCamp):
    def train(self, name: str) -> Hero:
        return Mage(name=name)
    
    
class WarrierTrainingCamp(TrainingCamp):
    def train(self, name: str) -> Hero:
        return Warrier(name=name)
