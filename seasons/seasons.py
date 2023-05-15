from datetime import date, timedelta
import sys

def main():
    print(time_calc(input('Date of Birth: '))) #YYYY-MM-DD

def time_calc(d):
    abs = date.today()
    print(abs)
    try:
        time_birth = date.fromisoformat(d)
        new_time = timedelta()
        new_time = abs - time_birth

    except:
        sys.exit()

    finally:
        return new_time


if __name__ == "__main__":
    main()