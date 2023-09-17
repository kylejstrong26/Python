#Heads or Tails#

import random

randomNum = random.random()

print("The coin is flipping!")

if randomNum <= 0.5: 
    print("Heads")
else:
    print("Tails")
    
    
    
    
# Credit Card Roulette #
import random

# split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# length of index
namesLength = len(names)

# random number from 1 to index size
randomNum = random.randint(1, namesLength)
chosenPerson = names[randomNum]

print(f"{chosenPerson} is going to buy the meal today!")




#Treasure Map#

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? (First Digit: Column, Second Digit Row) ")

# retrieve number from input
colNum = position[0]
rowNum = position[1]

# turn string of number to integer
intCol = int(colNum)
intRow = int(rowNum)

# place X in designated spot in index
map[intRow-1][intCol-1] = "x"

print(f"{row1}\n{row2}\n{row3}")




# Rock, Paper, Scissors #
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

userChoice = input("Rock, Paper or Scissors? ")
userChoice.lower()

# Rock=1, Paper=2, Scissors=3
computerChoice = random.randint(1,3)
print(computerChoice)

#computer chooses rock
if computerChoice == 1:
  if userChoice == "rock":
    print(f"You choose:\n{rock}")
    print(f"Computer Chooses:\n{rock}")
    print("\nYou Draw!")
  if userChoice == "paper":
    print(f"You choose:\n{paper}")
    print(f"Computer Chooses:\n{rock}")
    print("\nYou Win!")
  if userChoice== "scissors":
    print(f"You choose:\n{scissors}")
    print(f"Computer Chooses:\n{rock}")
    print("\nYou Lose!")

#computer chooses paper
if computerChoice == 2:
  if userChoice == "rock":
    print(f"You choose:\n{rock}")
    print(f"Computer Chooses:\n{paper}")
    print("\nYou Lose!")
  if userChoice == "paper":
    print(f"You choose:\n{paper}")
    print(f"Computer Chooses:\n{paper}")
    print("\nYou Draw!")
  if userChoice== "scissors":
    print(f"You choose:\n{scissors}")
    print(f"Computer Chooses:\n{paper}")
    print("\nYou Win!")

#computer chooses scissors
if computerChoice == 3:
  if userChoice == "rock":
    print(f"You choose:\n{rock}")
    print(f"Computer Chooses:\n{scissors}")
    print("\nYou Win!")
  if userChoice == "paper":
    print(f"You choose:\n{paper}")
    print(f"Computer Chooses:\n{scissors}")
    print("\nYou Lose!")
  if userChoice== "scissors":
    print(f"You choose:\n{scissors}")
    print(f"Computer Chooses:\n{scissors}")
    print("\nYou Draw!")

