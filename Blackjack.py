#An ambitious project to make BLACKJACK

import random
import os

#Object Oriented programming Practice.
class Card: #Basic properties of the card

    def __init__(self, card_face, value, symbol):
        self.card_face = card_face
        self.value = value
        self.symbol = symbol


def show_cards(cards, hidden): #All just graphics and stuff. Just Drawing of hidden and shown cards.
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card.card_face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|  {}             |'.format(card.card_face)
        elif card.value == 10:
            s = s + '\t|  {}            |'.format(card.value)
        else:
            s = s + '\t|  {}             |'.format(card.value)

    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|      * *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|    *     *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|       {}        |'.format(card.symbol)
    if hidden:
        s += '\t|          *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|         *      |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = '' #Card Faces and values
    for card in cards:
        if card.card_face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|            {}   |'.format(card.card_face)
        elif card.value == 10:
            s = s + '\t|           {}   |'.format(card.value)
        else:
            s = s + '\t|            {}   |'.format(card.value)
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|________________|'
    if hidden:
        s += '\t|________________|'
    print(s)
    print()


def deal_card(deck): #Using random to have a card check
    card = random.choice(deck)
    deck.remove(card)
    return card, deck


def play_blackjack(deck):#All Balckjack Properties and rules
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    os.system('cls')

    while len(player_cards) < 2:
        player_card, deck = deal_card(deck)
        player_cards.append(player_card)
        player_score += player_card.value

        if len(player_cards) == 2:
            if player_cards[0].value == 11 and player_cards[1].value == 11:
                player_cards[0].value = 1
                player_score -= 10

        print('PLAYER CARDS: ')
        show_cards(player_cards, False)
        print('PLAYER SCORE = ', player_score)

        input(' Press Enter and Continue...')

        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

        if len(dealer_cards) == 2:
            if dealer_cards[0].value == 11 and dealer_cards[1].value == 11:
                dealer_cards[1].value = 1
                dealer_score -= 10

        print('DEALER CARDS: ')
        if len(dealer_cards) == 1:
            show_cards(dealer_cards, False)
            print('DEALER SCORE = ', dealer_score)
        else:
            show_cards(dealer_cards[:-1], True)
            print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)

        input('Continue...')

    if player_score == 21:
        print('PLAYER HAS A BLACKJACK!!!!')
        print('PLAYER WINS!!!!')
        quit()
    os.system('cls')

    print('DEALER CARDS: ')
    show_cards(dealer_cards[:-1], True)
    print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)
    print()
    print('PLAYER CARDS: ')
    show_cards(player_cards, False)
    print('PLAYER SCORE = ', player_score)

    while player_score < 21:
        choice = input('Enter H to Hit or S to Stand: ').upper()
        if len(choice) != 1 or (choice not in ['H', 'S']):
            os.system('cls')
            print('Invalid choice!! Try Again...')
            continue

        if choice.upper() == 'S':
            break
        else:
            player_card, deck = deal_card(deck)
            player_cards.append(player_card)
            player_score += player_card.value
            card_pos = 0

            # If dealt an Ace, adjust score for each existing Ace in hand
            while player_score > 21 and card_pos < len(player_cards):
                if player_cards[card_pos].value == 11:
                    player_cards[card_pos].value = 1
                    player_score -= 10
                    card_pos += 1
                else:
                    card_pos += 1

            if player_score > 21:
                break

            os.system('cls')
            print('DEALER CARDS: ')
            show_cards(dealer_cards[:-1], True)
            print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)
            print()
            print('PLAYER CARDS: ')
            show_cards(player_cards, False)
            print('PLAYER SCORE = ', player_score)

    os.system('cls')
    print('PLAYER CARDS: ')
    show_cards(player_cards, False)
    print('PLAYER SCORE = ', player_score)
    print()
    print('DEALER IS REVEALING THEIR CARDS....')
    print('DEALER CARDS: ')
    show_cards(dealer_cards, False)
    print('DEALER SCORE = ', dealer_score)

    if player_score == 21:
        print('PLAYER HAS A BLACKJACK, PLAYER WINS!!!')
        quit()

    if player_score > 21:
        print('PLAYER BUSTED!!! GAME OVER!!!')
        quit()

    input('Continue...')
    while dealer_score < 17:
        os.system('cls')
        print('DEALER DECIDES TO HIT.....')
        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

        #The trickiest bit in my opinion. Adjusting for aces if multiple show up due to its variable value
        card_pos = 0
        while dealer_score > 21 and card_pos < len(dealer_cards):
            if dealer_cards[card_pos].value == 11:
                dealer_cards[card_pos].value = 1
                dealer_score -= 10
                card_pos += 1
            else:
                card_pos += 1

        print('PLAYER CARDS: ')
        show_cards(player_cards, False)
        print('PLAYER SCORE = ', player_score)
        print()
        print('DEALER CARDS: ')
        show_cards(dealer_cards, False)
        print('DEALER SCORE = ', dealer_score)
        if dealer_score > 21:
            break
        input('Continue...')

    if dealer_score > 21:
        print('DEALER BUSTED!!! YOU WIN!!!')
        quit()
    elif dealer_score == 21:
        print('DEALER HAS A BLACKJACK!!! PLAYER LOSES!!!')
        quit()
    elif dealer_score == player_score:
        print('TIE GAME!!!!')
    elif player_score > dealer_score:
        print('PLAYER WINS!!!')
    else:
        print('DEALER WINS!!!')


def init_deck():#And the game begins.
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    suit_symbols = {'Hearts': '\u2661', 'Diamonds': '\u2662', #First time using unicode, so not sure but I'll do it.
                    'Spades': '\u2664', 'Clubs': '\u2667'}
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    deck = []
    for suit in suits:
        for card, value in cards.items():
            deck.append(Card(card, value, suit_symbols[suit]))
    return deck

print("Hey I'm Naval, Let's play blackjack!!")
if __name__ == '__main__':
    deck = init_deck()
    play_blackjack(deck)