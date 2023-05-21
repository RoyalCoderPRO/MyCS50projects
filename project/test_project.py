import project

def test_pokereader():
    assert project.pokereader() == None


def test_pokelister():
    assert project.pokelister('Pikachu') == None


def test_repeater():
    assert project.checker('Pikachu') == 0
    assert project.checker('random_name') == 1
