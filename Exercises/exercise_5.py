def FizzBuzz(upTo):
    for i in range(upTo):
        num = i + 1
        
        if num % 15 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")

FizzBuzz(35)