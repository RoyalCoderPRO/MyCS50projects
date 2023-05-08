import sys
from PIL import Image, ImageOps

def main():
    system_check(sys.argv)
    shirt_changer(sys.argv[1], sys.argv[2])

def system_check(argument):

    #Variables
    file_name = argument[1].lower()

    #Checking number of arguments
    if len(argument) < 3:
        sys.exit('Too few command-line arguments')

    elif len(argument) > 3:
        sys.exit('Too many command-line arguments')

    #Checking image type input
    elif not file_name.endswith('.jpg') and not file_name.endswith('.jpeg') and not file_name.endswith('.png'):
        sys.exit('Invalid output')

    #Checking image type output and extension consistency
    elif file_name.endswith('.jpg') and not argument[2].lower().endswith('.jpg'):
        sys.exit('Input and output have different extensions')
    elif file_name.endswith('.jpeg') and not argument[2].lower().endswith('.jpeg'):
        sys.exit('Input and output have different extensions')
    elif file_name.endswith('.png') and not argument[2].lower().endswith('.png'):
        sys.exit('Input and output have different extensions')

    #Checking if file exists
    else:
        try:
            with Image.open(file_name, mode='r'):
                pass
        except FileNotFoundError:
            sys.exit('Input does not exist')

def shirt_changer(input, output):
    with Image.open('shirt.png') as shirt:
        with Image.open(input) as old:
            old = ImageOps.fit(old, shirt.size)
            old.paste(shirt, shirt)
            old.save(output)

if __name__ == '__main__':
    main()