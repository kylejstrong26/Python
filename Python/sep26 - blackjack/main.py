import random
import os
from art import logo

def dealCard():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calcScore(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, dealerScore):
    if userScore > 21 and dealerScore > 21:
      print("You Lose")
    elif userScore == 21:
        print("You Win")
    elif dealerScore == 21:
        print("You Lose")
    elif userScore > 21:
        print("You Lose")
    elif dealerScore > 21:
        print("You Win")
    elif userScore == dealerScore:
        print("You Draw")
    elif userScore > dealerScore:
        print("You Win")
    elif dealerScore > userScore:
        print("You Lose")


def playGame():
  
  print(logo)
  
  userHand = []
  dealerHand = []
  isGameOver = False
  
  for i in range(2):
      userHand.append(dealCard())
      dealerHand.append(dealCard())

  while not isGameOver:
    userScore = calcScore(userHand)
    dealerScore = calcScore(dealerHand)

    print(
      f"Your Cards: {userHand}, Current Score: {userScore}\nDealer's first card: {dealerHand[0]}"
    )

    if userScore == 0 or dealerScore == 0 or userScore > 21:
      isGameOver = True
    else:
      takeCard = input(print("Want another card?: (y/n) ")).lower()
      if takeCard == "y":
        userHand.append(dealCard())
      else:
        isGameOver = True

  while dealerScore != 0 and dealerScore < 17:
    dealerHand.append(dealCard())
    dealerScore = calcScore(dealerHand)

  print(
      f"Your Cards: {userHand}, Current Score: {userScore}\nDealer's Hand: {dealerHand}, Dealer's Score: {dealerScore}"
  )
  compare(userScore, dealerScore)


while input(print(
        "Do you want to play a game of Blackjack? (y/n) ")).lower() == "y":
    os.system('clear')
    playGame()
