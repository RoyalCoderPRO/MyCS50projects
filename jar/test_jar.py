from jar import Jar
from pytest import raises

def test_jar():
    bottle = Jar(12)
    with raises(ValueError):
        Jar.deposit(bottle, 15)

test_jar()
