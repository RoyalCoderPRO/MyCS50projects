from numb3rs import validate

def test_validate():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3.4.5') == False
    assert validate('11.2234.2.3') == False
    assert validate('11.224.4522.3') == False
    assert validate('11.22.2.653') == False