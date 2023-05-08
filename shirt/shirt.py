import sys
from PIL import Image

def main():
    system_check(sys.argv)
    shirt_changer(sys.argv[1], sys.argv[2])

def system_check(argument):

    if len(argument) < 3:
        sys.exit('Too few command-line arguments')

    elif len(argument) > 3:
        sys.exit('Too many command-line arguments')

    file_name = argument[1].lower()


    if not file_name.endswith('.jpg') and not file_name.endswith('.jpeg') and not file_name.endswith('.png') :
        sys.exit('Invalid output')

    else:
        try:
            with open(file_name, "r") as file:
                pass
        except FileNotFoundError:
            sys.exit('Input does not exist')

def shirt_changer(input, output):
    pass

if __name__ == '__main__':
    main()