# Number Guessing Game #
import random
import art

print(art.logo)
keepPlaying = True
num = random.randint(1,100)

print("Welcome to the Number Guessing Game")
print("Im thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Choose Level
if level == "easy":
  numOfGuesses = 10
else: numOfGuesses = 5

# Game
while keepPlaying:
  print(f"You have {numOfGuesses} guesses remaining.")
  guess = int(input("What's your guess?: "))
  if guess == num:
    print(f"You got it! The number was {num}")
    keepPlaying = False
  elif guess > num:
    print("Too High.\nGuess Again.")
    numOfGuesses -= 1
  elif guess < num:
    print("Too Low.\nGuess Again.")
    numOfGuesses -= 1
  

