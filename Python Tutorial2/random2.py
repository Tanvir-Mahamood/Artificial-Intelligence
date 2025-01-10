# guessing game
import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print(f"Select a number between {low} and {high}")
while is_running:
    if guesses == 5:
        print("Limit over")
        break
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("The number is out of range")
        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print("Correct")
            is_running = False
    else:
        print("Invalid guess")