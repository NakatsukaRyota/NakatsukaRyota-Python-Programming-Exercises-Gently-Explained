def getUppercase(text):
    CHAR_TO_UPPER_CASE = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H",
                            "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n":"N", "o": "O", 
                            "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w":"W", "x": "X", "y": "Y", "z": "Z"}

    result = ""
    for char in text:
        if char in CHAR_TO_UPPER_CASE:
            result = result + CHAR_TO_UPPER_CASE[char]
        else:
            result = result + char

    return result

assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''