import art
import gameData
import random
from replit import clear

# Format account data
def formatData(account):
  """Format data from account information"""
  accountName = account["name"]
  accountDescription = account["description"]
  accountCountry = account["country"]
  return f"{accountName}, a {accountDescription}, from {accountCountry}"

def checkAnswer(a,b,guess):
  """Check if user is correct by returning correct answer"""
  if a > b:
    return guess == "a"
  else:
    return guess == "b"

score = 0
keepPlaying = True
accountB = random.choice(gameData.data)

while keepPlaying:

  # Generate random account from gameData
  accountA = accountB
  accountB = random.choice(gameData.data)
  while accountA == accountB:
    accountB = random.choice(gameData.data)
  
  print(f"Compare A: {formatData(accountA)}")
  print(art.vs)
  print(f"Against B: {formatData(accountB)}")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  aFollowerCount = accountA["follower_count"]
  bFollowerCount = accountB["follower_count"]
  
  correct = checkAnswer(aFollowerCount,bFollowerCount, guess)

  # Clear screen
  clear()
  print(art.logo)
  
  if correct:
    score+=1
    print(f"That's Right! Score: {score}")
  else:
    print(f"Sorry, That's Wrong. Final Score: {score}")
    keepPlaying = False


  



  


















# keepPlaying = True
# score = 0

# def randPerson():
#   return random.choice(gameData.data)

# def checkScore():
#   global score
#   if score > 0:
#     print(f"You're right! Current Score: {score}. ")

# def increaseScore():
#   global score
#   score += 1
#   return score

# def swapPersonA(personA, personB):
#   personA = personB
#   return personA

# def newPersonB(personB):
#   personB = randPerson()
#   return personB

# def compare(choice, personA, personB, score):
#   global keepPlaying
#   if choice == 'a':
#     if personA['follower_count'] > personB['follower_count']:
#       increaseScore()
#       swapPersonA(personA,personB)
#       personB = newPersonB(personB)
#       return personB
#     else:
#       print(f"Sorry that's wrong. Final Score: {score}")
#       keepPlaying = False
#       return
#   else:
#     if personA['follower_count'] < personB['follower_count']:
#       increaseScore()
#       swapPersonA(personA,personB)
#       personB = newPersonB(personB)
#       return personB
#     else:
#       print(f"Sorry that's wrong. Final Score: {score}")
#       keepPlaying = False
#       return

# personA = randPerson()
# personB = randPerson()
# while keepPlaying:
#   print(art.logo)
#   while personA == personB:
#     personA = randPerson()
#   checkScore()
#   print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}")
#   print(art.vs)
#   print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}")
#   choice = input("Who has more followers? Type 'A' or 'B': ").lower()
#   compare(choice, personA, personB, score)
  
  
  
