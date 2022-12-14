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
play = True # creates the game loop
words = [
    "cat",
    "hungover",
    "apple",
    "horse",
    "configure",
    "automate",
    "capitalize"
]
word = list(random.choice(words))
word_list = [letter for letter in word]
print(word_list)
# get length of word
word_len = len(word)
letters_to_guess = set(word)
# give user info
user_guess = ["_" for i in range(word_len)]
print (f'''
The word you are guessing is {word_len} letters long.
{''.join(user_guess)}
''')
while play:
    letter = input(f"What letter are you going to guess? => ").lower()
    if len(letter) == 0 or not letter[0].isalpha():
        continue
    else:
        letter = letter[0]
        if letter not in letters_to_guess:
            health -= 1
            if letter in wrongly_guessed_letters:
                print(f'''You already guessed {letter} and it is still wrong!
                You have {health} tries remaining''')
            else:
                wrongly_guessed_letters.append(letter)
                print(f'''Sorry, {letter} is not in the word.
                You have {health} tries remaining''')
        else:
            for letter in word:
                print(letter)


