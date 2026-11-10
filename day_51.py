import random

number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")

while True:
    guess = int(input("Guess a number (1-100): "))

    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")