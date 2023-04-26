from bank import value

def test_hello():
    assert value('Hello There') == '$0'

def test_hi():
    assert value('Hi There') == '$20'

def test_nonh():
    assert value('Whats up') == '$100'