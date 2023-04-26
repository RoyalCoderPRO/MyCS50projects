def main():
    print(value())

def value(greeting = 'Hello There'):
    x = greeting.lower().split()
    if 'hello' in x[0]:
        return '$0'
    elif 'h' == x[0][0]:
        return '$20'
    else:
        return '$100'


if __name__ == "__main__":
    main()
