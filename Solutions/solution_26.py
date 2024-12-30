def printHandShakes(people):
    numberOfShakes = 0
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i], "shakes hands with", people[j])
            numberOfShakes += 1
    return numberOfShakes