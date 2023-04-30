import sys
def main():
    system_check(sys.argv)
    print(checker(sys.argv[1]))


def system_check(argument):

    if len(argument) < 2:
        sys.exit('Too few command-line arguments')

    elif len(argument) > 2:
        sys.exit('Too many command-line arguments')

    file_name = argument[1]


    if file_name[-3:] != '.py':
        sys.exit('Not a Python file')
    else:
        try:
            with open(file_name, "r") as file:
                pass
        except FileNotFoundError:
            sys.exit('File does not exist')


def checker(x):
    with open(x, 'r') as file:
        lines = file.readlines()
    complexity = 0
    for line in lines:
        line_in = line.strip()
        if line_in.startswith('#'):
            pass
        elif line_in == '':
            pass
        else:
            complexity += 1
    return complexity


if __name__ == "__main__":
    main()
