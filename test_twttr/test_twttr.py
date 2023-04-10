import twttr

x = input()

def test_null():
    x = twttr.shorten()
    assert x


def test_argument(x):
    x = twttr.shorten(x)
    assert x