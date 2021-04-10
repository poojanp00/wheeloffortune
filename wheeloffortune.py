import random

def main():
    originalphrase = choosephrase()
    winnings = initialwinnings()
    consonantsguessed = consonantlist()
    vowelsguessed = vowellist()
    blanks = word(originalphrase)
    gamestart(originalphrase, winnings)
    turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)


def choosephrase():
# The following lines of code choose a random phrase
    PhraseBank = open('phrasebank.txt').read().splitlines()
    originalphrase = random.choice(PhraseBank)
    return originalphrase


def initialwinnings():
# This function returns an initial winnings starting at zero
    winnings = 0
    return winnings


def consonantlist():
# This function returns an empty list of guessed consonants
    consonantsguessed = []
    return consonantsguessed


def vowellist():
# This function returns an empty list of guessed vowels
    vowelsguessed = []
    return vowelsguessed


def word(originalphrase):
# The following lines of code replace the phrase with the respective blanks and
# spaces
    blanks = list((len(originalphrase) * "_"))
    index_word = 0
    while index_word < len(originalphrase):
        if originalphrase[index_word] == " ":
            blanks[index_word] = " "
        index_word += 1
    blanks = "".join(blanks)
    return blanks


def category(originalphrase):
# The following lines determine which category the phrase is in, based on the
# position of the phrase in the PhraseBank
    PhraseBank = open('phrasebank.txt').read().splitlines()
    if PhraseBank.index(originalphrase) in range(0,20):
        category = "Before and After"
    elif PhraseBank.index(originalphrase) in range(20,40):
        category = "Song Lyrics"
    elif PhraseBank.index(originalphrase) in range(40,60):
        category = "Around the House"
    elif PhraseBank.index(originalphrase) in range(60,80):
        category = "Food and Drink"
    elif PhraseBank.index(originalphrase) in range(80,100):
        category = "Same Name"
    return category


def gamestart(originalphrase, winnings):
    blanks = word(originalphrase)
# The following lines will print out the instructions of the game, as well as
# the blanks, category, and winnings.
    print ("Welcome to the Wheel of Fortune!")
    print ("The phrase is:")
    print (blanks)
    print("The category is: ", category(originalphrase))
    print ("Your current winnings are: ", "$", winnings)
    return originalphrase


def turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed):
# The user is prompted to enter in what they would like to do as a turn. These
# if else statements ensure that the user input is correct.
    if (len(consonantsguessed) + len(vowelsguessed)) == 26:
        lost()

    else:
        print ("Would you like to Spin the Wheel (type 'spin'), Buy A Vowel (type 'vowel'), or Solve the Puzzle (type 'solve')?")
        choice = input().lower()
        if choice == "spin":
            spinTheWheel(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)
        elif choice == "vowel":
            buyAVowel(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)
        elif choice == "solve":
            solveThePuzzle(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)
        else:
            print("Whoops, I don't recognize that input! Try again.")
            turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)


def spinTheWheel(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed):
# This function spins the wheel for the user and asks them to input a consonant
# and replaces the respective blanks with the letter. It will also update the
# users cumulative winnings.
    wheel = [50, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 250, 250, 250, 500, 500, 750, 750, 1000, 2000, 5000, 10000, "Bankrupt", "Bankrupt"]
    spin = random.choice(wheel)
    vowel = ["A","E","I","O","U"]

# This if else statement ensures the user did not spin bankrupt on the wheel. If
# the user spins a numerical value, they will guess a consonant. The while statement
# will ask the player to input again if they input an invalid entry (numbers, symbols,
# multiple letter, reguessing letter, vowels etc)
    if spin == "Bankrupt":
        print ("Uh oh, you've spun a Bankrupt!! Your Winnings will go down to $0.")
        winnings = 0
        turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)

    elif len(consonantsguessed) == 21:
        print("Whoops, You have already guessed all of the letters! Try another turn.")
        turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)


    else:
        print ("You have spun", "$", spin, "! " "Guess a consonant letter: ")
        consonantguess = input().upper()

        while consonantguess.isalpha() == False or consonantguess in vowel or len(consonantguess) != 1 or consonantguess in consonantsguessed:
            if consonantguess in consonantsguessed:
                print("Whoops, You have already guessed that! Try again.")
                consonantguess = input().upper()
            else:
                print("Whoops, I don't recognize that input! Try again.")
                consonantguess = input().upper()
        number_of_occurences = originalphrase.count(consonantguess)

# This if else statement replaces the blanks with the guessed letters. if the
# letter is incorrect, winnings are subtracted and they are returned to take a
# new turn.
        if consonantguess in originalphrase:
            currentwinnings = spin * number_of_occurences
            winnings += currentwinnings
            print("Congratulations,", consonantguess, "appears in the phrase", number_of_occurences, "time(s)! You've won $", currentwinnings)
            print("The updated phrase is: ")
            place = originalphrase.find(consonantguess)
            blanks = list(blanks)
            blanks[place] = consonantguess
            blanks1 = blanks[:place+1]
            adjphrase = originalphrase[place+1:]
            adjblanks = blanks[place+1:]
            if number_of_occurences > 1:
                count = 0
                while count < number_of_occurences-1:
                    place = adjphrase.find(consonantguess)
                    adjblanks[place] = consonantguess
                    blanks2 = adjblanks[:place+1]
                    list1 = blanks1
                    list1 += blanks2
                    adjblanks = adjblanks[place+1:]
                    adjphrase = adjphrase[place+1:]
                    count += 1

                if len(list1) != len(blanks):
                    list1 += blanks[len(list1):]
                blanks = list1
                print("".join(blanks))
                print("The category is: ", category(originalphrase))

            else:
                print("".join(blanks))
                print("The category is: ", category(originalphrase))

# If the guessed consonant is incorrect, the winnings are deducted and the current
# or latest phrase is printed to to user.
        else:
            print("Good guess, but that was incorrect. $", spin, "will be deducted from your winnings")
            print("The phrase is: ")
            print("".join(blanks))
            print("The category is: ", category(originalphrase))
            winnings -= spin

# The following lines add on to the consonantsguessed list and return the vowels
# and consonants guessed. The winnings are also returned and the player is brought
# back to take a next turn.
        consonantsguessed.append(consonantguess)
        print("Vowels guessed:", ", ".join(vowelsguessed))
        print("Consonants guessed:", ", ".join(consonantsguessed))
        print("Your current winnings are: $", winnings)
        turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)


def buyAVowel(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed):
# These lines of code ensure that the user has a winnins total of at least $250
# before buying a vowel. If the user does not have enough money, they are returned
# to the options to spin the wheel, buy a vowel, or solve the puzzle. The while
# loop ensures that the user enters a correct vowel only. If the user has guessed
# all 5 vowels, they must take a new turn.
    vowel = ["A","E","I","O","U"]
    if len(vowelsguessed) == 5:
        print("Whoops, You have already guessed all 5 vowels! Try another turn.")
        turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)

    elif winnings >= 250:
        print("Ok! $250 will be deducted from your winnings. Which vowel would you like to buy (A, E, I, O, U)?: ")
        winnings -= 250
        vowelguess = input().upper()

        while vowelguess not in vowel or len(vowelguess) != 1 or vowelguess in vowelsguessed:
            if vowelguess in vowelsguessed:
                print("Whoops, You have already guessed that! Try again.")
                vowelguess = input().upper()
            else:
                print("Sorry, that is not a vowel, please try again: ")
                vowelguess = input().upper()

# The guessed vowels list is updated here
        vowelsguessed.append(vowelguess)
        number_of_occurences = originalphrase.count(vowelguess)


# This if else statement replaces the blanks with the guessed letters. If the
# letter is incorrect, winnings are subtracted by 250 and they are returned to take a
# new turn. These are essentually similar lines of code from the spinTheWheel function.
        if vowelguess in originalphrase:
            print("Congratulations,", vowelguess, "appears in the phrase", number_of_occurences, "time(s)!")
            print("The updated phrase is: ")
            place = originalphrase.find(vowelguess)
            blanks = list(blanks)
            blanks[place] = vowelguess
            blanks1 = blanks[:place+1]
            adjphrase = originalphrase[place+1:]
            adjblanks = blanks[place+1:]
            if number_of_occurences > 1:
                count = 0
                while count < number_of_occurences-1:
                    place = adjphrase.find(vowelguess)
                    adjblanks[place] = vowelguess
                    blanks2 = adjblanks[:place+1]
                    list1 = blanks1
                    list1 += blanks2
                    adjblanks = adjblanks[place+1:]
                    adjphrase = adjphrase[place+1:]
                    count += 1

                if len(list1) != len(blanks):
                    list1 += blanks[len(list1):]
                blanks = list1
                print("".join(blanks))
                print("The category is: ", category(originalphrase))

            else:
                print("".join(blanks))
                print("The category is: ", category(originalphrase))

# If the user guesses an incorrect vowel, the winnings are deducted (done earlier in the code)
        else:
            print("Good guess, but that was incorrect. $ 250 will be deducted from your winnings")
            print("The phrase is: ")
            print("".join(blanks))
            print("The category is: ", category(originalphrase))


    else:
        print("Sorry, a vowel costs $250, you do not have enough money to buy a vowel!")
        turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)

# The following lines return the updated vowels and consonants guessed.
# The winnings are also returned and the player is brought back to take a next turn.
    print("Vowels guessed:", ", ".join(vowelsguessed))
    print("Consonants guessed:", ", ".join(consonantsguessed) )
    print("Your current winnings are: $", winnings)
    turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)


def solveThePuzzle(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed):
# This if else statement will check if the guess is equivilant compared to the
# original phrase. If the user guesses correctly, they are congratulated and informed
# about their winnings. If they have a negative balance, the winnings are returned as
# $0. If the guess is incorrect, winnings are reset and they are asked to take another
# turn.
    if winnings < 0:
        winnings = 0
    print("what is your best guess (be sure to enter your guess with single space!)?: ")
    solveguess = input()
    if solveguess.upper() == originalphrase:
        print("That's correct!!! You have solved the puzzle! :p")
        print("Congratulations, you've won the game! Your winnings are $", winnings, ". Thank you for playing the Wheel of Fortune!")

    else:
        print("Sorry, that guess is incorrect! Your winnings will start over at $0. :(")
        winnings = 0
        turn(originalphrase, winnings, blanks, vowelsguessed, consonantsguessed)

def lost():
    print("You have guessed all 26 letters! Your winnings are $0. You have lost the game :(")
    print("Thank you for playing the Wheel of Fortune")


if __name__ == '__main__':
    main()
