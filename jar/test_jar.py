from jar import Jar
from pytest import raises

def test_jar():
    with raises(ValueError):
        bottle = Jar(12)
        Jar.deposit(bottle, 15)
        print(bottle)


test_jar()
