from pprint import pprint
import functions as f

no_of_decks = 6
deck = f.get_decks(no_of_decks)
player1 = f.Player("Dude")
dealer = f.Player("dealer")
player_turn = True
dealer_turn = True
# deck.remove({"colour":"orange","value":"queen"}) test line to check what error to use in except clause
# int("J") test line to check what error to check for in except clause
# create a game loop to play around with
dealer.draw_card(deck)
player1.get_hand(deck)
pprint(f"The dealers card is {dealer.hand}")
# starts players turn
while player_turn:
    player_decision = True
    # gives player info on their hand
    print(f"The value of your hand is {player1.count}")
    print("Your cards are:")
    double_down = "or (D)ouble down" if len(player1.hand) == 2 else ""
    pprint(player1.hand)
    # check for player blackjack
    if player1.check_blackjack():
        print("BLACKJACK! You now have a great chance of winning")
        player_turn = False
        continue
    # get player action
    while player_decision:
        player_action = input(f"Do you want to (H)it, (S)tand {double_down}?\n =>")
        if len(player_action) > 0 and player_action.lower()[0] in ["h", "s", "d" if double_down else None]:
            player_decision = False
    # evaluate player actions
    if player_action == "s":
        player_turn = False
        continue
    elif player_action == "d":
        if not player1.double_down(deck):
            print(f"You have gone bust on your double down card, the card you drew was a {player1.hand[-1]['value']}")
        else:
            print(f"Your double down card is a {player1.hand[-1]['value']}")
        player_turn = False
        continue
    if not player1.draw_card(deck):
        print(f"You have gone bust, the card you last drew was a {player1.hand[-1]['value']}")
        player_turn = False
        continue

print(f"final player hand is {player1.hand}")
dealer.draw_card(deck)
while dealer_turn:
    # dealers game
    # check dealer blackjack
    if dealer.check_blackjack():
        print("The dealer got a blackjack!")
        dealer_turn = False
        continue
    # if dealer has count less than 17 they draw a card
    if dealer.count <= 16:
        if not dealer.draw_card(deck):
            print(f"The dealer has gone bust their final hand is {dealer.hand}")
            dealer_turn = False
            continue
    else:
        print(f"The dealers final hand is {dealer.hand}")
        print(f"The dealers final hand value is {dealer.count}")
        dealer_turn = False
        continue
# evaluate result and ask to play again
# check for either person bust
if player1.bust:
    print("You have lost the game.")
elif dealer.bust:
    print("Congratulations! You win.")

# checks for draw or win on blackjack
elif dealer.count == 21 == player1.count:
    if player1.blackjack and not dealer.blackjack:
        print("Congratulations! You win the game with a blackjack.")
    elif dealer.blackjack and not player1.blackjack:
        print("You have lost the game.")
    else:
        print("Unlucky, the game ended in a draw.")

# evaluates rest of options
elif player1.count > dealer.count:
    print("Congratulations! You win.")
elif player1.count == dealer.count:
    print("Unlucky, the game ended in a draw.")
else:
    print("You have lost the game.")

while True:
    play = input("Do you want to play again? (Y)es or (N)o.")
    if len(play) == 0 or play.lower() not in ["y", "n"]:
        game = False
