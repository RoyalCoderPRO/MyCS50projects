from twttr import shorten

variable = 'Twitter'
def test_null():

    x = shorten()
    assert x


def test_argument():

    x = shorten(variable)
    assert x