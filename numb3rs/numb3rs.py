import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    re.search("\.\.\.\.", ip)


...


if __name__ == "__main__":
    main()