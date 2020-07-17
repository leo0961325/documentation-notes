import pytest
from dependency_injection.di_example1 import Bruce, Michael, Poison, Lion


class TestDIExample1:
    @pytest.fixture(scope='module')
    def init_lion(self):
        return Lion()

    def test_lion_initial_blood_equals_to_1(self, init_lion):
        lion = init_lion
        assert lion.get_power() == 1

    def test_lion_eat_bruce(self):
        food = Bruce()
        lion = Lion()
        lion.eat_food(food)
        assert lion.get_power() == 6

    def test_lion_eat_michael(self):
        food = Michael()
        lion = Lion()
        lion.eat_food(food)
        assert lion.get_power() == 11

    def test_lion_eat_poision(self, init_lion):
        poision = Poison()
        lion = init_lion
        lion.eat_food(poision)
        assert lion.get_power() < 0
