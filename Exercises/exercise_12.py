def getSmallest(numbers):
    if numbers == []:
        return None
    
    smallestNum = numbers[0]
    for num in numbers:
        for i in range(len(numbers)):
            if smallestNum > numbers[i]:
                smallestNum = numbers[i]

    return smallestNum


assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None