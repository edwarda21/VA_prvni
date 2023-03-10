import random
import re
import json
import os

PLAYERS_FILE = "players.json"
LEADERBOARD_FILE = "leaderboard.json"
STARTING_TOKENS = 20
BASE_TOKENS = 12


def can_split(hand):
    output = False
    if len(hand.contents) == 2:
        if hand.contents[0]["value"] in ["J", "Q", "K"] and hand.contents[1]["value"] in ["J", "Q", "K"]:
            output = True
        elif hand.contents[0]["value"] == hand.contents[1]["value"]:
            output = True
        else:
            output = False
    return output


def payout(player, hand, win=True):
    # give the player their bet back
    player.tokens += hand.bet
    # give the player the reward
    if win:
        player.tokens += hand.bet * hand.bet_multiplier


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


def write_hand(hand):
    output = f"Hand:\n"
    output += "-" * 30 + "\n"
    for i, card in enumerate(hand.contents):
        output += f"{i}.\t{card['value']} of {card['colour']} \n"
    output += "-" * 30 + "\n"
    return output


class Player:

    def __init__(self, nick, tokens=STARTING_TOKENS, won=0, lost=0, max_tokens=STARTING_TOKENS):
        self.hands = []
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
        hand = Hand(self, self._bet)
        for x in range(0, 2):
            hand.draw_card(in_deck)
        self.hands.append(hand)

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
        if tokens >= self.max_tokens:
            self.max_tokens = tokens
            update_leaderboard(self)
        self._tokens = tokens


class Hand:
    def __init__(self, player, bet=0):
        self.bet_multiplier = 1
        self.blackjack = False
        self.bust = False
        self.contents = []
        self.count = 0
        self.played = False
        self.bet = bet
        self.parent_player = player
        self.parent_player.tokens -= self.bet

    def draw_card(self, in_deck, card=None):
        # allows for optional 'drawing' of a predefined card if needed, keeps consistency of conditions and updates made
        # to the hand
        if card is None:
            card = in_deck.pop()

        # checks if the value of the card is an integer, if not then sets value to value of the corresponding card
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
            # adds card to hand and checks for hand value, if needed it strips off 10 points for an ace or goes bust
            self.contents.append(card)
            if self.count > 21:
                if find_ace(self.contents):
                    self.count -= 10
                    return True
                else:
                    self.bust = True
                    self.played = True
                    print(f"Sorry, you have gone bust, you have lost {self.bet * self.bet_multiplier} tokens")
                    print(f"The card you last drew was a {self.contents[-1]['value']}")
                    self.parent_player.lost += 1
                    self.parent_player.hands.remove(self)
                    return False
            else:
                return True

    def check_blackjack(self):
        if self.count == 21 and len(self.contents) == 2:
            self.blackjack = True
            self.played = True
            self.bet_multiplier = 1.5
            return True

    def double_down(self, in_deck):
        if self.bet is None:
            return False
        else:
            self.parent_player.tokens -= self.bet
            self.bet *= 2
            self.draw_card(in_deck)
            self.played = True
            return False if self.bust else True

    def split(self, in_deck):
        # removes current hand from the player and equalizes the tokens removed from player
        self.parent_player.hands.remove(self)
        self.parent_player.tokens += self.bet
        # created a new hand and adds it to the player, 'drawing' a card that was in the previous hand and a new one
        for i in range(2):
            card = self.contents.pop()
            if card["value"] == "A":
                card["type"] == "soft"
            hand = Hand(self.parent_player, self.bet)
            hand.draw_card(in_deck, card)  # sets the card to be 'drawn'
            hand.draw_card(in_deck)
            self.parent_player.hands.append(hand)


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
    try:
        with open(file) as f:
            content = f.read()
            try:
                output = json.loads(content) if len(content) > 0 else False
                return output
            except json.decoder.JSONDecodeError:
                raise IOError("There is a problem with the files. Please fix me")
    except FileNotFoundError as e:
        print(e)
        print(os.getcwd())
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
        # sets turn loops to true and gets cards for the dealer and player
        dealer_turn = True
        player_turn = True
        # set player bet or show respective error
        while True:
            try:
                player.bet = input(f"What will your bet be {player.nick}? You have {player.tokens} tokens to your "
                                   f"name. Keep in mind, if you choose over 50% of your total tokens you will not "
                                   f"be allowed to double down or split\n")
                break
            except ValueError as e:
                print(e)
        # set hand for player
        player.hands = []
        player.get_hand(deck)
        # set hand for dealer
        dealer.hands = []
        dealer_hand = Hand(dealer)
        dealer_hand.draw_card(deck)
        dealer.hands.append(dealer_hand)
        dealer_hand = dealer.hands[0]
        # starts players turn
        # TODO: fix what hands are getting currently played, maybe by breaking for loop that is withing a while loop
        while player_turn:
            rerun = False
            for i, hand in enumerate(player.hands):
                if rerun:
                    break
                if hand == player.hands[-1]:
                    player_turn = False
                if hand.played:
                    continue
                turn = True
                while turn:
                    player_decision = True
                    player_action = None

                    double_down = "or (D)ouble down" if (
                            len(hand.contents) == 2 and hand.bet <= player.tokens) else ""
                    split = "or s(P)lit" if (can_split(hand) and hand.bet <= player.tokens) else ""
                    # gives player info on their hand

                    print(f"Dealers hand: \n {write_hand(dealer_hand)}")
                    print(f"The value of your hand is {hand.count}")

                    print(write_hand(hand))
                    # check for player blackjack
                    if hand.check_blackjack():
                        print("BLACKJACK! You now have a great chance of winning")
                        turn = False
                        continue
                    # get player action, if it is one of the actions allowed continue on, otherwise keep asking for action
                    while player_decision:
                        player_action = input(f"Do you want to (H)it, (S)tand {double_down} {split}?\n =>")
                        if len(player_action) > 0 and player_action.lower()[0] in ["h", "s",
                                                                                   "d" if double_down else None,
                                                                                   "p" if split else None]:
                            player_decision = False
                    # evaluate player actions
                    if player_action == "s":
                        turn = False
                        hand.played = True
                        continue
                    elif player_action == "d":
                        # if player doubles down, and they go bust they lose and lose their bet respectively otherwise they
                        # go on
                        if hand.double_down(deck):
                            print(f"Your double down card is a {hand.contents[-1]['value']}")
                        turn = False
                        continue
                    elif player_action == "p":
                        hand.split(deck)
                        turn = False
                        rerun = player_turn = True
                    elif not hand.draw_card(deck):
                        # last possible option of action, checks if player has gone bust
                        # the draw card function automatically tells the player the hand has gone bust and removes the hand
                        turn = False
                        continue
                    else:
                        # players hasn't gone bust so ask for action again
                        continue
                print(f"The final hand state is\n {write_hand(hand)}")
        dealer_hand.draw_card(deck)
        while dealer_turn:
            # dealers game
            # check dealer blackjack
            if dealer_hand.check_blackjack():
                print("The dealer got a blackjack!")
                dealer_turn = False
                continue
            # if dealer has count less than 17 they draw a card
            elif dealer_hand.count <= 16:
                if not dealer_hand.draw_card(deck):
                    print(f"The dealer has gone bust their final hand is\n {write_hand(dealer_hand)}")
                    dealer_turn = False
                    continue
            else:
                dealer_turn = False
                continue
        print(f"The dealers final hand is\n {write_hand(dealer_hand)}")
        print(f"The dealers final hand value is {dealer_hand.count}")
        # evaluate result and ask to play again
        for hand in player.hands:
            if dealer_hand.bust:
                print("Congratulations! You win.")
                payout(player, hand)
                player.won += 1

            # checks for draw or win on blackjack
            elif dealer_hand.blackjack or hand.blackjack:
                if hand.blackjack and not dealer_hand.blackjack:
                    print("Congratulations! You win the game with a blackjack.")
                    player.won += 1
                    payout(player, hand)
                elif dealer_hand.blackjack and not hand.blackjack:
                    print("You have lost the game.")
                    player.lost += 1
                else:
                    print("Unlucky, the game ended in a draw.")
                    payout(player, hand, False)

            # evaluates rest of options
            elif hand.count > dealer_hand.count:
                print("Congratulations! You win.")
                payout(player, hand)
                player.won += 1
            elif hand.count == dealer_hand.count:
                print("Unlucky, the game ended in a draw.")
                payout(player, hand, False)
            else:
                print("You have lost the game.")
                player.lost += 1

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
        while deciding:
            decision = input("Do you want to play again? (Y)es/(N)o").lower()
            if len(decision) > 0 and decision[0] in ["y", "n"]:
                if decision[0] == "y":
                    deciding = False
                else:
                    deciding = False
                    playing = False
                break
            else:
                continue


def show_leaderboard():
    leaderboard = get_json(LEADERBOARD_FILE) or []
    output = "-" * 50 + "\n"
    for i, v in [[i, v] for i, v in enumerate(leaderboard)]:
        output += f"{i}. {v['name']}" + " " * (40 - len(v["name"])) + str(v["tokens"]) + "\n"
    output += "-" * 50
    print(output)
