def convertIntToStr(integerNum):
    if integerNum == 0:
        return "0"

    if integerNum > 0:
        numList = {}
        i = 0
        while integerNum > 0:
            num = (integerNum // (10 ** i)) % 10
            numList[i] = num
            integerNum -= num * (10 ** i)
            i += 1

        result = ""
        for key in numList:
            num = numList[key]
            if num == 0:
                result = "0" + result
            elif num == 1:
                result = "1" + result
            elif num == 2:
                result = "2" + result
            elif num == 3:
                result = "3" + result
            elif num == 4:
                result = "4" + result
            elif num == 5:
                result = "5" + result
            elif num == 6:
                result = "6" + result
            elif num == 7:
                result = "7" + result
            elif num == 8:
                result = "8" + result
            elif num == 9:
                result = "9" + result

        return result
    
    if integerNum < 0:
        integerNum = -integerNum
        numList = {}
        i = 0
        while integerNum > 0:
            num = (integerNum // (10 ** i)) % 10
            numList[i] = num
            integerNum -= num * (10 ** i)
            i += 1

        result = ""
        for key in numList:
            num = numList[key]
            if num == 0:
                result = "0" + result
            elif num == 1:
                result = "1" + result
            elif num == 2:
                result = "2" + result
            elif num == 3:
                result = "3" + result
            elif num == 4:
                result = "4" + result
            elif num == 5:
                result = "5" + result
            elif num == 6:
                result = "6" + result
            elif num == 7:
                result = "7" + result
            elif num == 8:
                result = "8" + result
            elif num == 9:
                result = "9" + result

        result = "-" + result
        return result



for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)