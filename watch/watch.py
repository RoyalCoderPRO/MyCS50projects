import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Returns 'None' for no input
    if s == None or not re.search("iframe.+youtube.+",s):
        return None
    source = re.split("src=", s)
    source = re.split('"', source[1])
    source = source[1].strip()
    source = source.strip('"')
    slug = source.split('/')[-1]
    slug = 'https://youtu.be/' + slug
    return slug

if __name__ == "__main__":
    main()
