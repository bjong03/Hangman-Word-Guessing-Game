# Hangman-Word-Guessing-Game

This application is a version of the Hangman word guessing game, where a player must guess the secret word within a limited amount of guesses. I used Python and a words.txt file to create this game. The rules to the game are as follows:
1. The user starts off with 6 guesses and 3 warnings.
2. The user loses a warning if they perform any of the following actions:
    - Enters anything besides an alphabet
    - Enters more than one alphabet/character at a time
    - Enters a letter that has already been guessed
3. If the user runs out of warnings, they will lose one guess in lieu of warnings
4. If the user inputs a letter that has not been guessed before and the letter is in the secret word, the user does not lose any guesses.
5. If the user inputs a consonant that has not been guesssed and the consonant is not in the secret word, the user loses one guess.
6. If the user inputs a vowel (a, e, i, o, u) that has not been guessed and the vowel is not in the secret word, the user loses two guesses.
7. The game terminates either when the secret word is guessed or the user runs out of guesses.
8. The final score is calculated by the product of the number of unique letters in the secret word and the number of guesses remaining.
