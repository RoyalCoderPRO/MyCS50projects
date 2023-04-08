import math
while True:
    try:
        x, y = input('Fraction: ').split('/')
        z = int(x)/int(y)
        assert z <= 1
        if z <= 0.01:
            print('E')
            break
        elif z >= 0.99:
            print('F')
            break
        else:
            print(str(int(math.ceil(z*100))) + '%')
            break
    except (ValueError, ZeroDivisionError, AssertionError):
        pass


