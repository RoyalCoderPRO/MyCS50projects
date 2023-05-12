import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_range = re.findall(r'1?\d?:*[0-5]*\d*\s.M',s)
    for times in time_range:
        if ':' in times:
            hour = int(times.split(':')[0])
        else:
            hour = times.strip('AM')
            hour = times.strip('PM')
        if hour > 12:
            raise ValueError




if __name__ == "__main__":
    main()