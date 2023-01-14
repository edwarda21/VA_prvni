from pprint import pprint
import random


# create deck of cards


def get_deck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["H", "C", "S", "D"]
    out_deck = [[{"value": value, "colour": colour} for value in values] for colour in colours]
    return out_deck


def draw_card(in_deck, in_hand_value, in_hand):
    card = random.choice(random.choice(in_deck))
    out_hand = in_hand
    out_val_of_hand = in_hand_value
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
    out_hand.append(card)
    out_val_of_hand += value
    return out_hand, out_val_of_hand


deck = []
no_of_decks = 1
hand = []
val_of_hand = 0
for i in range(0, no_of_decks):
    deck += get_deck()
for x in range(0, 2):
    hand, val_of_hand = draw_card(deck, val_of_hand, hand)
pprint(hand)
pprint(val_of_hand)
# deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
# int("J") test line to check what error to check for in except clause
