# ---------------------------------------------------------------- Function with outputs

def format_name(f_name, l_name):
    if f_name == '' and l_name == '':
        return 'You didn\'t provide anything'

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f'{formatted_f_name} {formatted_l_name}'


formatted_string = format_name('IvO', 'PeycHo')
formatted_string2 = format_name('', '')
print(formatted_string)
print(formatted_string2)


# ----------------------------------------------------------------  Days in month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return 'Invalid month'

    # month_index = month - 1
    # if is_leap(year) and month == 2:
    #     number_of_days = month_days[month_index] + 1
    # else:
    #     number_of_days = month_days[month_index]

    if is_leap(year) and month == 2:
        return 29

    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

