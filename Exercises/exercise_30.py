def drawBox(size):
    if size < 1:
        return 
    print(" " * (size + 1) + "+" + "-" * (size * 2) + "+")
    for i in range(size):
        print(" " * (size - i) + "/" + " " * (size * 2) + "/" + " " * i + "|")
    print("+" + "-" * (size * 2) + "+" + " " * size + "+")
    for i in range(size):
        print("|" + " " * (size * 2) + "|" + " " * (size - 1 - i) + "/")
    print("+" + "-" * (size * 2) + "+" + " " * size)

for i in range(0, 6):
    drawBox(i) 
    print() 