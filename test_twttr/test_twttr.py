import twttr

variable = input()

def test_null():

    x = twttr.shorten()
    assert x


def test_argument():

    x = twttr.shorten(variable)
    assert x