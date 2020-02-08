import pytest
from unittest import TestCase


@pytest.fixture()
def fx_return_value():
    yield 'some returned value'


@pytest.mark.usefixtures(fx_return_value.__name__)
def test0(fx_return_value):
    print(fx_return_value)


class Test1(TestCase):
    @pytest.mark.usefixtures(fx_return_value.__name__)
    def test1(self, fx_return_value):  #TODO Error here > TypeError: test1() missing 1 required positional argument: 'fx_return_value'
        print(fx_return_value)
