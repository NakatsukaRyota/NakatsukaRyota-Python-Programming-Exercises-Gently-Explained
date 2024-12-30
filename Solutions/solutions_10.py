def findAndReplace(text, oldText, newText):
    replacedText = ""
    i = 0
    while i < len(text):
        if text[i : i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText)
        else:
            replaceText += text[i]
            i += 1
    return replacedText