def test_function_1():
    ...


def test_function_2():
    ...


def test_function_3():
    ...
import requests

data = requests.get(f'https://pokeapi.co/api/v2/pokemon/pikachu')
print(data.json()['height'])
