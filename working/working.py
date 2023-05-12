import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r'1?\d?:[0-5]\d+',s)
    if match:
        first, second = match.groups()
        

    return match

if __name__ == "__main__":
    main()