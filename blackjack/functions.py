import random
import re
import json
from pprint import pprint

import keyboard

PLAYERS_FILE = "players.json"
LEADERBOARD_FILE = "leaderboard.json"
STARTING_TOKENS = 20
BASE_TOKENS = 12


def get_decks(in_number_of_decks):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["♥", "♣", "♠", "♦"]
    out_deck = []
    for decks in range(0, in_number_of_decks):
        out_deck += [{"value": value, "colour": colour, "type": "soft"} for value in values for colour in colours]
    random.shuffle(out_deck)
    return out_deck


def find_ace(in_hand):
    for card in in_hand:
        if card["value"] == "A" and card["type"] == "soft":
            card["type"] = "hard"
            return True
    return False


def write_hand(in_hand):
    for card in in_hand:
        continue


class Player:
    def __init__(self, nick, tokens=STARTING_TOKENS, won=0, lost=0, max_tokens=STARTING_TOKENS):
        self.hand = []
        self.count = 0
        self.blackjack = False
        self.bust = False
        self.nick = nick
        self._bet = None
        self.bet_multiplier = 1
        self.max_tokens = max_tokens
        self._tokens = tokens
        self.won = won
        self.lost = lost

    def get_hand(self, in_deck):
        for x in range(0, 2):
            self.draw_card(in_deck)

    def draw_card(self, in_deck):
        card = in_deck.pop()
        try:
            self.count += int(card["value"])
        except ValueError:
            if card["value"] in ["J", "Q", "K"]:
                self.count += 10
            elif self.count + 11 > 21:
                self.count += 1
                card["type"] = "hard"
            else:
                self.count += 11
        finally:
            self.hand.append(card)
            if self.count > 21:
                if find_ace(self.hand):
                    self.count -= 10
                    return True
                else:
                    self.bust = True
                    return False
            else:
                return True

        # gets the value of drawn card, if the value is not a number then value is assigned manually, hence try except
        # finally clause there to always check the value of the persons hand see if they are bust or not

    def check_blackjack(self):
        if self.count == 21 and len(self.hand) == 2:
            self.blackjack = True
            self.bet_multiplier = 1.5
            return True

    def double_down(self):
        if self.bet is None:
            return False
        else:
            self.bet *= 2
            return False if self.bust else True

    def save_info(self):
        list_of_players = get_json(PLAYERS_FILE)
        current_player = list_of_players[self.nick]
        current_player["tokens"] = self.tokens
        current_player["won"] = self.won
        current_player["lost"] = self.lost
        if self.tokens > current_player["max"]:
            current_player["max"] = self.tokens
            self.max_tokens = self.tokens
        write_to_json(PLAYERS_FILE, list_of_players)

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, bet):
        if bet < 1 or not isinstance(bet, int):
            raise ValueError("You may not bet less than 1$")
        else:
            self._bet = bet

    def write_statistic(self):
        output = '''
    |'''+ "-" * 30+ '''
    | Nickname: {nick}
    | Amount of tokens: {tokens}
    | Games won: {won}
    | Games lost: {lost}
    | All time most tokens: {max_tokens}
    |'''+"-" * 30
        print(output.format(nick=self.nick,tokens=self.tokens,won=self.won,lost=self.lost,max_tokens=self.max_tokens))
    @property
    def tokens(self):
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        if tokens >= self.max_tokens:
            self.max_tokens = tokens
            update_leaderboard(self)
        self._tokens = tokens


def create_player():
    player_list = get_json(PLAYERS_FILE) or {}
    while True:
        in_name = input(
            '''Well hello player, what will your nickname be? (at least 3 characters long with at least 1 letter)
            \n =>''')
        if len(in_name) >= 3 and not in_name.isspace() and " " not in in_name and re.search('[a-zA-Z]', in_name):
            if check_player_exists(in_name, player_list):
                print("Sorry, this username is already taken, try choosing something else.")
            else:
                print(f"That is a great username!\n")
                break
        else:
            print("Sorry, your username has to be at least 3 characters long and must not include whitespace")
    # runs a loop until the player puts in a valid username that can be saved
    out_player = Player(in_name)
    print(
        f"Welcome {out_player.nick}! Glad to have you onboard. We have given you {STARTING_TOKENS} tokens as a "
        f"welcome gift.")
    player_list[out_player.nick] = {"tokens": STARTING_TOKENS, "won": 0, "lost": 0, "max": STARTING_TOKENS}
    update_leaderboard(out_player)
    write_to_json(PLAYERS_FILE, player_list)
    return out_player
    # creates a new player instance and automatically saves it to the players file


def get_json(file):
    with open(file) as f:
        content = f.read()
        return json.loads(content) if len(content) > 0 else False
    # return data from the given JSON file


def write_to_json(file, content):
    content = json.dumps(content)
    with open(file, "w+") as f:
        return f.write(content)
    # rewrites the players.json file with new or updated content


def check_player_exists(name, player_list):
    if name in player_list:
        return True
    return False
    # checks if a player exists by seeing if there is a key in the players.json


def returning_player():
    keyboard.unhook_all_hotkeys()
    file_data = get_json(PLAYERS_FILE)
    player_list = [] if not file_data else file_data
    while True:
        in_name = input(
            '''Please tell us what your nick is, player. 
            \n =>''')

        if in_name in player_list:
            print(f"Welcome back {in_name}!")
            return Player(in_name, player_list[in_name]["tokens"], player_list[in_name]["won"],
                          player_list[in_name]["lost"],
                          player_list[in_name]["max"])
        else:
            print("Sorry, there is no player with this nick")
    # checks if the inputted name is from a returning player or not, if not then asks for the nick again


def update_leaderboard(player):
    leaderboard = get_json(LEADERBOARD_FILE) or []
    player_info = {"name":player.nick,"tokens":player.max_tokens}
    if len(leaderboard) == 0:
        leaderboard.append({"name": player.nick, "tokens": player.max_tokens})
        write_to_json(LEADERBOARD_FILE, leaderboard)
        return
    for i, v in enumerate(leaderboard):

        if v["name"] == player.nick:
            player_info = leaderboard.pop(i)
            player_info["tokens"] = player.max_tokens
            break
    # retrieve players information in the leaderboard and remove from leaderboard array to insert at the correct space
    print("Leaderboard")
    print(leaderboard)
    for index, v in [[i, v] for i, v in enumerate(leaderboard)]:
        if v["tokens"] < player.max_tokens:
            leaderboard.insert(index, player_info)
            break
        elif index == len(leaderboard) - 1:
            leaderboard.insert(index + 1, player_info)
        else:
            continue
    print("RUN")
    print(leaderboard)
    write_to_json(LEADERBOARD_FILE, leaderboard)


def game(player, no_of_decks=6):
    deck = get_decks(no_of_decks)
    dealer = Player("dealer")
    player_turn = True
    dealer_turn = True
    # deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
    # int("J") test line to check what error to check for in except clause
    # TODO: create a main gameloop
    # TODO: put game into a function
    # TODO: create menu
    # TODO: add keyboard listeners to menu
    dealer.draw_card(deck)
    player.get_hand(deck)
    pprint(f"The dealers card is {dealer.hand}")
    # starts players turn
    while player_turn:
        player_decision = True
        player_action = None
        # gives player info on their hand
        print(f"The value of your hand is {player.count}")
        print("Your cards are:")
        double_down = "or (D)ouble down" if len(player.hand) == 2 else ""
        pprint(player.hand)
        # check for player blackjack
        if player.check_blackjack():
            print("BLACKJACK! You now have a great chance of winning")
            player_turn = False
            continue
        # get player action
        while player_decision:
            player_action = input(f"Do you want to (H)it, (S)tand {double_down}?\n =>")
            if len(player_action) > 0 and player_action.lower()[0] in ["h", "s", "d" if double_down else None]:
                player_decision = False
        # evaluate player actions
        if player_action == "s":
            player_turn = False
            continue
        elif player_action == "d":
            if not player.double_down(deck):
                print(
                    f"You have gone bust on your double down card, the card you drew was a {player.hand[-1]['value']}")
            else:
                print(f"Your double down card is a {player.hand[-1]['value']}")
            player_turn = False
            continue
        if not player.draw_card(deck):
            print(f"You have gone bust, the card you last drew was a {player.hand[-1]['value']}")
            player_turn = False
            continue

    print(f"final player hand is {player.hand}")
    dealer.draw_card(deck)
    while dealer_turn:
        # dealers game
        # check dealer blackjack
        if dealer.check_blackjack():
            print("The dealer got a blackjack!")
            dealer_turn = False
            continue
        # if dealer has count less than 17 they draw a card
        if dealer.count <= 16:
            if not dealer.draw_card(deck):
                print(f"The dealer has gone bust their final hand is {dealer.hand}")
                dealer_turn = False
                continue
        else:
            print(f"The dealers final hand is {dealer.hand}")
            print(f"The dealers final hand value is {dealer.count}")
            dealer_turn = False
            continue
    # evaluate result and ask to play again
    # check for either person bust
    if player.bust:
        print("You have lost the game.")
        player.lost += 1
    elif dealer.bust:
        print("Congratulations! You win.")
        player.won += 1

    # checks for draw or win on blackjack
    elif dealer.count == 21 == player.count:
        if player.blackjack and not dealer.blackjack:
            print("Congratulations! You win the game with a blackjack.")
            player.won += 1
        elif dealer.blackjack and not player.blackjack:
            print("You have lost the game.")
            player.lost += 1
        else:
            print("Unlucky, the game ended in a draw.")

    # evaluates rest of options
    elif player.count > dealer.count:
        print("Congratulations! You win.")
        player.won += 1
    elif player.count == dealer.count:
        print("Unlucky, the game ended in a draw.")
    else:
        print("You have lost the game.")
        player.lost += 1
    # save info of player (saves to files)
    player.save_info()

def show_leaderboard():
    leaderboard = get_json(LEADERBOARD_FILE) or []
    output = "-" * 50 + "\n"
    for i,v in [[i,v] for i,v in enumerate(leaderboard)]:
        output += f"{i}. {v['name']}"+" "*(40-len(v["name"]))+str(v["tokens"])+"\n"
    output += "-" * 50
    print(output)
