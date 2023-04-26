def main():
    value()

def value(greeting = 'Yo'):
    x = greeting.lower().split()
    if 'hello' in x[0]:
        return '$0'
    elif 'h' == x[0][0]:
        return '$20'
    else:
        return '$100'


if __name__ == "__main__":
    main()
