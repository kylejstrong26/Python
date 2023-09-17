# Instructions

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."



print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

total_lower = lower_name1 + lower_name2

#TRUE
trueNum=0
trueNum += int(total_lower.count("t"))
trueNum += int(total_lower.count("r"))
trueNum += int(total_lower.count("u"))
trueNum += int(total_lower.count("e"))

#Love
loveNum=0
loveNum += int(total_lower.count("l"))
loveNum += int(total_lower.count("o"))
loveNum += int(total_lower.count("v"))
loveNum += int(total_lower.count("e"))

strLoveNum=str(loveNum)
strTrueNum=str(trueNum)

strScore = strTrueNum + strLoveNum
intScore = int(strScore)

if intScore <10 or intScore > 90:
    print(f"Your score is {intScore}, you go together like coke and mentos.")
elif 40 < intScore < 50:
    print(f"Your score is {intScore}, you are alright together.")
else:
    print(f"Your score is {intScore}")