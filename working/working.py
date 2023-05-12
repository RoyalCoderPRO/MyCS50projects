import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_range = re.findall(r'1?\d?:*[0-5]*\d*\s.M',s)
    print(time_range)
    pm_yes = False
    for times in time_range:
        if 'AM' in times:
            times = int(times.strip(' AM'))
        elif 'PM' in times:
            times = int(times.strip(' PM'))
            pm_yes = True
        if ':' in times:
            hour = int(times.split(':')[0])
        if hour > 12:
            raise ValueError

        print(hour)




if __name__ == "__main__":
    main()