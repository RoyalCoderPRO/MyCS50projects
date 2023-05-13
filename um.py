import re


def main():
    print(count(input("Text: ")))


def count(s):
    all_ums = re.match('um', s)
    print(all_ums)

if __name__ == "__main__":
    main()