
repeat = True
bid = {}
def find_highest_bidder(bidding):
    value = 0
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount>value:
            value = bid_amount
            winner = bidder

    print('The winner is', bidder, 'with an amoutn of', value)


while repeat == True:
    name = input("What's your name? ")
    price = int(input("What's your bid? $"))
    bid[name]=price
    if input("New user?") == 'yes':
        repeat = True
    else:
        repeat = False
find_highest_bidder(bid)

print(bid)

