def ordinalSuffix(number):
    number = str(number)

    if number[-2:] in ("11", "12", "13"):
        return number + "th"
    if number[-1] == "1":
        return number + "st"
    if number[-1] == "2":
        return number + "nd"
    if number[-1] == "3":
        return number + "rd"
    return number + "th"
    
assert ordinalSuffix(0) == '0th'
ordinalSuffix(1)
assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'