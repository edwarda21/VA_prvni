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
health = 7
difficulties_threshold = {"e":5,"m":8} # sets the threshold for word length in each difficulty
with open("words.txt", "r") as f:
    words = f.readlines()
while True:
    difficulty = input('''What difficulty do you want to choose?
        (E)asy => Word is less than 5 letters long
        (M)edium => Word length is between 5 and 8 letters
        (H)ard => Word is 8 or more letters long''').lower()
    while True:
        if len(difficulty) > 0:
            word = random.choice(words).strip("\n")
            if (difficulty[0] == "e" or difficulty[0] == "m") and len(word) < difficulties_threshold[difficulty]:
                print(len(word) < difficulties_threshold[difficulty])
                break
            elif difficulty[0] == "h" and len(word) >= 8:
                break
            else:
                continue
    break

print(word)
word_list = ["_" for letter in word]
print(word_list)
play = True
# get length of word
word_len = len(word)
letters_to_guess = set(word)
# give user info
user_guess = ["_" for i in range(word_len)]
print (f'''
The word you are guessing is {word_len} letters long.
{''.join(user_guess)}
''')
while True: # creates the game loop
    print(word_list)
    print("".join(word_list)) # shows player their progress throughout the word
    letter = input(f"What letter are you going to guess? => ").lower() # gets the guess from player and makes it lowercase so its easier to work with
    if len(letter) == 0 or not letter[0].isalpha(): # checks if user entered something and if it was a letter
        continue
    else:
        letter = letter[0] # gets the first letter from users guess
        if letter not in letters_to_guess: # check if it's needed to guess this letter or not
            health -= 1 # since the letter is not in the word take away a life
            if health == 0:
                print(f"Sorry you lose, the word was {word}")
                break
            elif letter in wrongly_guessed_letters:
                print(f'''You already guessed {letter} and it is still wrong!
                You have {health} tries remaining''')
            else:
                wrongly_guessed_letters.append(letter)
                print(f'''Sorry, {letter} is not in the word.
                You have {health} tries remaining''')
        else:
            print(f"Yes, {letter} is in the word")
            indexes_to_remove = [i for i, x in enumerate(word) if x == letter]
            for index in indexes_to_remove:
                word_list[index] = letter
            letters_to_guess.remove(letter)
        if not letters_to_guess:
            print(f"Congratulations! You have guessed the word {word} with just {health} tries left")
            break



