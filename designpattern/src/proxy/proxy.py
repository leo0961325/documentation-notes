"""
Michael 喜歡 Jennifier 很久了, 但是太害羞不敢表達
於是請 Bruce 幫忙送禮物給她
"""
from abc import ABCMeta, abstractmethod


class Wife:
    # 人妻
    def __init__(self, name: str):
        self.name = name


class IGive(metaclass=ABCMeta):
    @abstractmethod
    def give_money(self):
        raise NotImplementedError

    def give_flower(self):
        raise NotImplementedError


class Pursuit(IGive):
    # 追求者
    def __init__(self, target: Wife):
        self.target = target

    def give_money(self) -> int:
        return 0

    def give_flower(self) -> str:
        return ''


class Proxy(IGive):
    # 幫忙送東西
    def __init__(self, who: Pursuit):
        """
        who: 幫忙代理的對象
        """
        self.who = who

    def give_money(self):
        return 1_000

    def give_flower(self):
        return '向日葵'
