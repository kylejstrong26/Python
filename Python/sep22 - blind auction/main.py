from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

# Print Art 
print(logo)
keepBidding = True
bidders = {}

while keepBidding == True:
  name = input("What's your name? ")
  bidPrice = int(input("How much do you want to bid? "))

  bidders[name] = bidPrice

  moreBidders = input("Are there more bidders? (y/n)").lower()
  if moreBidders == "y":
    clear()
  else:
    clear()
    keepBidding = False
winner = max(bidders)
print(f"The winner of the auction is {winner}")
    


