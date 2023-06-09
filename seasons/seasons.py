from datetime import date, timedelta
import sys
import inflect

def main():
    print(time_calc(input('Date of Birth: '))) #YYYY-MM-DD


def time_calc(d):
    p = inflect.engine()
    abs = date.today()
    try:
        time_birth = date.fromisoformat(d)
        new_time = timedelta()
        new_time = abs - time_birth
        new_time = new_time.total_seconds()/60
        new_time = p.number_to_words(int(new_time), andword="").capitalize()
        new_time = new_time + " minutes"
        return new_time

    except (UnboundLocalError, ValueError):
        sys.exit('Invalid date')

if __name__ == "__main__":
    main()