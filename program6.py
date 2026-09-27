secret_number = 7

guess = int(input("Guess the number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess. Try again!")