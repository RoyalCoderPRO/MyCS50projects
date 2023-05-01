import sys
import csv

def main():
    system_check(sys.argv)
    scourger(sys.argv[1], sys.argv[2])


def system_check(argument):

    if len(argument) < 3:
        sys.exit('Too few command-line arguments')

    elif len(argument) > 3:
        sys.exit('Too many command-line arguments')

    file_name = argument[1]


    if file_name[-4:] != '.csv':
        sys.exit('Could not read ' + file_name)
    else:
        try:
            with open(file_name, "r") as file:
                pass
        except FileNotFoundError:
            sys.exit('Could not read' + file_name)


def scourger(old, new):
    with open(old, "r") as file:
        file_colmn = csv.DictReader(file, fieldnames= ['name','house'])
    first, last = file_colmn['name'].split(',')
    house = file_colmn['house']
    new_dict = {first, last, house}
    with open (new, 'a') as file:
        file.write(new_dict)


if __name__ == '__main__':
    main()
