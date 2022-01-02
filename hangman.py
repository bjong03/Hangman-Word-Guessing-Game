import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Purpose: Load words from words.txt file
    Return: List of valid words. Words are strings of lowercase letters.  
    Note: This function may take a while to finish depending on the size of the word list.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    Purpose: Choose a random word from the wordlist
    Parameter: wordlist - list of words (strings)  
    Return: Random word from wordlist
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    Purpose: Determines whether the secret word has been guessed or not
    Parameter: secret_word - String, the word the user is guessing; assumes all letters are lowercase
    Parameter: letters_guessed - List (of letters), which letters have been guessed so far; assumes that all letters are lowercase
    Return: Boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    """
    num = 0
    list(secret_word)
    for char in secret_word:
        if char in letters_guessed:
            num += 1
    if num == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    Purpose: Displays the position of correctly guessed letters in the secret word
    Parameter: secret_word - String, the word the user is guessing
    Parameter: letters_guessed - List (of letters), which letters have been guessed so far
    Return: String, comprised of letters, underscores (_), and spaces that represents which letters in secret_word have been guessed so far.
    """
    list(secret_word)
    current_guess = ""
    for char in secret_word:
        if char in letters_guessed:
            current_guess = current_guess + char + " "
        else: 
            current_guess = current_guess + "_ "
    return current_guess


def get_available_letters(letters_guessed):
    """
    Purpose: Keep track of all the letters that have not been guessed yet
    Parameter: letters_guessed - List (of letters), which letters have been guessed so far
    Return: String (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    available_letters = string.ascii_lowercase
    available_letters = list(available_letters)
    for char in letters_guessed:
        if char in available_letters:
            available_letters.remove(char)
    available_letters = ''.join(available_letters)
    return available_letters

def score_calculator(secret_word, guesses):
    """
    Purpose: Calculates the score obtained by the user using the formula: guesses remaining * number of unique letters in secret word
    Parameter: secret_word - String, the word the user is guessing
    Parameter: guesses - Integer, the number of guesses the user has remaining at the end of the game
    Return: Integer, the score the player obtained for the game
    """
    letter_counter = 0
    letter_bank = [""]
    for char in secret_word:
        if char not in letter_bank:
            letter_bank.append(char)
            letter_counter += 1
    score = letter_counter * guesses
    return score
        

def hangman(secret_word):
    """
    Purpose: Runs the hangman word guessing game when this function is called
    Parameter: secret_word - String, the word the user is guessing
    """
    guesses = 6
    warnings = 3
    round_number = 0
    answer = False
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    letters_guessed = [""]
    while answer == False:
        if guesses > 0:
            round_number += 1
            print("************************************")
            print("Round", round_number)
            print("Guesses Remaining:", guesses)
            print("Warnings Remaining:", warnings)
            print("Available Letters:", get_available_letters(letters_guessed))
            user_input = str(input("Please guess a letter: "))
            # Converts uppercase guesses to lowercase
            user_input = user_input.lower()
            if len(user_input) > 1:
                print("You have entered too many letters. Please try again.")
                if warnings == 0:
                    guesses -= 1
                else:
                    warnings -= 1
            elif user_input not in string.ascii_lowercase:
                print("This character is not valid. Please try again.")
                if warnings == 0:
                    guesses -= 1
                else:
                    warnings -= 1
            elif user_input == 1:
                print(get_available_letters(letters_guessed))
            elif user_input in letters_guessed:
                if warnings == 0:
                    guesses -= 1
                else:
                    warnings -= 1
                print("Oops! That letter has already been guessed.")
            elif user_input not in letters_guessed and user_input not in secret_word:
                letters_guessed.append(user_input)
                print("That letter is not in the word:", get_guessed_word(secret_word, letters_guessed))
                if user_input in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
            else:
                letters_guessed.append(user_input)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                answer = is_word_guessed(secret_word, letters_guessed)
        else:
            print("************************************")
            print("Sorry, you ran out of guesses. The word is:",secret_word)
            break
    if answer == True:
        print("************************************")
        print("Congratulations, you won the game! Your score is:", score_calculator(secret_word, guesses))

hangman(choose_word(wordlist))