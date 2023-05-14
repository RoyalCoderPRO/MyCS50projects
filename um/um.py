import re


def main():
    print(count(input("Text: ")))


def count(s):
    all_ums = re.findall(r' um ', s)
    all_ums = all_ums.append(re.findall(r'^um', s))
    print(all_ums)

if __name__ == "__main__":
    main()