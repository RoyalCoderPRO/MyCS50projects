import sys
from tabulate import tabulate
import csv
def main():
    system_check(sys.argv)
    printer(sys.argv[1])

def system_check(argument):

    if len(argument) < 2:
        sys.exit('Too few command-line arguments')

    elif len(argument) > 2:
        sys.exit('Too many command-line arguments')

    file_name = argument[1]


    if file_name[-4:] != '.csv':
        sys.exit('Not a CSV file')
    else:
        try:
            with open(file_name, "r") as file:
                pass
        except FileNotFoundError:
            sys.exit('File does not exist')

def printer(menu):
    dishes = []
    with open(menu, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            dishes.append({'name':row[0], 'small': row[1], 'large': row[2]})
    print(tabulate(dishes, headers= 'firstrow',tablefmt= 'grid'))


if __name__ == '__main__':
    main()