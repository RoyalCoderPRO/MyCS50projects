from jar import Jarring
from pytest import raises

def test_jar():
    bottle = Jarring(12)
    with raises(ValueError):
        Jarring.deposit(bottle, 15)

test_jar()
