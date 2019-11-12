def getAvailableLetters(lettersGuessed):
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for x in letters:
        if x not in lettersGuessed:
            string += x
    return string