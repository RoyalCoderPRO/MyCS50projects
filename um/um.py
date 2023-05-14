import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    all_ums = re.findall(r'\Wum\W', s)

    for um in all_ums:
        counter += 1
    if re.search(r'^um', s):
        counter += 1
    if re.search(r'um\Z', s):
        counter += 1
    return counter

if __name__ == "__main__":
    main()