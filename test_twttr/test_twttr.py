from twttr import shorten

def test_null():

    x = twttr.shorten()
    assert x


def test_argument():

    x = twttr.shorten(variable)
    assert x