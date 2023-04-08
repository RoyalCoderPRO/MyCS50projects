def main():
    if 7 <= convert(input('What time is it? ')) <= 8:
        print('breakfast time')
    elif 12 <= convert()



def convert(time):
    hour, minutes = time.split(:)
    hour, minutes = int(hour), int(minutes)
    x = hour + (minutes/60)
    return x


if __name__ == "__main__":
    main()