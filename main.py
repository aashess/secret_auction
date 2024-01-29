# from turtle import clear
import logo
 

print(logo.logo)
print("Welcome to Secret Auction Program.")


bidding_record = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela":123, "James", "321"}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("Enter Your Name?: ")
    bid = int(input("Enter Your Bid?: "))
    bidding_record[name] = bid
    should_continue = input("Are there any other bidders? Type 'Yes or No'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bidding_record)
    
    
    




