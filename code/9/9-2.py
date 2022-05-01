def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])