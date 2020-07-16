import pytest
from singleton.singleton_decorator import S1, S2


class TestSingleton:


    def test_overwrite_new(self):
        s1 = S1()
        s2 = S1()

        assert id(s1) == id(s2)

    def test_use_decorator(self):
        s3 = S2()
        s4 = S2()
        assert id(s3) == id(s4)