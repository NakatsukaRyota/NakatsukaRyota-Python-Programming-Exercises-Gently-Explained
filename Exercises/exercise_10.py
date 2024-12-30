def findAndReplace(text, oldText, newText):
    for i in range(len(text)):
        if text[i] == oldText[0]:
            if text[i : i + len(oldText)] == oldText:
                text = text[:i] + newText + text[i + len(oldText):]

    return text

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'