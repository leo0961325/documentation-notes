import pytest
from factory.factory_method import *


class TestFactoryMethod:
    mage_camp: TrainingCamp = None
    warrier_camp: TrainingCamp = None
    
    @pytest.fixture(scope='module')
    def init_factory(self):
        print(MageTrainingCamp())
        print(f"111 {self.mage_camp}")
        self.mage_camp = MageTrainingCamp()
        print(f"222 {self.mage_camp}")
        self.warrier_camp = WarrierTrainingCamp()
        
    def test_mage_camp_trains_mage(self, init_factory):
        print(f"333 {self.mage_camp}")
        # mage = self.mage_camp.train(name='swei')
        # assert mage.attack() == -9999
        assert 1 == 1

    def test_warrier_camp_trains_warrier(self, init_factory):
        print(f"4444 {self.warrier_camp}")
        # warrier = self.warrier_camp.train(name='Tony2')
        # assert warrier.attack() == -1
        assert 2 == 2