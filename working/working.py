import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_range = re.findall(r'1?\d?:*[0-5]*\d*\s.M',s)
    for times in time_range:
        if ':' in times:
            hour = int(times.split(':')[0])
        elif 'AM' in times:
            hour = int(times.strip('AM'))
            
        elif 'PM' in times:
            hour = int(times.strip('PM'))
        if hour > 12:
            raise ValueError
        print(hour)




if __name__ == "__main__":
    main()