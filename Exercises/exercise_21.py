import exercise_20

MONTH_HAVE_31DAY = [1, 3, 5, 7, 8, 10, 12]
MONTH_HAVE_30DAY = [4, 6, 9, 11]

def isValidDate(year, month, day):
    if year < 0:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if month in MONTH_HAVE_31DAY:
        if day < 1 or day > 31:
            return False
    elif month in MONTH_HAVE_30DAY:
        if day < 1 or day > 30:
            return False
    else:
        if exercise_20.isLeapYear(year):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    return True

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False


import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay            