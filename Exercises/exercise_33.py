def commaFormat(number):
    if number < 1000:
        return str(number)

    number = str(number)
    isFloat = False
    for i in range(len(number)):
        if number[i] == ".":
            isFloat = True
            floatNum = number[i:]
            number = number[:i]
            break

    numLength = len(number)
    numForLoop = (numLength - 1) // 3
    numForHeadNum = (numLength % 3)
    if numForHeadNum == 0:
        numForHeadNum = 3
    head = number[:numForHeadNum]
    result = ""
    for i in range(numForLoop):
        result =   "," + number[-3:] + result
        number = number[:-3]
    
    result = head + result
    
    if isFloat:
        result = result + floatNum  
        return result
    else:
        return result




assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'