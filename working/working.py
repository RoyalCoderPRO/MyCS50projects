import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.findall(r'1?\d?:[0-5]\d+',s)
    new_match = re.sub(r'1?\d?:[0-5]\d+', ,s)
    return match

if __name__ == "__main__":
    main()