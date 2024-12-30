def makeChange(amount):
    result = {}

    quarters = amount // 25
    amount -= quarters * 25
    if quarters != 0:
        result["quarters"] = quarters

    dimes = amount // 10
    amount -= dimes * 10
    if dimes != 0:
        result["dimes"] = dimes

    nickels = amount // 5
    amount -= nickels * 5
    if nickels != 0:
        result["nickels"] = nickels

    pennies = amount
    if pennies != 0:
        result["pennies"] = pennies

    return result

assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}