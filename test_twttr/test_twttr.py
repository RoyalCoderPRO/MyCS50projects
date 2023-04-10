from twttr import shorten

def test_null():

    x = shorten()
    assert x


def test_argument():

    x = shorten(variable)
    assert x