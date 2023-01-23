import random


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
            self.bust = not self.draw_card(in_deck)
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
