import random
import re
import json


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
    def __init__(self, nick):
        self.hand = []
        self.count = 0
        self.blackjack = False
        self.bust = False
        self.nick = nick
        self._bet = None
        self.bet_multiplier = 1
        self.tokens = 0

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

    def double_down(self, in_deck):
        if self.bet is None:
            return False
        else:
            self.bet *= 2
            return False if self.bust else True

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, bet):
        if bet < 5 or not isinstance(bet, int):
            raise ValueError("You may not bet less than 5$")
        else:
            self._bet = bet


def create_player(player_list):
    while True:
        in_name = input(
            '''Well hello player, what will your nickname be? (at least 3 characters long with at least 1 character) \n =>''')
        if len(in_name) >= 3 and not in_name.isspace() and " " not in in_name and re.search('[a-zA-Z]', in_name):
            if check_player_exists(in_name,player_list):
                print("Sorry, this username is already taken, try choosing something else.")
            else:
                print(f"That is a great username, welcome {in_name}.")
                break
        else:
            print("Sorry, your username has to be at least 3 characters long and must not include whitespace")

    player = Player(in_name)
    add_player(player,player_list)
    return Player



def get_players(file):
    with open(file) as f:
        content = f.read()

        return json.loads(content) if len(content) > 0 else {}


def write_to_json(file, content):
    content = json.dumps(content)
    with open(file, "w+") as f:
        return f.write(content)


def add_player(in_player, player_list):
    if in_player.nick in player_list:
        print("Sorry, cant add your player, this nick is already taken")
        return False
    else:
        player_list[in_player.nick] = {"tokens": 5,"won":0,"lost":0}
        return True
    # creates a new player to the list

def check_player_exists(name,player_list):
    if name in player_list:
        return True
    return False
    # checks if a player exists by seeing if there is a key in the players.json



