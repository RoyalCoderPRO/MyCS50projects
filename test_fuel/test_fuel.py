import fuel
import pytest

def test_gauge():
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(22) == '22%'

def test_convert():
    assert fuel.convert('99/100') == 99
    assert fuel.convert('0/100') == 0
    assert fuel.convert('22/100') == 22
    with pytest.raises(ZeroDivisionError):
       fuel.convert('2/0')
    with pytest.raises(ValueError):
       fuel.convert('105/100')

