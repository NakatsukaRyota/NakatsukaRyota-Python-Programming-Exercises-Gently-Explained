def getTitleCase(text):
    isAlpha = False
    result = ""
    for character in text:
        if not isAlpha:
            result = result + character.upper()
        else:
            result = result + character.lower()
        isAlpha = character.isalpha()

    return result

import random

random.seed(42)

chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')

for i in range(1000):

    random.shuffle(chars)

    assert getTitleCase(''.join(chars)) == ''.join(chars).title()