import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    first, second = re.findall(r'[1-91112]?:[0-5]\d+',s)
    print(first + second)


if __name__ == "__main__":
    main()