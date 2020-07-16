import pytest
from factory.simple_factory import TrainingCamp


class TestSimpleFactory:
    @pytest.fixture(scope='module')
    def init_factory(self):
        return TrainingCamp()

    def test_mage_attack(self, init_factory):
        mage = init_factory.train(career='mage', name='Swei')
        assert mage.attack() == -9999

    def test_warrier_attack(self, init_factory):
        mage = init_factory.train(career='warrier', name='Tony2')
        assert mage.attack() == -1
