# Card Game API

import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for s in suits:
        for r in ranks:
            card = (s, r)
            deck.append(card)
    random.shuffle(deck)
    return deck

# deck = fresh_deck()
# print(deck)

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0], deck[1:]

# card, deck = hit(deck)
# print(card)

def count_score(cards):
    score = 0
    number_of_aces = 0
    for card in cards:
        rank = card[1]
        if rank == 'A':
            score += 11
            number_of_aces += 1
        elif rank in {'J', 'Q', 'K'}:
            score += 10
        else:
            score += rank
    while score > 21 and number_of_aces > 0:
        score -= 10
        number_of_aces -= 1
    return score

def show_cards(cards, message):
    print(message)
    for card in cards:
        print(' ', card[0], card[1])

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

