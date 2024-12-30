def mode(numbers):
    if len(numbers) == 0:
        return None
    
    counter = {}
    for number in numbers:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 0

    for key in counter.keys():
        if counter[key] == max(counter.values()):
            return key

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4