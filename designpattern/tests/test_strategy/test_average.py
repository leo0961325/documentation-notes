import pytest
from strategy.average_strategy import (
    Calculator, 
    SimpleAverage, 
    MovingAverage, 
    TrimmedAverage
)


class TestAverageStrategy:
    
    def test_calculate_average(self):
        c = Calculator()
        c.add(100)
        c.add(80)
        sa = SimpleAverage()
        c.average_strategy(method=sa)
        
        assert c.grade == 90
        # [100, 80]

        c.add(60)
        
        assert c.grade == 80
        # [100, 80, 60]

        c.add(40)
        c.add(20)
        
        assert c.grade == 60
        # [100, 80, 60, 40, 20]

        ma = MovingAverage()
        c.average_strategy(method=ma)
        
        assert c.grade == 40
        # [100, 80, 60, 40, 20]
        
        c.add(540)
        
        assert c.grade == 200
        # [100, 80, 60, 40, 20, 540]
        
        ta = TrimmedAverage()
        c.average_strategy(method=ta)
        
        assert c.grade == 50
        # [100, 80, 60, 40, 20, 540]
        
        c.average_strategy(method=sa)
        assert c.grade == 140
        # [100, 80, 60, 40, 20, 540]
