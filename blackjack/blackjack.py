from pprint import pprint
import functions as f
import keyboard
import sys

login_menu = '''
        Welcome player, it seems you are not logged in. What would you like to do?
        (to choose press the number that the option is presented with or press escape to stop the program)
        1. Log in (I am a returning player)
        2. Register (I have never played before)'''
print(login_menu)
while True:
    key = keyboard.read_key()
    if key == "esc":
        sys.exit("You have quit the game")
    elif key == "1":
        player = f.returning_player()
        break
    elif key == "2":
        player = f.create_player()
        break
    else:
        continue
menu = '''
        Hello there {player_name}, what would you like to do?
            (to choose press the number that the option is presented with or press escape to stop the program)
            1. Play game
            2. Look at the leaderboard
            3. Look at your own info
        '''
print(menu.format(player_name = player.nick))
while True:
    key = keyboard.read_key()
    match key:
        case "esc":
            sys.exit("You have quit the game")
        case "1":
            f.game(player)
            break
        case "2":
            f.show_leaderboard()
            break
        case "3":
            player.write_statistic()
            break

# while True:
#     play = input("Do you want to play again? (Y)es or (N)o.")
#     if len(play) == 0 or play.lower() not in ["y", "n"]:
#         game = False
