import copy
import random
cards = [
   ##"ace", "ace", "ace", "ace", "ace",
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    10, 10, 10, 10,
    10, 10, 10, 10,
    10, 10, 10, 10]

cards_in_deck = copy.deepcopy(cards)
player_cards = []
dealer_cards = []

def shuffle_cards():
    random.shuffle(cards_in_deck)

def check_status():
    print("status func running")
    if sum(player_cards) == 21:
        print("The player has won the game!")
        return False
    elif sum(player_cards) > 21:
        print("Player has busted. Dealer wins!")
        return False
   ## elif sum(player_cards) > sum(dealer_cards) and is_player_hitting == "stand":
     ##   print("player has won as they have", sum(player_cards), "and the dealer has", sum(dealer_cards))
     ##   return False


    if sum(dealer_cards) == 21:
        print("The dealer has won the game!")
        return False
    elif sum(dealer_cards) > 21:
        print("Dealer has busted. Player wins!")
        return False
    elif sum(dealer_cards) > 17 and  sum(player_cards):
        print("Dealer has won as they have", sum(dealer_cards), "and the player has", sum(player_cards))
        return False
    elif sum(dealer_cards) == sum(player_cards) and sum(dealer_cards) >= 17:
        print("game has ended in a draw!")
        return False

    else:
        return True

def start_cards():
    print("test")
    if len(player_cards) == 0:
        shuffle_cards()
        for i in range(2):
            card = cards_in_deck.pop(0)
            if card == "ace":
                player_ace(new_ace = True)
            else:
                card = int(card)
                player_cards.append(card)

            ## Gives dealer a card
            card = cards_in_deck.pop(0)
            if card == "ace":
                dealer_ace(new_ace = True)
            else:
                card = int(card)
                dealer_cards.append(card)
    print(player_cards)
    print(dealer_cards[1])

def player_hit():
    while True:
        if not check_status():
            break
        else:
            is_player_hitting = input("Would you like to hit or stand?")

        if not is_player_hitting == "hit":
            break

        if len(player_cards) >= 2 and is_player_hitting == "hit":
            print("dealing 1 card to player because they hit")
            card = cards_in_deck.pop(0)
            if card == "ace":
                player_ace(new_ace = True)
                print("player has gotten an ace and triggering ace logic")

            else:
                card = int(card)
                player_cards.append(card)
                player_ace(new_ace=False)


        print(player_cards)
        print(dealer_cards)


def dealer_hit():
    while True:
        if not check_status():
            break

        if sum(dealer_cards) >= 17:
            print("dealer can't hit anymore as he has 17 or greater")
            check_status()
            break
        print("dealing 1 card to dealer because their total is less than player")
        card = cards_in_deck.pop(0)
        if card == "ace":
            dealer_ace(new_ace = True)
        else:
            card = int(card)
            dealer_cards.append(card)
        dealer_ace(new_ace = False)
        print(player_cards)
        print(dealer_cards)

def player_ace(new_ace):
    value1 = 1
    value2 = 11

    if new_ace == True:
        if value2 + sum(player_cards) <= 21:
            player_cards.append(11)

        else:
            player_cards.append(1)

    if sum(player_cards) > 21 and value2 in player_cards:
        player_cards.append(1)

        try:
            player_cards.remove(11)
        except ValueError:
            print("Tried to remove value 11 from players cards but not found. YOU FUCKED UP FIX IT")

    check_status()


def dealer_ace(new_ace):
    value1 = 1
    value2 = 11

    if new_ace == True:
        if value2 + sum(dealer_cards) <= 21:
            dealer_cards.append(11)

        else:
            dealer_cards.append(1)

    if sum(dealer_cards) > 21 and value2 in dealer_cards:
        dealer_cards.append(1)
        try:
            dealer_cards.remove(11)
        except ValueError:
            print("Tried to remove value 11 from dealers cards but not found. YOU FUCKED UP FIX IT")
    check_status()









start_cards()
player_hit()
if check_status():
    dealer_hit()

