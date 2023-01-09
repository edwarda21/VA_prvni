import random

'''
Create hangman game
Number of tries = 7
Steps:
    1. Get random word * 
    2. Convert to letters * 
    3. Check input is a letter from the alphabet *
    4. Check letter is in word * 
    5. Save guessed letters 
    6. Save wrongly guessed letters * 
'''


# define functions
def create_statistic(in_guesses, in_correct_guesses, in_result, in_word):
    percentage = round(in_correct_guesses / in_guesses, 2) * 100  # creates percentage
    if in_result:
        print(f"Congratulations! You guessed the word \"{in_word}\" in just {in_guesses}. Out of your {in_guesses}"
              f" guesses you got {in_correct_guesses} correct,"
              f" that is {percentage}% !. ")
    else:
        print(f"Sorry, you lost. The word  was \"{in_word}\". Out of your {in_guesses}"
              f" guesses you got {in_correct_guesses} correct,"
              f" that is {percentage}% ! Better luck next time ")


# define variables and lists

difficulties_threshold = {"e": [0, 5], "m": [4, 8], "h": [7, 15]}  # sets the threshold for word length in each
health_values = {"e": 4, "m": 7, "h": 9}
play = True
with open("words.txt", "r") as f:
    words = f.readlines()
while play:  # creates loop to continue playing
    # get difficulty
    while True:
        difficulty = input('''What difficulty do you want to choose?
            (E)asy => Word is less than 5 letters long
            (M)edium => Word length is between 5 and 8 letters
            (H)ard => Word is 8 or more letters long\n =>''').lower().strip()
        if difficulty not in ["e", "m", "h"] or len(difficulty) == 0:
            continue
        else:
            difficulty = difficulty[0]
            while True:
                if len(difficulty) > 0:
                    # get random word based on difficulty constraints
                    word = random.choice(words).strip("\n")
                    if (difficulty[0] in ["e", "m", "h"]) and difficulties_threshold[difficulty][0] < len(word) < \
                            difficulties_threshold[difficulty][1]:
                        break
                    else:
                        continue
        break

    health = health_values[difficulty]
    word_list = ["_" for letter in word]
    guesses = 0
    correct_guesses = 0
    guessed_letters = []
    wrongly_guessed_letters = []
    # get length of word
    word_len = len(word)
    letters_to_guess = set(word)
    # give user info
    user_guess = ["_" for i in range(word_len)]
    print(f'''
    The word you are guessing is {word_len} letters long.
    You start with {health} guesses
    ''')

    while True:  # creates the individual game loop
        print("-_-" * 20)
        print("Wrong guesses: ", ",".join(wrongly_guessed_letters))
        print(f"Remaining lives: {health}")
        print("".join(word_list))  # shows player their progress throughout the word
        letter = input(f"What letter are you going to guess? => ").lower()
        # gets the guess from player and makes it lowercase, so it's easier to work with
        if len(letter) == 0 or not letter[0].isalpha():  # checks if user entered something and if it was a letter
            continue
        else:
            guesses += 1
            letter = letter[0]  # gets the first letter from users guess
            if letter not in word:  # check if it's needed to guess this letter or not
                health -= 1  # since the letter is not in the word take away a life
                if health == 0:
                    print(f" ** Sorry you lose, the word was {word} ** ")
                    create_statistic(guesses, correct_guesses, False, word) # create final statistic for game loss
                    break
                else:

                    wrongly_guessed_letters.append(letter) if letter not in wrongly_guessed_letters else False
                    # add the wrongly guessed letter to the wrongly_guessed_letters list if it is not in there already
                    print(f''' ** Sorry, {letter} is not in the word. ** ''')
            else:  # inserted letter is correct
                correct_guesses += 1
                # adds 1 to the counter of correct guesses that will be used in the final statistic
                if letter not in letters_to_guess:  # checks if the letter that was guessed was already guessed or not
                    print(" ** You have already guessed this correct letter. ** ")
                else:  # letter that was guessed correctly and was not guessed before
                    print(f" ** Yes, {letter} is in the word ** ")
                    indexes_to_remove = [i for i, x in enumerate(word) if x == letter]
                    for index in indexes_to_remove:
                        word_list[index] = letter
                    letters_to_guess.remove(letter)
            if not letters_to_guess:
                create_statistic(guesses, correct_guesses, True, word)
                break
    while True:
        keep_playing = input("Do you want to continue? Y/N \n =>" ).lower().strip()[0]
        if keep_playing == "y":
            break
        elif keep_playing == "n":
            play = False
            break
