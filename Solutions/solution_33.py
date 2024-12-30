def commaFormat(number):
    number = str(number)

    if "." in number:
        fractionalPart = number[number.index("."):]
        number = number[:number.index(".")]
    else:
        fractionalPart = ""

    triplet = ""
    commaNumber = ""

    for i in range(len(number) - 1, -1, -1):
        triplet = number[i] + triplet
        if len(triplet) == 3:
            commaNumber = triplet + "," + commaNumber
            triplet = ""

    if triplet != "":
        commaNumber = triplet + "," + commaNumber

    return commaNumber + fractionalPart

print(commaFormat(1000))