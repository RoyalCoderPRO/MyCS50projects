from twttr import shorten

def test_null():

    assert shorten('Twitter') == 'Twttr'
    assert shorten('TwItter') == 'Twttr'
    assert shorten('Tw1tter') == 'Tw1ttr'
    assert shorten('Tw,tter') == 'Tw,ttr'