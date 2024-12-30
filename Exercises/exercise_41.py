def rot13(text):
    result = []
    for character in text:
        if not character.isalpha():
            result.append(character)
        else:
            if character.isupper():
                asciiNum = ord(character) + 13
                if asciiNum > 90:
                    asciiNum -=  26
                result.append(chr(asciiNum))
            else:
                asciiNum = ord(character) + 13
                if asciiNum > 122:
                    asciiNum -= 26
                result.append(chr(asciiNum))
    result = "".join(result)
    return result

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'

assert rot13('Uryyb, jbeyq!') == 'Hello, world!'

assert rot13(rot13('Hello, world!')) == 'Hello, world!'

assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'

assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
