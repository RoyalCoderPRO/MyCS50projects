import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Returns 'None' for no input
    if s == None:
        return None
    source = re.split("src=", s)
    source = re.split('"', source[1])
    source = source[1].strip()
    source = source.strip('"')
    return source


if __name__ == "__main__":
    main()
