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
    new_dict = []
    with open(old, "r") as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            last, first = row['name'].split(', ')
            house = row['house']
            new_dict.append({'first':first, 'last':last, 'house':house})
    with open(new, "w") as file:
        file_writer = csv.DictWriter(file, fieldnames= ['first','last','house'])
        file_writer.writeheader()
        for row in new_dict:
            file_writer.writerow(row)


if __name__ == '__main__':
    main()
