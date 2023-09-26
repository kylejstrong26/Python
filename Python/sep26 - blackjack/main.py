import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userHand = []
dealerHand = []

def dealCard():
  userHand.append(random.choice(cards))
  dealerHand.append(random.choice(cards))

def calcScore(list):
  score = sum(list)
  if list.length() == 2 and score == 21:
    return 0
  elif list.count(11) > 0 and score > 21:
    list.remove(11)
    list.append(1)
    score = sum(list)
    return score
  else:
    return score


# Gameplay
play = input(print("Do you want to play a game of Blackjack? (y/n) ").lower())
if play == "n":
  print("Thanks for stopping by!")

dealCard()
userScore = calcScore(userHand)
dealerScore = calcScore(dealerHand)

if userScore == 0:
  print("You win!")
elif userScore > 21:
  print("You lose!")
elif dealerScore == 0:
  print("You lose!")
elif dealerScore > 21:
  print("You win!")
else: