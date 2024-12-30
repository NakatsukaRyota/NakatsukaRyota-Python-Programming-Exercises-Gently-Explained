def reverseString(text):
    text = list(text)
    listLength = len(text)
    
    for i in range(listLength // 2):
            temp = text[i]
            text[i] = text[- (i + 1)]
            text[- (i + 1)] = temp

    text = "".join(text)
    return text

assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'