secret = 42

guess1 = int(input("Guess 1: "))
if guess1 == secret:
    print("Correct!")
elif guess1 > secret:
    print("Too High")
else:
    print("Too Low")

guess2 = int(input("Guess 2: "))
if guess2 == secret:
    print("Correct!")
elif guess2 > secret:
    print("Too High")
else:
    print("Too Low")

guess3 = int(input("Guess 3: "))
if guess3 == secret:
    print("Correct!")
elif guess3 > secret:
    print("Too High")
else:
    print("Too Low")