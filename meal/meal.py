def main():
    x = convert(input('What time is it? '))
    if 7 <= x <= 8:
        print('breakfast time')
    elif 12 <= x <= 13:
        print('lunch time')
    elif 18 <= x <= 19:
        print('dinner time')
    else:
        pass



def convert(time):
    hour, minutes = time.split(':')
    hour, minutes = int(hour), int(minutes)
    x = hour + (minutes/60)
    return x


if __name__ == "__main__":
    main()