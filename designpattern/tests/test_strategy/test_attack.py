from strategy.attack_strategy import Warrier, NormalAttack, HeavyAttack


class TestAttackStrategy:

    def test_normal_attack(self):
        vince = Warrier()
        vince.set_strategy(strategy=NormalAttack())
        assert vince.hit() == -1
        
    def test_heavy_attack(self):
        vince = Warrier()
        vince.set_strategy(strategy=HeavyAttack())
        assert vince.hit() == -10

    def test_continuous_attack(self):
        vince = Warrier()
        vince.set_strategy(strategy=HeavyAttack())

        hurts = 0
        hurts += vince.hit()
        hurts += vince.hit()
        hurts += vince.hit()
        vince.set_strategy(strategy=NormalAttack())
        hurts += vince.hit()

        assert hurts == -31
