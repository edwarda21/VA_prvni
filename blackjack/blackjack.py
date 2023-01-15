from pprint import pprint
import random


def get_decks(in_number_of_decks):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["H", "C", "S", "D"]
    out_deck = []
    for decks in range(0, in_number_of_decks):
        out_deck += [[{"value": value, "colour": colour} for value in values] for colour in colours]
    return out_deck


def find_ace(in_hand):
    for card in in_hand:
        if card["value"] == "A":
            return True
    return False


class Player:
    def __init__(self):
        self.hand = []
        self.val_of_hand = 0

    def get_hand(self, in_deck):
        for x in range(0, 2):
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
        # deck is list created of suits (lists) try and except block to check if card can be removed from suit
        try:
            self.val_of_hand += int(card["value"])
        except ValueError:
            if card["value"] in ["J", "Q", "K"]:
                self.val_of_hand += 10
            else:
                self.val_of_hand += 11
        finally:
            self.hand.append(card)
            if self.val_of_hand > 21:
                if not find_ace(self.hand):
                    return False
                else:
                    self.val_of_hand -= 10
            else:
                return True

        # gets the value of drawn card, if the value is not a number then value is assigned manually, hence try except
        # finally clause there to always check the value of the persons hand see if they are bust or not


no_of_decks = 6
deck = get_decks(no_of_decks)
player1 = Player()
dealer = Player()

# deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
# int("J") test line to check what error to check for in except clause
# create a game loop to play around with
dealer.draw_card(deck)
player1.get_hand(deck)
print(f"The dealers card is {dealer.hand}")
while True:
    print(f"The value of your hand is {player1.val_of_hand}")
    print(f"Your cards are {player1.hand}")
    while True:
        h_or_s = input("Do you want to (H)it or (S)tand?\n")
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
        print(f"Sorry, you have gone bust your final hand is {player1.hand}")
        break
dealer.draw_card(deck)
while True:
    # dealers game
    if dealer.val_of_hand <= 16:
        print(dealer.val_of_hand)
        print("Card is drawn")
        if not dealer.draw_card(deck):
            print(f"The dealer has gone bust their final hand is {dealer.hand}")
            break
        print(dealer.val_of_hand)
    else:
        print(f"The dealers final hand is {dealer.hand}")
        print(f"The dealers final hand value is {dealer.val_of_hand}")
        break
