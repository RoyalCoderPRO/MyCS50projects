import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    all_ums = re.match(r'um', s)
    print(all_ums)

    for um in all_ums:
        counter += 1

    return counter

if __name__ == "__main__":
    main()