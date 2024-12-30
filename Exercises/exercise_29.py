def drawPyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i), "#" * ((i * 2) - 1))

drawPyramid(20)