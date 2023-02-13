import functions as f
import sys

running = True
login = True
player = None
login_menu = "-"*100 + '''
        Welcome player, it seems you are not logged in. What would you like to do?
        (to choose type the number that the option is presented with or type quit to stop the program)
        1. Log in (I am a returning player)
        2. Register (I have never played before)\n'''+"-"*100
print(login_menu)
while login:
    action = input()
    match action:
        case "quit":
            sys.exit("You have quit the game")
        case "1":
            player = f.returning_player()
            login = False
        case "2":
            player = f.create_player()
            login = False
menu = "-"*100 + '''
            Hello there {player_name}, what would you like to do?
                (to choose type the number that the option is presented with or type quit to stop the program)
                1. Play game
                2. Look at the leaderboard
                3. Look at your own info\n'''+"-"*100
while running:
    print(menu.format(player_name=player.nick))
    while True:
        action = input()
        match action:
            case "quit":
                sys.exit("You have quit the game")
            case "1":
                f.game(player)
                running = True
                break
            case "2":
                f.show_leaderboard()
                running = True
                break
            case "3":
                player.write_statistic()
                running = True
                break
