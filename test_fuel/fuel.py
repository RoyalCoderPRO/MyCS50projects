def main():
    ...


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            z = int(x)/int(y)
            assert z <= 1
            if z <= 0.01:
                return 'E'
            elif z >= 0.99:
                return 'F'
            else:
                print(str(int(round(z*100))) + '%')
                break
        except (ValueError, ZeroDivisionError, AssertionError):
            pass


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()





