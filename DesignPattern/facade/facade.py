"""
新生入學, 自己要跑 「註冊, 繳費, 報到」這流程好麻煩

找好人學長幫你就好了, 一條龍快速辦好~
"""
from abc import ABCMeta, abstractmethod


class Register:
    def register(self, name: str) -> str:
        return f"{name} 的 學號 193898706449"


class Payment:
    def pay(self, name: str) -> str:
        return f"{name} 的 收據 AK45698217"


class Dormitory:
    def check_in(self, name: str) -> str:
        return f"{name} 的 門禁卡 AXo8y6"


class Senior:
    def __init__(self, junior_name: str):
        self.junior_name = junior_name
        self._register = Register()
        self._payment = Payment()
        self._dormitory = Dormitory()

    def help_you(self):
        sid = self._register.register(self.junior_name)
        invoice = self._payment.pay(self.junior_name)
        card = self._dormitory.check_in(self.junior_name)
        return {
            "sid": sid,
            "invoice": invoice,
            "card": card
        }
