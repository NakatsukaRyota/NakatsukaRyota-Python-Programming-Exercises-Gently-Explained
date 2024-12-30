import random


def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        
    return smallest

numbers = []
for i in range(10000000):
    numbers.append(random.randint(1, 10000000000))
print("Numbers:", numbers)
print("Smallest number is", getSmallest(numbers))
