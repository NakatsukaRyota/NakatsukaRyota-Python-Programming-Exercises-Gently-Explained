def median(numbers):
    if len(numbers) == 0:
        return None
    
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        half_size = size // 2
        result = (numbers[half_size] + numbers[half_size - 1]) / 2
        return result
    else:
        half_size = (size // 2) 
        return numbers[half_size]

assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6
