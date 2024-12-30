def printHandshakes(people): 
    num = len(people)
    for i in range(num):
        for j in range(num - 1 - i):
            print(f"{people[i]} shakes hands with {people[i + 1 + j]}")

    numOfShakes = num * (num - 1) / 2
    return numOfShakes

assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6