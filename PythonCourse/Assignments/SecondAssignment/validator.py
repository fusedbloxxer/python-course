control_num = 279146358279

total_counties = 52

months_to_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


def is_foreigner(cnp: dict) -> bool:
    return 7 <= cnp["S"] <= 9


def is_born_in_bucharest(cnp: dict) -> bool:
    return 41 <= cnp["JJ"] <= 46


def is_leap_year(year: int) -> bool:
    if year < 0:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def find_birth_year(cnp: dict) -> int:
    if cnp["S"] == 0:
        return -1

    return cnp["AA"] + (1800 if 3 <= cnp["S"] <= 4 else 2000 if 5 <= cnp["S"] <= 6 else 1900)


def find_days_in_month_and_year(month: int, year: int) -> int:
    if month not in months_to_days:
        return -1

    return months_to_days[month] + (1 if month == 2 and is_leap_year(year) else 0)


def is_cnp_valid(cnp: str) -> bool:
    if len(cnp) != 13:
        return False

    if not cnp.isdigit():
        return False

    cnp = {
        "S": int(cnp[0]),
        "AA": int(cnp[1:3]),
        "LL": int(cnp[3:5]),
        "ZZ": int(cnp[5:7]),
        "JJ": int(cnp[7:9]),
        "NNN": int(cnp[9:12]),
        "C": int(cnp[12])
    }

    if (birth_year := find_birth_year(cnp)) == -1:
        return False

    if (available_days := find_days_in_month_and_year(cnp["LL"], birth_year)) == -1:
        return False

    if cnp["ZZ"] == 0 or cnp["ZZ"] > available_days:
        return False

    if cnp["JJ"] == 0 or cnp["JJ"] > total_counties:
        return False

    if is_foreigner(cnp) and is_born_in_bucharest(cnp):
        return False

    if cnp["NNN"] == 0:
        return False

    control_digit = 0
    control_num_len = len(str(control_num)) - 1

    for item in cnp.items():

        if item[0] == "C":
            break

        for power in range(len(item[0]), 0, -1):
            control_num_digit = control_num // 10 ** control_num_len % 10
            current_num_digit = item[1] // 10 ** (power - 1) % 10
            control_digit += current_num_digit * control_num_digit
            control_num_len -= 1

    control_digit %= 11

    return cnp["C"] == (1 if control_digit == 10 else control_digit)


while True:
    print(is_cnp_valid(input("Enter CNP: ")))