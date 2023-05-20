import requests


def main():
    match menu():
        case '1':
            pokelister()
        case '2':
            pokereader()




def menu():
    while True:
        try:
            value = str(input("Enter 1 for putting new pokemon in your pokedex\nEnter 2 for reading your pokemon\n"))
            assert value in ['1','2']
        except AssertionError:
            print('Only choose 1 or 2 and press enter\n')
        else:
            return value


def pokereader():
    with open('PokeDex.txt', mode= 'r') as file:
        for line in file:
            if line.startswith(' '):
                continue
            pokemon_name = line.strip('\n').strip(':')
            print(pokemon_name)



def pokelister():
    # start editing
    with open('PokeDex.txt', mode= 'a') as file:
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
            pokemon_name = pokemon_name.capitalize()

            file.write(f'{pokemon_name}:\n  Abilities: \n')
            # indexes desired 'ability' and 'ability slot'
            i = 0
            for ability in data.json()['abilities']:
                i += 1
                name = ability['ability']['name']
                slot = ability['slot']
                name_type = []
                # prints into txt file
                file.write(f'   {i}> {name}, slots: {slot},\n')
            file.write(f'  Types:\n')
            j = 0
            # indexes desired 'types'
            for types_num in data.json()['types']:
                j += 1
                name_type = types_num['type']['name']
                file.write(f'   {j}> {name_type}\n')
            if repeater() == 'N':
                file.close
                break

# takes return value of main and repeats if Y

def repeater():
    while True:
        try:
            repeat = input('Done! Would you like to add any other Pokemon to your Pokedex?: (Y/N) ')
            assert repeat == 'Y' or repeat == 'N'
        except:
            repeat = input("Only enter 'Y' or 'N' to answer 'Yes' or 'No':")
        else:
            return repeat
        # for checking valid value


if __name__ == "__main__":
    main()