def bottlesOfBeer():
    for i in range(99, 1, -1):
        print(f"{i} bottles of beer on the wall,\n")
        print(f"{i} bottles of beer,\n")
        print("Take one down,\n")
        print("Pass it around,\n")
        if i == 2:
            print("1 bottle of beer on the wall,\n")
        else:
            print(f"{i - 1} bottles of beer on the wall,\n")

    print("1 bottle of beer on the wall,\n")
    print("1 bottle of beer,\n")
    print("Take one down,\n")
    print("Pass it around,\n")
    print("No more bottles of beer on the wall!\n")
    

bottlesOfBeer()