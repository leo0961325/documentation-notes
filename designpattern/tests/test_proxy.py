import pytest
from proxy.proxy import Wife, Proxy, Pursuit


class TestProxy:
    @pytest.fixture(scope='module')
    def mock_wife(self):
        return Wife(name='Jennifier')

    def test_give_money_by_yourself(self, mock_wife):
        michael = Pursuit(target=mock_wife)
        assert michael.give_money() == 0

    def test_give_flower_by_yourself(self, mock_wife):
        michael = Pursuit(target=mock_wife)
        assert michael.give_flower() == ''

    def test_give_money_via_proxy(self, mock_wife):
        michael = Pursuit(target=mock_wife)
        bruce = Proxy(who=michael)
        assert bruce.give_money() == 1_000

    def test_give_flower_via_proxy(self, mock_wife):
        michael = Pursuit(target=mock_wife)
        bruce = Proxy(who=michael)
        assert bruce.give_flower() == '向日葵'
