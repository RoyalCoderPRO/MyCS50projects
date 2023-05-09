import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Returns 'None' for no input
    if s == None:
        return None
    source = re.split("src=", s)
    source = re.split(r'/"', source[1])
    print(source)
    source = re.split(r'/"', source[0])
    print(source)
    source = source[0].strip()
    source = source.strip('"')
    return source


if __name__ == "__main__":
    main()
