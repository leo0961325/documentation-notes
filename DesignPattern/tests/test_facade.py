import pytest
from facade.facade import Register, Payment, Dormitory, Senior


class TestFacade:
    def test_good_senior_makes_things_simple(self):
        chris = Senior(junior_name='jay')
        assert 'sid' in chris.help_you()
        assert 'invoice' in chris.help_you()
        assert 'card' in chris.help_you()
        
    def test_go_to_register(self):
        register_center = Register()
        assert '學號' in register_center.register(name='jay')

    def test_go_to_pay(self):
        payment_center = Payment()
        assert '收據' in payment_center.pay(name='jay')


    def test_go_to_check_in(self):
        counter = Dormitory()
        assert '門禁卡' in counter.check_in(name='jay')