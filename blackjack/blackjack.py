# create deck of cards

values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
colours = ["H", "C", "S", "D"]
deck = [[{"value": value, "colour": colour} for value in values] for colour in colours]

print(deck)
