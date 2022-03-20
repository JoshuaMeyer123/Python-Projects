from art import logo
import os

def clear_console():
    os.system('cls')

print(logo)

bidding = {}
end_bidding = False

while not end_bidding:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bidding price?: $"))
    more_bidders = input("Are there any remaining bidders? Type 'yes' or 'no'. ")
    bidding[name] = bid_price
    if more_bidders == "no":
        end_bidding = True

    elif more_bidders == "yes":
        clear_console()

top_bid = 0
top_bidder = ""

for name in bidding:
    if bidding[name] > top_bid:
        top_bid = bidding[name]
        top_bidder = name

print(f"{top_bidder} had the highest bid and is the winner!")
