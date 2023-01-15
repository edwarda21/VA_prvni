from pprint import pprint
import random


def get_decks(in_number_of_decks):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "A", "A", "A"]
    colours = ["H", "C", "S", "D"]
    out_deck = []
    for decks in range(0, in_number_of_decks):
        out_deck += [[{"value": value, "colour": colour, "type": "soft"} for value in values] for colour in colours]
    return out_deck


def find_ace(in_hand):
    for card in in_hand:
        if card["value"] == "A" and card["type"] == "soft":
            card["type"] = "hard"
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
            elif self.val_of_hand + 11 > 21:
                self.val_of_hand += 1
                card["type"] = "hard"
            else:
                self.val_of_hand += 11
        finally:
            self.hand.append(card)
            if self.val_of_hand > 21:
                if find_ace(self.hand):
                    self.val_of_hand -= 10
                    return True
                else:
                    return False
            else:
                return True

        # gets the value of drawn card, if the value is not a number then value is assigned manually, hence try except
        # finally clause there to always check the value of the persons hand see if they are bust or not

    def check_win(self):
        if self.val_of_hand == 21 and len(self.hand) == 2:
            return True


no_of_decks = 6
deck = get_decks(no_of_decks)
player1 = Player()
dealer = Player()

# deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
# int("J") test line to check what error to check for in except clause
# create a game loop to play around with
dealer.draw_card(deck)
player1.get_hand(deck)
pprint(f"The dealers card is {dealer.hand}")
while True:
    print(f"The value of your hand is {player1.val_of_hand}")
    print("Your cards are:")
    pprint(player1.hand)
    if player1.check_win():
        print("BLACKJACK! You now have a great chance of winning")
        break
    while True:
        h_or_s = input("Do you want to (H)it or (S)tand?\n =>")
        if len(h_or_s) > 0 and h_or_s.lower()[0] in ["h", "s"]:
            break
    if h_or_s == "s":
        break
    if not player1.draw_card(deck):
        print(f"You have gone bust, the card you last drew was a {player1.hand[len(player1.hand) - 1]['value']}")
        print(f"Your final hand value was {player1.val_of_hand}")
        break

dealer.draw_card(deck)
while True:
    # dealers game
    if dealer.check_win():
        print("The dealer got a blackjack!")
        break
    if dealer.val_of_hand <= 16:
        if not dealer.draw_card(deck):
            print(f"The dealer has gone bust their final hand is {dealer.hand}")
            break
    else:
        print(f"The dealers final hand is {dealer.hand}")
        print(f"The dealers final hand value is {dealer.val_of_hand}")
        break
#