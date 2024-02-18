import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Hello! What is your name?")
    user_name = input()

    print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    while True:
        user_guess = int(input(''))
        attempts += 1

        if user_guess == secret_number:
            print(f"Good job, {user_name}! You guessed my number in {attempts} guesses!")
            break
        elif user_guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

guess_the_number()
