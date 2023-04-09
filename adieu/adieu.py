while True:
    names = []
    try:
        names.append(input('Name: '))

    except EOFError:
        break