from plates import is_valid
def test():
    assert is_valid('0ad234f') == False
    assert is_valid('Adit1230') == False
    assert is_valid('12lkakasdlkf') == False
    assert is_valid('afa230') == True
    assert is_valid('12454sfd') == False
