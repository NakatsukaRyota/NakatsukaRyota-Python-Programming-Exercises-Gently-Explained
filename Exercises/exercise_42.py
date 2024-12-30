def bubbleSort(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            
    return numbers

bubbleSort([2, 0, 4, 1, 3])

assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]