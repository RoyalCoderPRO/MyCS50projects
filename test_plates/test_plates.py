from plates import is_valid
def test():
    assert is_valid('0ad234f') == False
    assert is_valid('Adit1230') == False
    assert is_valid('12lkakasdlkf') == False
    assert is_valid('asdfa23') == False
    assert is_valid('12454sfd') == False
