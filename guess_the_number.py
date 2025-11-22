import random

secret_number = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1  # adds 1 each time

    if guess == secret_number:
        print("🎉 Correct! You guessed it!")
        break
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

if attempts == 3:
    print("Game over! The number was", secret_number)
