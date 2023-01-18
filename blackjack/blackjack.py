from pprint import pprint
import functions as f
no_of_decks = 6
deck = f.get_decks(no_of_decks)
player1 = f.Player("Dude")
dealer = f.Player("dealer")

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
