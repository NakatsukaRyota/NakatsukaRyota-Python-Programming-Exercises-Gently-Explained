def mode(numbers):
    if len(numbers) == 0:
        return None
    numberCount = {}

    mostFreqNumber = None
    mostFreqNumberCount = 0

    for number in numbers:
        if number not in numberCount:
            numberCount[number] = 0
        numberCount[number] += 1

        if numberCount[number] > mostFreqNumber:
            mostFreqNumber = number
            mostFreqNumberCount = numberCount[number]
        
    return mostFreqNumber