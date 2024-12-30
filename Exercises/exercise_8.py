def writeToFile(filename, text):
    with open(filename, mode="w") as f: # or W
        f.write(text)

def appendToFile(filename, text):
    with open(filename, mode="a") as f:
        f.write(text)

def readFromFile(filename):
    with open(filename, mode="r") as f:
        text = f.read()
        return text

writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'