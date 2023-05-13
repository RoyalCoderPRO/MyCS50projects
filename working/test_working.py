from working import convert
from pytest import raises

def test_conversion():
    with raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with raises(ValueError):
        convert('9 AM - 5 PM')
    with raises(ValueError):
        convert('09:00 AM - 17:00 PM')
    assert ('9 AM to 5 PM') == '09:00 to 17:00'
    assert ('10:30 PM to 8:50 AM') == '22:30 to 08:50'



