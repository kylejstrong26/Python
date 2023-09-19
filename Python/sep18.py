# Calculate average student height #

#input
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

averageHeight=0

for height in student_heights:
    averageHeight+=height

#calculation
finalHeight = round(averageHeight/len(student_heights))

print(f"Average student height: {finalHeight}")



# Find the highest score #

# input
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

currentScore = 0
for score in student_scores:
    if score > currentScore:
        currentScore = score

print(f"The highest score in the class is: {currentScore}")



# Fizzbuzz #

# If number is divisible by 3: say "Fizz"
# If number is divisible by 5: say "Buzz"
# If number is divisible by 3 & 5: say "Fizzbuzz"

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("Fizzbuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
        
        
        

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

sel_letters=""
sel_symbols=""
sel_numbers=""

#select random characters for the desired input
for char in range(1,nr_letters+1):
  sel_letters += letters[random.randrange(0,len(letters))]

for sym in range(1,nr_symbols+1):
  sel_symbols += symbols[random.randrange(0,len(symbols))]

for num in range(1,nr_numbers+1):
  sel_numbers += numbers[random.randrange(0,len(numbers))]

#add three strings to make one password
password = sel_letters + sel_symbols + sel_numbers

#randomize password
passList = list(password)
random.shuffle(passList)
password = ''.join(passList)
print(password)