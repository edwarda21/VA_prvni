from pprint import pprint
import random


def get_decks(in_number_of_decks):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["H", "C", "S", "D"]
    out_deck = []
    for decks in range(0, in_number_of_decks):
        out_deck += [[{"value": value, "colour": colour} for value in values] for colour in colours]
    return out_deck


class Player:
    def __init__(self):
        self.hand = []
        self.val_of_hand = 0

    def get_hand(self, in_deck):
        for i in range(0, 2):
            self.draw_card(in_deck)

    def draw_card(self, in_deck):
        card = random.choice(random.choice(in_deck))
        for suit in deck:
            try:
                suit.remove(card)
            except ValueError:
                pass
            else:
                break
        # gets a random card from deck and then removes it.
        # deck is list created of suits (lists) so there is try and except block to check if card can be removed from suit
        try:
            value = int(card["value"])
        except ValueError:
            if card["value"] in ["J", "Q", "K"]:
                value = 10
            else:
                value = 11
        # gets the value of drawn card, if the value is not a number then value is assigned manually, hence try except
        self.hand.append(card)
        self.val_of_hand += value


no_of_decks = 6
deck = get_decks(no_of_decks)
player1 = Player()

pprint(player1.hand)
pprint(player1.val_of_hand)
# deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
# int("J") test line to check what error to check for in except clause
# create a gameloop to play around with
while True:
    while True:
        h_or_s = input("Do you want to (H)it or (S)tand?")
        if h_or_s.lower()[0] in ["h", "s"]:
            break
    if h_or_s == "s":
        break
    player1.draw_card(deck)
    if player1.val_of_hand > 21:
        for i in player1.hand:
            if i["value"] == "A":
                player1.val_of_hand -= 10
                break
        print(f"Sorry, you have gone bust your final hand is {hand}")
        break
    print(f"The value of your hand is {val_of_hand}")
    print(f"Your cards are {hand}")
while True:
    # dealers game
    dealer_hand = []
    dealer_val_of_hand = 0
