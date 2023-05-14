import re


def main():
    print(count(input("Text: ").lower()))


def count(s):
    counter = 0
    all_ums = re.findall(r'\bum\b', s)
    for um in all_ums:
        counter += 1

    return counter

if __name__ == "__main__":
    main()