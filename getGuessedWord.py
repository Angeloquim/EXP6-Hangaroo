def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for x in secretWord:
        if x in lettersGuessed:
            string += x
        else:
            string += "_ "
    return string
