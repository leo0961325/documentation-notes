import pytest
from facade.facade import Register, Payment, Dormitory, Senior


class TestFacade:
    
    @pytest.fixture(scope='module')
    def init_register(self):
        return Register()
    
    @pytest.fixture(scope='module')
    def init_payment(self):
        return Payment()
    
    @pytest.fixture(scope='module')
    def init_dermitory(self):
        return Dormitory()
        
    def test_go_to_register(self, init_register):
        register_center = init_register
        assert '學號' in register_center.register(name='jay')

    def test_go_to_pay(self, init_payment):
        payment_center = init_payment
        assert '收據' in payment_center.pay(name='jay')

    def test_go_to_check_in(self, init_dermitory):
        counter = init_dermitory
        assert '門禁卡' in counter.check_in(name='jay')
        
    def test_no_good_senior_help_you(self, 
                                     init_register, 
                                     init_payment, 
                                     init_dermitory):
        register_center = init_register
        payment_center = init_payment
        counter = init_dermitory
        assert '學號' in register_center.register(name='jay')
        assert '收據' in payment_center.pay(name='jay')
        assert '門禁卡' in counter.check_in(name='jay')
        
    def test_good_senior_makes_things_simple(self):
        chris = Senior(junior_name='jay')
        assert 'sid' in chris.help_you()
        assert 'invoice' in chris.help_you()
        assert 'card' in chris.help_you()