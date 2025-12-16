#Highest bidder code program. The bidding will be secret from other bidders. The bidder with highest bid wins.
bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False

def find_highest_bidder(bidding_dictionary):
    winner = ""
    high = 0
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > high:
            high = bidding_dictionary[bidder]
            winner = bidder
    return winner

print(f"The winner is {find_highest_bidder(bids).capitalize()}.")