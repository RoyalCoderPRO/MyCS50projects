import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_range = re.findall(r'1?\d?:*[0-5]*\d*\s.M',s)
    print(time_range)
    pm_yes = False
    new_time_range = []
    for times in time_range:
        if 'AM' in times:
            times = times.strip(' AM')
        elif 'PM' in times:
            times = times.strip(' PM')
            pm_yes = True
        if ':' in times:
            hour, minute = times.split(':')
            hour, minute = int(hour), int(minute)
        else:
            hour = int(times)
        if hour > 12:
            raise ValueError
        if pm_yes:
            hour += 12
        hour, minute = str(hour), str(minute)
        if len(hour) == 1:
            hour = '0' + hour
        if minute:
            new_time_range.append(hour + ':' + minute)
        else:
            new_time_range.append(hour + ':00')


    return new_time_range



if __name__ == "__main__":
    main()