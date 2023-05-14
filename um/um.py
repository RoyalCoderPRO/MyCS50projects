import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    counter = 0
    all_ums = re.findall(r'\bum\b', s)
    for um in all_ums:
        counter += 1

    return counter

if __name__ == "__main__":
    main()