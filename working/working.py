import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_range = re.findall(r'1?\d?:[0-5]\d+',s)
    for times in time_range:
        hour = int(times.split(':')[0])
        if hour > 12:
            



if __name__ == "__main__":
    main()