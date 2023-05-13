import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if not re.search(r'1?\d{1}:*[0-5][0-9]\s.M\sto\s1?\d?:*[0-5]*\d*\s.M', s):
        raise ValueError

    time_range = re.findall(r'1?\d?:*[0-5]*\d*\s.M',s)
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
            minute = False
        if hour > 12:
            raise ValueError
        if pm_yes:
            hour += 12
        hour = str(hour)
        if len(hour) == 1:
            hour = '0' + hour
        if minute:
            minute = str(minute)
            new_time_range.append(hour + ':' + minute)
        else:
            new_time_range.append(hour + ':00')
        pm_yes = False


    return new_time_range[0] + ' to ' + new_time_range[1]



if __name__ == "__main__":
    main()