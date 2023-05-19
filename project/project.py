import requests

def main():
    # start editing
    with open('PokeDex.word', mode= 'a') as file:
        # create loop to keep appending until exit program
        while True:
            # user input for pokemon name
            pokemon_name = input('Which pokemon would you like to add to pokedex?: ').lower()
            # checks for request error
            try:
                data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
                data.json()['height']
            # resets input for revising
            except:
                print('Not a pokemon, try again')
                pass
            # enters name
            else:
                pokemon_name = pokemon_name.capitalize()
                i = 0
                file.write(f'{pokemon_name}:\n  Abilities: \n')
                # indexes desired 'ability' and 'ability slot'
                for ability_num in data.json()['abilities']:
                    i += 1
                    ability = ability_num['ability']
                    name = ability['name']
                    slot = ability_num['slot']
                    name_type = []
                    # prints into txt file
                    file.write(f'   {i}> {name}, slots: {slot},\n')
                file.write(f'  Types:\n')
                j = 0
                # indexes desired 'types'
                for types_num in data.json()['types']:
                    j += 1
                    types = types_num['type']
                    name_type = types['name']
                    file.write(f'   {j}> {name_type}\n')

                file.close
                break

    # for repeating application task
    repeat = input('Done! Would you like to add any other Pokemon to your Pokedex?: (Y/N) ')
    while True:
        try:
            assert repeat == 'Y' or repeat == 'N'
        except:
            repeat = input("Only enter 'Y' or 'N' to answer 'Yes' or 'No':")
        else:
            break

    return repeat
# takes return value of main and repeats if Y
while main() == 'Y':
    pass