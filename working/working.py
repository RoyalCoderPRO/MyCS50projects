import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r'[0]:\d\d+',s):
        return True

if __name__ == "__main__":
    main()