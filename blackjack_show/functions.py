import random
import re
import json

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
        # creates deck
    random.shuffle(out_deck)
    return out_deck


def find_ace(in_hand):
    for card in in_hand:
        if card["value"] == "A" and card["type"] == "soft":  # check if the card is an ace and has not been changed yet
            card["type"] = "hard"
            return True
    return False


def write_hand(player):
    # writes out the hand of the player
    output = f"{player.nick}s hand:\n"
    output += "-" * 30 + "\n"
    for card in player.hand:
        output += f"\t{card['value']} of {card['colour']} \n"
    output += "-" * 30 + "\n"
    return output


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
        # removes top card from deck
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
        finally:  # evaluates if player lost or not
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
        # checks if the player got a blackjack (2 cards with sum value of 21)
        if self.count == 21 and len(self.hand) == 2:
            self.blackjack = True
            self.bet_multiplier = 1.5
            return True

    def double_down(self, in_deck):
        # draws a card, if bust then lost else true and continues on
        if self.bet is None:
            return False
        else:
            self.bet_multiplier = 2
            self.draw_card(in_deck)
            return False if self.bust else True

    def save_info(self):
        # saves player info to the players.json file, if the amount of current tokens succeeds the number or maximum
        # tokens then leaderboard is updated
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
        if isinstance(bet, str) and not bet.isdigit():
            raise ValueError("Bet must be of positive integer value eg. 50")
        elif int(bet) < 1:
            raise ValueError("You cannot bet less than 1 token")
        elif int(bet) > self.tokens:
            raise ValueError(f"You cannot bet more than what you have. You have {self.tokens} tokens")
        else:
            self._bet = int(bet)
        # sets the bet to what the person set, or it raises a value error with the given message

    def write_statistic(self):
        # prints out the information about the current user
        output = '''
    |''' + "-" * 30 + '''
    | Nickname: {nick}
    | Amount of tokens: {tokens}
    | Games won: {won}
    | Games lost: {lost}
    | All time most tokens: {max_tokens}
    |''' + "-" * 30
        print(
            output.format(nick=self.nick, tokens=self.tokens, won=self.won, lost=self.lost, max_tokens=self.max_tokens))

    @property
    def tokens(self):
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        # sets the tokens of player, if more than max tokens updates the leaderboard
        if tokens >= self.max_tokens:
            self.max_tokens = tokens
            update_leaderboard(self)
        self._tokens = tokens


def create_player():
    # gets list of player, if empty sets to a default empty dictionary
    player_list = get_json(PLAYERS_FILE) or {}
    while True:
        # gets player input and checks if nick is a viable option
        in_name = input(
            '''Well hello player, what will your nickname be? (at least 3 characters long with at least 1 letter)
            \n =>''')
        if len(in_name) >= 3 and not in_name.isspace() and " " not in in_name and not re.fullmatch('[^a-zA-Z0-9_-]', in_name):
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
    try:
        with open(file) as f:
            content = f.read()
            try:
                output = json.loads(content) if len(content) > 0 else False
                return output
            except json.decoder.JSONDecodeError:
                raise IOError("There is a problem with the files. Please fix me")
    except FileNotFoundError:
        return False
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
    # retrieves data from file and sets a template for the player info
    leaderboard = get_json(LEADERBOARD_FILE) or []
    player_info = {"name": player.nick, "tokens": player.max_tokens}
    # if there is nothing in the leaderboard automatically inserts in
    if len(leaderboard) == 0:
        leaderboard.append({"name": player.nick, "tokens": player.max_tokens})
        write_to_json(LEADERBOARD_FILE, leaderboard)
        return
    # finds player information and temporarily removes it from the leaderboard
    for i, v in enumerate(leaderboard):
        if v["name"] == player.nick:
            player_info = leaderboard.pop(i)
            player_info["tokens"] = player.max_tokens
            break
    # retrieve players information in the leaderboard and remove from leaderboard array to insert at the correct space
    for index, v in [[i, v] for i, v in enumerate(leaderboard)]:
        if v["tokens"] < player.max_tokens:
            leaderboard.insert(index, player_info)
            break
        elif index == len(leaderboard) - 1:
            leaderboard.insert(index + 1, player_info)
        else:
            continue
    write_to_json(LEADERBOARD_FILE, leaderboard)


def game(player, no_of_decks=6):
    deck = get_decks(no_of_decks)
    # create dealer instance
    dealer = Player("Dealer")

    # main game loop, is broken if person doesn't want to play again
    playing = True
    while playing:
        # set player attributes to default
        player.hand = []
        player.count = 0
        player.blackjack = False
        player.bust = False
        player.bet_multiplier = 1
        # set dealer attributes to default
        dealer.hand = []
        dealer.count = 0
        dealer.blackjack = False
        dealer.bust = False
        # sets turn loops to true and gets cards for the dealer and player
        player_turn = True
        dealer_turn = True
        dealer.draw_card(deck)
        player.get_hand(deck)
        # set player bet or show respective error
        while True:
            try:
                player.bet = input(f"What will your bet be {player.nick}? You have {player.tokens} tokens to your "
                                   f"name. Keep in mind, if you choose over 50% of your total tokens you will not "
                                   f"be allowed to double down\n")
                break
            except ValueError as e:
                print(e)
        # starts players turn
        while player_turn:
            player_decision = True
            player_action = None

            double_down = "or (D)ouble down" if (len(player.hand) == 2 and player.bet <= player.tokens / 2) else ""
            # gives player info on their hand
            print(write_hand(dealer))
            print(f"The value of your hand is {player.count}")

            print(write_hand(player))
            # check for player blackjack
            if player.check_blackjack():
                print("BLACKJACK! You now have a great chance of winning")
                player_turn = False
                continue
            # get player action, if it is one of the actions allowed continue on, otherwise keep asking for action
            while player_decision:
                player_action = input(f"Do you want to (H)it, (S)tand {double_down}?\n =>")
                if len(player_action) > 0 and player_action.lower()[0] in ["h", "s", "d" if double_down else None]:
                    player_decision = False
            # evaluate player actions
            if player_action == "s":
                player_turn = False
                continue
            elif player_action == "d":
                # if player doubles down, and they go bust they lose and lose their bet respectively otherwise they
                # go on
                if not player.double_down(deck):
                    print(
                        f"You have gone bust on your double down, the card you drew was a {player.hand[-1]['value']}")
                else:
                    print(f"Your double down card is a {player.hand[-1]['value']}")
                player_turn = False
                continue
            elif not player.draw_card(deck):
                # last possible option of action, checks if player has gone bust
                print(f"You have gone bust, the card you last drew was a {player.hand[-1]['value']}")
                player_turn = False
                continue
            else:
                # players hasn't gone bust so ask for action again
                continue
        print(f"final player hand is\n {write_hand(player)}")
        dealer.draw_card(deck)
        while dealer_turn:
            # dealers game
            # check dealer blackjack
            if dealer.check_blackjack():
                print("The dealer got a blackjack!")
                dealer_turn = False
                continue
            # if dealer has count less than 17 they draw a card
            elif dealer.count <= 16:
                if not dealer.draw_card(deck):
                    print(f"The dealer has gone bust their final hand is\n {write_hand(dealer)}")
                    dealer_turn = False
                    continue
            else:
                dealer_turn = False
                continue
        print(f"The dealers final hand is\n {write_hand(dealer)}")
        print(f"The dealers final hand value is {dealer.count}")
        # evaluate result and ask to play again
        # check for either person bust and add or remove tokens respectively
        if player.bust:
            print("You have lost the game.")
            player.tokens -= player.bet * player.bet_multiplier
            player.lost += 1
        elif dealer.bust:
            print("Congratulations! You win.")
            player.tokens += player.bet * player.bet_multiplier
            player.won += 1

        # checks for draw or win on blackjack
        elif dealer.count == 21 or player.count == 21:
            if player.blackjack and not dealer.blackjack:
                print("Congratulations! You win the game with a blackjack.")
                player.won += 1
                player.tokens += player.bet * player.bet_multiplier
            elif dealer.blackjack and not player.blackjack:
                print("You have lost the game.")
                player.lost += 1
                player.tokens -= player.bet * player.bet_multiplier
            else:
                print("Unlucky, the game ended in a draw.")

        # evaluates rest of options
        elif player.count > dealer.count:
            print("Congratulations! You win.")
            player.tokens += player.bet * player.bet_multiplier
            player.won += 1
        elif player.count == dealer.count:
            print("Unlucky, the game ended in a draw.")
        else:
            print("You have lost the game.")
            player.lost += 1
            player.tokens -= player.bet * player.bet_multiplier

        # give player default 10 tokens if drop to 0
        if player.tokens <= 0:
            print("OH NO! Your tokens have dropped 0. We have given you 10 tokens to play again with.")
            player.tokens = 10
        # save info of player (saves to files)
        player.save_info()
        # tell them how many token they have
        print(f"You currently have {player.tokens} tokens to your name")
        # ask player if they want to play again
        deciding = True
        while deciding: # have player decide on what they want to do next, either continue playing or go back to the menu
            decision = input("Do you want to play again? (Y)es/(N)o").lower()
            if len(decision) > 0 and decision[0] in ["y", "n"]:
                match decision[0]:
                    case "y":
                        deciding = False
                    case "n":
                        deciding = False
                        playing = False
                break
            else:
                continue


def show_leaderboard():
    # gets the leaderboard and values withing it
    leaderboard = get_json(LEADERBOARD_FILE) or []
    output = "-" * 50 + "\n"
    for i, v in [[i, v] for i, v in enumerate(leaderboard)]:  # runs through each entry and gets in index along with the value
        output += f"{i}. {v['name']}" + " " * (40 - len(v["name"])) + str(v["tokens"]) + "\n"
    output += "-" * 50
    print(output)


def write_rules():
    # writes rules
    rules = '''
    Rules of Blackjack:
    - In blackjack you play against the dealer. 
    - After setting a bet you are given two cards. 
    - The dealer gets two cards but reveals only one of them. 
    - If the value of your first two cards adds up to 21 you got a blackjack. 
    - On your turn unless you get a blackjack or go bust you get asked to either hit, stand or double down if you can. 
    - By hitting you get given another card. 
    - Standing ends your turn. 
    - If at any given the sum of your hands value is over 21 you go bust and automatically lose. 
    - If at the end of a round you have a higher score than the dealer and have not gone bust you win. 
    - If you have a lesser score than the dealer or the dealer has a blackjack and you don't you lose the round. 
    - If you and the dealer have the same score or have both gotten blackjack then it's a draw(push). 
    -   Blackjack pays out 3:2.
        Winning pays out 1:1.
        A draw gives you back your bet.
        When losing you lose your bet 
    - Double down is an action taken at the beginning of your turn when you have 2 cards, you double your bet but 
    only get one last card before your turn automatically ends.'''
    print(rules)
