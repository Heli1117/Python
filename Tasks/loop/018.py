import random

target = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < target:
        print("Too Low")
    elif guess > target:
        print("Too High")
    else:
        print("Correct! You guessed it in", attempts, "attempts.")
        break