from strategy.average_no_strategy import Calculator

class TestAverageNoStrategy:
    
    def test_calculate_average(self):
        c = Calculator()
        c.add(100)
        c.add(80)
        c.average_strategy(method='sa')
        assert c.grade == 90
        
    def test_calculate_average2(self):
        c = Calculator()
        c.add(100)
        c.add(80)
        c.average_strategy(method='sa')
        assert c.grade == 90
        c.average_strategy(method='ma')
        c.add(60)
        c.add(40)
        assert c.grade == 60