while True:
    try:
        x, y = input('Fraction: ').split('/')
        z = int(x)/int(y)
        if z< 1:
            print('E')
            break
        elif z> 99:
            print('F')
            break
        else:
            print(str(z) + '%')
            break
    except (ValueError, ZeroDivisionError):
        pass


