while True:
    try:
        x, y = input('Fraction: ').split('/')
        z = int(x)/int(y)
        if z< 0:
            print('E')
            break
        elif z> 99:
            print('F')
            break
        else:
            print(str(z) + '%')
    except (ValueError, ZeroDivisionError):
        pass


