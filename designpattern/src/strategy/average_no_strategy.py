"""
計算平均數

沒有使用策略模式的情境
"""

class Calculator:
    _grade: list = []
    _strategy: str = 'sa'

    def add(self, grade: int) -> None:
        self._grade.append(grade)

    @property
    def grade(self):
        if self._strategy == 'sa':
            return sum(self._grade) / len(self._grade)
        elif self._strategy == 'ma':
            return sum(self._grade[-3:]) / 3
        else:
            raise NotImplementedError(f"尚未實作的平均方式")

    def average_strategy(self, method: str):
        self._strategy = method
            