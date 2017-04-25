def alphabet_position(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        alphaplace = ord(letter) - 65
        return alphaplace
    elif ord(letter) >= 97 and ord(letter) <= 122:
        alphaplace = ord(letter) - 97
        return alphaplace

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    isUpper = 0
    if ord(char) >= 65 and ord(char) <= 90:
        isUpper = 1
    newLetterPos = (alphabet_position(char)) + rot
    newLetterPos = newLetterPos % 26
    if isUpper == 1:
        newLetterPos = newLetterPos + 65
        newLetter = chr(newLetterPos)
    else:
        newLetterPos = newLetterPos + 97
        newLetter = chr(newLetterPos)
    return newLetter

def encrypt(text,rot):
    newText = ""
    for char in text:
        newText = newText + rotate_character(char, rot)

    return newText
