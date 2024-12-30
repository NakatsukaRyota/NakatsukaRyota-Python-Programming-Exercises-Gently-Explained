def drawRectangle(width, height):
    if width < 1 or height < 1:
        return 
    for i in range(height):
        for j in range(width):
            print("#", end="")
        print()

