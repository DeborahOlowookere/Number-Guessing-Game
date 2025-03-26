import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))

        if user_guess < 1:
            print("Invalid Number. Number must be greater than 0.")
            continue

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
