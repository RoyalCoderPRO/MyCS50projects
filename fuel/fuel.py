try:
    x, y = input('Fraction: ').split('/')
    print(int(x)/int(y))
except (ValueError, ZeroDivisionError):
    pass


