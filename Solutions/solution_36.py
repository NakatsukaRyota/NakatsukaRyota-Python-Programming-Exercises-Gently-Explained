def reverseString(text):
    text = list(text)

    for i in range(len(text) // 2):
        mirrorIndex = len(text) - 1 - i
        text[i], text[mirrorIndex] = text[mirrorIndex], text[i]

    return "".join(text)