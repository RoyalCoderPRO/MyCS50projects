import requests
def main():
    match menu():
        case '1':
            pokelister()
        case '2':
            pokereader()




def menu():
    value = str(input("Enter 1 for putting new pokemon in your pokedex\n Enter 2 for reading your pokemon\n:"))


def pokereader():
    with open('Pokedex.txt', mode= 'r') as file:
        for line in file:
            if line.startswith(' '):
                continue
            pokemon_name = line
            print(pokemon_name)



def pokelister():
    # start editing
    with open('PokeDex.txt', mode= 'a') as file:
        # create loop to keep appending until exit program
        while True:
            # user input for pokemon name
            pokemon_name = input('Which pokemon would you like to add to pokedex?: ').capitalize()
            # checks for request error
            try:
                data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
                data.json()['height']
            # resets input for revising
            except:
                print('Not a pokemon, try again')
                pass
            # enters name

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
                types = types_num['type']
                name_type = types['name']
                file.write(f'   {j}> {name_type}\n')

            file.close
            break

    return repeater()
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
    while pokelister() == 'Y':
        pass
