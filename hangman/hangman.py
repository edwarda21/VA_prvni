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
# define variables and lists
guessed_letters = []
wrongly_guessed_letters = []
difficulties_threshold = {"e": [0, 5], "m": [4, 8], "h": [7, 15]}  # sets the threshold for word length in each
health_values = {"e": 4, "m": 7, "h": 9}
with open("words.txt", "r") as f:
    words = f.readlines()
# TODO: create loop for multiple games
while True:
    difficulty = input('''What difficulty do you want to choose?
        (E)asy => Word is less than 5 letters long
        (M)edium => Word length is between 5 and 8 letters
        (H)ard => Word is 8 or more letters long\n =>''').lower().strip()
    if difficulty not in ["e", "m", "h"]:
        continue
    else:
        while True:
            if len(difficulty) > 0:
                word = random.choice(words).strip("\n")
                if (difficulty[0] in ["e", "m", "h"]) and difficulties_threshold[difficulty][0] < len(word) < \
                        difficulties_threshold[difficulty][1]:
                    break
                elif difficulty[0] == "h" and len(word) >= 8:
                    break
                else:
                    continue
    break

health = health_values[difficulty]
word_list = ["_" for letter in word]
play = True
# get length of word
word_len = len(word)
letters_to_guess = set(word)
# give user info
user_guess = ["_" for i in range(word_len)]
print(f'''
The word you are guessing is {word_len} letters long.
You start with {health} guesses
''')
# TODO: optimize and reduce reduntant code
while True:  # creates the game loop
    print("Wrong guesses: ", ",".join(wrongly_guessed_letters))
    print("".join(word_list))  # shows player their progress throughout the word
    letter = input(f"What letter are you going to guess? => ").lower()
    # gets the guess from player and makes it lowercase so its easier to work with
    if len(letter) == 0 or not letter[0].isalpha():  # checks if user entered something and if it was a letter
        continue
    else:
        letter = letter[0]  # gets the first letter from users guess
        if letter not in word:  # check if it's needed to guess this letter or not
            health -= 1  # since the letter is not in the word take away a life
            if health == 0:
                print(f"Sorry you lose, the word was {word}")
                break
            else:
                wrongly_guessed_letters.append(letter)
                print(f'''Sorry, {letter} is not in the word.
                You have {health} tries remaining''')
        else:
            if letter not in letters_to_guess:
                print("You have already guessed this correct letter.")
            else:
                print(f"Yes, {letter} is in the word")
                indexes_to_remove = [i for i, x in enumerate(word) if x == letter]
                for index in indexes_to_remove:
                    word_list[index] = letter
                letters_to_guess.remove(letter)
        if not letters_to_guess:
            print(f"Congratulations! You have guessed the word \"{word}\" with just {health} tries left")
            break
