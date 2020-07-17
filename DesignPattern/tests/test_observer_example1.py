import pytest
from observer.observer_example1 import WaterHeater, Father, GrandPa


class TestObserverExample1:
    @pytest.fixture(scope='module')
    def water_heater(self):
        return WaterHeater()

    def test_initial_water_degree_equals_20(self, water_heater):
        assert water_heater.get_degree() == 20

    def test_water_degree_is_20(self):
        water_heater = WaterHeater()
        father = Father()
        grandpa = GrandPa()
        water_heater.add_observer(father)
        water_heater.add_observer(grandpa)
        water_heater.set_degree(20)
        assert father.is_taking_shower is True
        assert grandpa.is_taking_shower is False

    def test_water_degree_is_40(self):
        water_heater = WaterHeater()
        father = Father()
        grandpa = GrandPa()
        water_heater.add_observer(father)
        water_heater.add_observer(grandpa)
        water_heater.set_degree(40)
        assert father.is_taking_shower is False
        assert grandpa.is_taking_shower is False

    def test_water_degree_is_60(self):
        water_heater = WaterHeater()
        father = Father()
        grandpa = GrandPa()
        water_heater.add_observer(father)
        water_heater.add_observer(grandpa)
        water_heater.set_degree(60)
        assert father.is_taking_shower is False
        assert grandpa.is_taking_shower is True
