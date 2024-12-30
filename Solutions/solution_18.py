def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    totalPrice = 0
    cupsUntilFreeCoffee = 8

    while numberOfCoffees > 0:
        numberOfCoffees -= 1
        if cupsUntilFreeCoffee == 0:
            cupsUntilFreeCoffee = 8 
        else:
            totalPrice += pricePerCoffee
            cupsUntilFreeCoffee -= 1
        
    return totalPrice

print(getCostOfCoffee(10000000000, 2.50))

def getCostOfCoffee2(numberOfCoffees, pricePerCoffee):
    numberOfFreeCoffees = numberOfCoffees // 9
    numberOfPaidCoffees = numberOfCoffees - numberOfFreeCoffees
    return numberOfPaidCoffees * pricePerCoffee

print(getCostOfCoffee2(10000000000, 2.50))
