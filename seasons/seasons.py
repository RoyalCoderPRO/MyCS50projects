from datetime import date, timedelta
import sys

def main():
    print(time_calc(input('Date of Birth: '))) #YYYY-MM-DD

def time_calc(d):
    abs = date(0000)
    try:
        time_birth = date.fromisoformat(d)
        print(abs)
        new_time = time_birth - abs
        print(new_time)

    except:
        sys.exit()

    finally:
        return time_birth


if __name__ == "__main__":
    main()