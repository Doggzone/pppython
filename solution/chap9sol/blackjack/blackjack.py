# Blackjack primer

from cardgame import *

def blackjack():
    print("Welcome to Softopia Casino")
    deck = fresh_deck()
    chips = 0
    while True:
        print("-----")
        ## hands out two cards each
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        # shows dealer's hand
        print("My cards are:")
        print("  **** **")
        print(' ', dealer[1][0], dealer[1][1])
        # shows player's hand
        show_cards(player, "Your cards are:")
        # calculates the score of each hand
        score_dealer = count_score(dealer)
        score_player = count_score(player)
        # judges who wins and adjusts chips
        if score_player == 21:
            print("Blackjack! You won.")
            chips += 2
        else:
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ", card[0], card[1])
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                elif score_dealer == score_player:
                    print("We draw.")
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                else:
                    print("I won.")
                    chips -= 1
        print("Chips =", chips)
        if not more("Play more? (y/n) "):
            break
    print("-----")
    print("Bye!")

blackjack()
