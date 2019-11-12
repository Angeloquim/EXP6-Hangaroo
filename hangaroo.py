def isWordGuessed(secretWord, lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            return False
        
def getGuessedWord(secretWord, lettersGuessed):
    word = ''
    for x in secretWord:
        if x in lettersGuessed:
            word += x
        else:
            word += '_ '
    return word

def getAvailableLetters(lettersGuessed):
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for x in letters:
        if x not in lettersGuessed:
            string += x
    return string

secretWord = "apple"

def hangaroo(secretWord):
    print ("Welcome to the game, Hangaroo!")
print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
lettersGuessed = ''
guessesLeft = 8
print ("------------")
while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Oops! Not part of the word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        if guess == secretWord:
            print ("Congratulations! You've won!")
            break