def main():
    print(convert())
    print(gauge(convert(input('Enter fraction: '))))


def convert(fraction='5/0'):
    try:
        x, y = fraction.split('/')
        z = int(x)/int(y)
        assert z <= 1
    except ZeroDivisionError:
        raise ZeroDivisionError
    except (AssertionError, ValueError):
        raise ValueError
    else:
        return round(z*100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return (str(percentage)) + '%'


if __name__ == "__main__":
    main()





