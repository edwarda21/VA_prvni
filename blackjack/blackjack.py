from pprint import pprint
import random


def get_decks(in_number_of_decks):
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colours = ["H", "C", "S", "D"]
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
    def __init__(self):
        self.hand = []
        self.count = 0
        self.blackjack = False
        self.bust = False

    def get_hand(self, in_deck):
        for x in range(0, 2):
            self.draw_card(in_deck)

    def draw_card(self, in_deck):
        card = random.choice(random.choice(in_deck))
        # TODO use pop to get random card you faggot
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
            return True


no_of_decks = 6
deck = get_decks(no_of_decks)
pprint(deck)
player1 = Player()
dealer = Player()

# deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
# int("J") test line to check what error to check for in except clause
# create a game loop to play around with
dealer.draw_card(deck)
player1.get_hand(deck)
pprint(f"The dealers card is {dealer.hand}")
while True:
    print(f"The value of your hand is {player1.count}")
    print("Your cards are:")
    pprint(player1.hand)
    if player1.check_blackjack():
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
        break

dealer.draw_card(deck)
while True:
    # dealers game
    if dealer.check_blackjack():
        print("The dealer got a blackjack!")
        break
    if dealer.count <= 16:
        if not dealer.draw_card(deck):
            print(f"The dealer has gone bust their final hand is {dealer.hand}")
            break
    else:
        print(f"The dealers final hand is {dealer.hand}")
        print(f"The dealers final hand value is {dealer.count}")
        break
# evaluate code and ask to play again
if player1.bust:
    print("You have lost the game.")
elif dealer.bust:
    print("Congratulations! You win.")
elif dealer.count == 21 == player1.count:
    if player1.blackjack and not dealer.blackjack:
        print("Congratulations! You win the game with a blackjack.")
    elif dealer.blackjack and not player1.blackjack:
        print("You have lost the game.")
    else:
        print("Unlucky, the game ended in a draw.")
elif player1.count > dealer.count:
    print("Congratulations! You win.")
else:
    print("You have lost the game.")
