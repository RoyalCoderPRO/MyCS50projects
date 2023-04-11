from twttr import shorten

def test_null():

    assert shorten('Twitter') == 'Twttr'


def test_argument():

    x = shorten(variable)
    assert x