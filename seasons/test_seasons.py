from seasons import time_calc
from pytest import raises

def test_time():
    assert time_calc('2004-01-18') == time_calc('2004-01-18')
