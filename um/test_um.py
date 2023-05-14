from um import count

def test_counting():
    assert count('um') == 1
    assert count(' um ') == 1
    assert count('Um') == 1
    assert count('"um"') == 1