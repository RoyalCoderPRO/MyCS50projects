import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.fullmatch(r'1?\d?:[0-5]?\d?+',s):
        return True

if __name__ == "__main__":
    main()