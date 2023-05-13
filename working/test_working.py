from working import convert

def test_conversion():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

