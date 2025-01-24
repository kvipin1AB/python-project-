# Guess the number
# import random

# randNum = random.randint(1, 100)

# while True:
#     userChoice = int(input("Guess the target or Quit(Q) : "))
#     if(userChoice=="Q"):
#         break
#     userChoice = int(userChoice)
#     if userChoice == randNum:
#         print("Success: Correct Guess!!")
#         break  # Exit the loop when the guess is correct
#     elif userChoice < randNum:
#         print("Your number was too small. Take a bigger guess...")
#     else:
#         print("Your number was too big. Take a smaller guess...")
        
# print("------Game Over-------")


# Random Password Generator
import random
import string
pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# list Comprehension 

Password = "&".join ([random.choice(charValues) for i in range(pass_len)])



# Password = ""
# for i in range(pass_len):
#     Password += random.choice(charValues)

print("your random Password is :",Password)






print(random.choice(charValues))
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(random.choice("hello"))