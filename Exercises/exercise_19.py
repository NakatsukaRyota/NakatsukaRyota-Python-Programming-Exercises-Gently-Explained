import random

def generatePassword(length):
    if length < 12:
        length = 12
    password = []

    specialChar = [33, 35, 36, 37, 38, 40, 41, 42, 42, 64, 94, 95, 126]
    allChar = list(range(97, 123)) + list(range(65, 91)) + list(range(48, 58)) + specialChar

    leftLength = length - 4
    lowerPass = chr(random.randint(97, 122))
    password.append(lowerPass)
    upperPass = chr(random.randint(65, 90))
    password.append(upperPass)
    numPass = chr(random.randint(48, 57))
    password.append(numPass)
    specialPass = chr(specialChar[random.randint(0, 12)])
    password.append(specialPass)

    for i in range(leftLength):
            password.append(chr(allChar[random.randint(0, 73)]))

    random.shuffle(password)    
    return "".join(password)

print(generatePassword(12))