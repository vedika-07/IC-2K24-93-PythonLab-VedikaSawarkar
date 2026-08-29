# Program 8: Number Guessing Game

import random

number = random.randint(1, 100)

print("Guess a number between 1 and 100")

for i in range(7):

    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You won.")
        break

    elif guess < number:
        print("Too low")

    else:
        print("Too high")

else:
    print("You lost.")
    print("The number was:", number)