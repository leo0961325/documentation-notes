import pytest
from factory.simple_factory import TrainingCamp


class TestSimpleFactory:
    def test_mage_attack(self):
        mage = TrainingCamp().train(career='mage', name='Swei')
        assert mage.attack() == -9999

    def test_warrier_attack(self):
        warrier = TrainingCamp().train(career='warrier', name='Jay')
        assert warrier.attack() == -1
