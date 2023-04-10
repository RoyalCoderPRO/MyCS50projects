import twttr

x = input()

def test_null():
    try:
        x = twttr.shorten()
        assert x
    except AssertionError:
        pass



def test_argument(x):
    twttr.shorten()