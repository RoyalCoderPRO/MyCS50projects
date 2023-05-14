from datetime import date
import sys

def main():
    print(time_calc(input('Date of Birth: '))) #YYYY-MM-DD

def time_calc(date):
    try:
        time_birth = date.fromisoformat(date)

    except:
        sys.exit()
    finally:
        return time_birth


if __name__ == "__main__":
    main()