def main():
    if convert(input('What time is it? ')) <:



def convert(time):
    hour, minutes = time.split(:)
    hour, minutes = int(hour), int(minutes)
    x = hour + (minutes/60)
    return x


if __name__ == "__main__":
    main()