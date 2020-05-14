import random
from words import word_list


def get_word():  # get words from the word file for the game
    word = random.choice(word_list)  # choose words randomly from word_list
    return word.upper()  # make all user input to upper case to make comparison easier


def play(word):  # get the word from the word list
    word_completion = "_" * len(word)  # Words that is chosen will be showed in underscore
    guessed = False
    guessed_letters = []  # hold the letters user guessed
    guessed_words = []  # hold the words user guessed
    tries = 6  # How many tries user will have
    print("Let's play Hangman!")
    print(display_hangman(tries))  # display the hangman
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:  # this will run till the word is guessed or the user ran out of tries
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():  # guess has a length of 1 and contains only characters from the alphabet so we call it is alpha on guess
            if guess in guessed_letters:  # if user input the same letter again
                print("You already guessed the letter", guess)
            elif guess not in word:  # if user input the wrong letter
                print(guess, "is not in the word.")
                tries -= 1  # decrease the tries of the words
                guessed_letters.append(guess)  # add the input to the guessed_letters
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)  # add the input to the guessed_letters
                word_as_list = list(word_completion)  # make word-complete as a list
                indices = [i for i, letter in enumerate(word) if letter == guess]  # user input same as the word
                for index in indices:
                    word_as_list[index] = guess  # replace each underscore as guess
                word_completion = "".join(word_as_list)  # converting back to string
                if "_" not in word_completion:  # if the word is already guessed
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # guessing a word would mean that the length of guests equals the length of the actual word
            if guess in guessed_words:  # if user guess that word previously
                print("You already guessed the word", guess)
            elif guess != word:  # if input does not exist in word list
                print(guess, "is not the word.")
                tries -= 1  # decrease every time user give incorrect letter
                guessed_words.append(guess)  # add them to the guessed_word
            else:
                guessed = True  # user input is correct
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))  # display the hangman
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):  # the display of hangman
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":  # if user wants to play again
        word = get_word()
        play(word)


if __name__ == "__main__":  # for running this code in cmd
    main()