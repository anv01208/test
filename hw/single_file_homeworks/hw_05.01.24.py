from datetime import datetime, timedelta


def find_next_day(needed_day):
    weekdays = {'Monday': 0,
                'Tuesday': 1,
                'Wednesday': 2,
                'Thursday': 3,
                'Friday': 4,
                'Saturday': 5,
                'Sunday': 6}

    current_date = datetime.now()
    current_day_of_week = current_date.weekday()

    difference = (weekdays[needed_day] - current_day_of_week + 7) % 7
    next_day_date = current_date + timedelta(days=difference)

    print(f"Next {needed_day}: {next_day_date.strftime('%Y-%m-%d')}, after {difference} day(s)")


find_next_day('Saturday')
