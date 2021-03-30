month_days = [0, 31, 28, 31, 30, 31, 30,  31,  31,  30, 31, 30,

def is_leap(year): 
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)


def days_in_month(year, month):
     """Return number of day's that month in that year."""

    if not 1 <=mouth <=12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29

    return month_days(month)

    print(day_in_mounth(2017,   2))  mantra madar