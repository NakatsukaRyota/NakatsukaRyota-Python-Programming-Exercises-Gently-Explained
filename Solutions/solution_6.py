# alternative solutino
def ordinalSuffix(number):
    if number % 100 in (11, 12, 13):
        return str(number) + "th"
    if number % 10 == 1:
        return str(number) + "st"
    if number % 10 == 2:
        return str(number) + "nd"
    if number % 10 == 3:
        return str(number) + "rd"
    return str(number) + "th"