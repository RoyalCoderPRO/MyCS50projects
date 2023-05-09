import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Returns 'None' for no input
    truth = re.search(".+youtube.+",s)
    print(truth)
    if s == None or re.search(".+youtube.+",s):
        return None
    source = re.split("src=", s)
    source = re.split('"', source[1])
    source = source[1].strip()
    source = source.strip('"')
    slug = source.split('/')[-1]
    slug = 'https://youtu.be/embed/' + slug
    return slug
# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# or re.search(r'[youtube]+',s)
if __name__ == "__main__":
    main()
