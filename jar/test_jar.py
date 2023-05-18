from jar import Jar
from pytest import raises

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar(4)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(3)
    jar.deposit(3)
    assert jar.size == jar.capacity
    with raises(ValueError):
        jar.deposit(1)
def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with raises(ValueError):
        jar.withdraw(2)
