import random

def calculateSum(numbers):
    total = 0
    for number in numbers:
        total += number

    return total

def calculateProduct(numbers):
    total = 1
    for number in numbers:
        total *= number

    return total


assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840

numbers = [] 
for i in range(10000):
    numbers.append(random.randint(1, 100000))
print("Numbers:", numbers)
print("Sum", calculateSum(numbers))
print("Product", calculateProduct(numbers))
