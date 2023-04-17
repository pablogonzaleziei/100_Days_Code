import random
def hand():
    print("Your cards: ", player_cards)
    print("Dealer cards: ", dealer_cards)

def hand_value(hand):
    total = 0
    for card in hand:
        total += card_value[card]
    return total

card_value = {
    "A": 1, "2": 2, 
    "3": 3, "4": 4, 
    "5": 5, "6": 6, 
    "7": 7, "8": 8, 
    "9": 9, "J": 10, 
    "Q": 10, "K": 10, 
}
deck = list(card_value.keys()) *4 #4 palos
random.shuffle(deck)
print(type(deck))
player_cards = [deck.pop(),deck.pop()]
dealer_cards = [deck.pop()]
hand()

player_turn = True
while player_turn == True:
    play = input("Do you want to hit or stand?")
    if play == "hit":
        player_cards.append(deck.pop())
        hand()
        
        if hand_value(player_cards) >= 21:
            print("You Bust!")
            player_cards = False
    else:
        player_turn = False

dealer_cards.append(deck.pop())
hand()
if hand_value(player_cards)<=21:
    while hand_value(dealer_cards)<17:
        dealer_cards.append(deck.pop())
        hand()
        if hand_value(dealer_cards) == hand_value(player_cards):
            print("Draw!")
        elif hand_value(dealer_cards) > hand_value(player_cards):
            print("You Loose!")
else:
    print("You Loose!")
