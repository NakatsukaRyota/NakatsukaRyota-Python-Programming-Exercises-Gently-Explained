def convertStrToInt(stringNum):
    DIGIT_STR_TO_NUM = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                        "6": 6, "7": 7, "8": 8, "9": 9}
    
    if stringNum[0] == "-":
        isNegative = True
        stringNum = stringNum[1:]
    else:
        isNegative = False
    
    result = 0
    lengthStr = len(stringNum)
    for str in stringNum:
        num = DIGIT_STR_TO_NUM[str]
        result += num * (10 ** (lengthStr - 1))
        lengthStr -= 1

    if isNegative:
        return -result
    else:
        return result

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
