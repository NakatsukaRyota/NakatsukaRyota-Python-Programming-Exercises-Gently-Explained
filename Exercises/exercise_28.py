def drawBorder(width, height):
    if width < 2 or height < 2:
        return
    
    for row in range(height):
        if row == 0 or row == height - 1:
            print("+", end="")
            for column in range(width - 2):
                print("-", end="")
            print("+")
        else:
            print("|", end="")
            for column in range(width - 2):
                print(" ", end="")
            print("|")

drawBorder(2,2)
