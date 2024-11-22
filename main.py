# Alex Williams
# 11/22/2024
# Web and App Devlopment




# Number Guess Game with WHILE Loop

# import random

# name = input("Hello what is your name?:\n")
# number = random.randint(1,100)
# print(f"Hi {name}, I'm thinking of a number between 1 and 100.")
# guessesTaken = 0
# while guessesTaken < 5:
#     guess = int(input("Enter a guess:\n"))
#     guessesTaken = guessesTaken + 1
#     if guess < number:
#         print("That was too low.")
#     elif guess > number:
#         print("Number was too high!")
#     else:
#         break
    
# if guess == number:
#     print(f"Winner, Congrats! {name} you guesed the correct number")
# else:
#     print(f"You lose, too bad. Better luck next time. The right number was {number}")



# Managing a List with a WHILE Loop
    
temperature = int(input("Please enter a temperature in degrees F(-9999 to quit): \n"))
length = []
while not temperature == -9999:
    temperature = int(input("Please enter a temperature in degrees F (-9999 to quit):\n"))
    length.append(temperature)
if len(length) > 0:
    print(f'Temperatures entered: {length}')
    average_temp = sum(length) / len(length)
    print(f'average temperature {average_temp}')
else:
    print("No temperatures were entered")