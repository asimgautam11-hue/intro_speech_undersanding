def next_birthday(date, birthdays):
    if not birthdays:
        return (1, 1), []

    sorted_dates = sorted(birthdays.keys())

    for bday in sorted_dates:
        if bday > date:
            return bday, birthdays[bday]

    next_date = sorted_dates[0]
    return next_date, birthdays[next_date]


if __name__ == "__main__":
    sample_birthdays = {
        (5, 15): ["Hari", "Sita"],
        (10, 20): ["Gopal"],
        (1, 10): ["Ram"]
    }

    current_date_1 = (5, 12)
    bday_1, names_1 = next_birthday(current_date_1, sample_birthdays)
    print(f"Current Date: {current_date_1} -> Next Birthday: {bday_1} (Names: {names_1})")

    current_date_2 = (11, 5)
    bday_2, names_2 = next_birthday(current_date_2, sample_birthdays)
    print(f"Current Date: {current_date_2} -> Next Birthday: {bday_2} (Names: {names_2})")