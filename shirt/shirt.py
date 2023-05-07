import sys

def main():
    system_check(sys.argv)

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

def shirt_changer(self):
    

if __name__ == '__main__':
    main()