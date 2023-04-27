from plates import is_valid
def test():
    assert is_valid('ad2034') == True
    assert is_valid('Adit1230') == False
    assert is_valid('ad0234') == False
    assert is_valid('0asdf') == False
    assert is_valid('afd_df') == False
    assert is_valid('a23') == False
    assert is_valid('kd23k') == False
    assert is_valid('d') == False
