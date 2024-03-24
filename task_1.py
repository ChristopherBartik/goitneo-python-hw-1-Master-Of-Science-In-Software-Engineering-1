# Press the green button in the gutter to run the script.
from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    today = datetime.now()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Adjust start_date to the next Monday if today is not Monday
    start_date = today + timedelta((7 - today.weekday()) % 7)  # Monday is 0, Sunday is 6
    end_date = start_date + timedelta(days=7)

    # Dictionary to hold birthday names categorized by weekdays
    birthdays = defaultdict(list)

    for user in users:
        # Extract user's upcoming birthday this year
        birthday_this_year = user["birthday"].replace(year=today.year)

        # If the birthday has already passed this year, set it for the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Adjust weekend birthdays to Monday
        if birthday_this_year.weekday() > 4:  # Saturday or Sunday
            birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

        if start_date <= birthday_this_year < end_date:
            day_of_week = weekdays[birthday_this_year.weekday()]
            birthdays[day_of_week].append(user["name"])

    # Print formatted output
    for day in weekdays[:5]:  # Only Monday to Friday
        if birthdays[day]:
            names = ", ".join(birthdays[day])
            print(f"{day}: {names}")


if __name__ == '__main__':

    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Jill Valentine", "birthday": datetime(1974, 11, 1)},
        {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)}
    ]

    get_birthdays_per_week(users)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
