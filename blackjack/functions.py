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
    def __init__(self,nick):
        self.hand = []
        self.count = 0
        self.blackjack = False
        self.bust = False
        self.nick = nick

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
            return True
