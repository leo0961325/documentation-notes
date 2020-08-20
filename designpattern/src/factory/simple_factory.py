"""
簡單工廠模式

TrainingCamp 專門用來生產 Hero
Hero 有分為 
- 戰士 Warrier
- 法師 Mage
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


class TrainingCamp:
    """
    倆光的訓練營, 非常不尊重專業.
    """
    def train(self, career: str, name: str) -> Hero:
        if career == 'mage':
            return Mage(name=name)
        elif career == 'warrier':
            return Warrier(name=name)
