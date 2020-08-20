"""
跟別人打架
攻擊之前的那一剎那會決定:
  這次要小小的揮拳
  還是用力地給他踹下去
"""
from abc import ABCMeta, abstractmethod


class IAttack(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass


class NormalAttack(IAttack):
    def attack(self) -> int:
        return -1


class HeavyAttack(IAttack):
    def attack(self) -> int:
        return -10


class Warrier:
    _strategy: IAttack = None
    
    def set_strategy(self, strategy: IAttack):
        self._strategy = strategy
    
    def hit(self) -> float:
        return self._strategy.attack()
