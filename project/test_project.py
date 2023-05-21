import project

def test_pokereader():
    assert project.pokereader() == 'Pokedex pokemon read'


def test_pokelister():
    assert project.pokelister('Pikachu') == 'Pokemon added to PokeDex.txt'


def test_repeater():
    assert project.checker('Pikachu') == 0
    assert project.checker('random_name') == 1
