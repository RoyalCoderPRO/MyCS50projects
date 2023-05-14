import re


def main():
    print(count(input("Text: ")))


def count(s):
    all_ums = re.findall(r' um ', s)
    all_ums.append(re.findall(r'^um', s))
    all_ums.append(re.findall(r'/Zum', s))
    print(all_ums)

if __name__ == "__main__":
    main()