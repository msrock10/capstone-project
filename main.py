import random

lb = 1
ub = 5
ma = 2
senu = random.randint(lb, ub)

def gg():
    while True:
        guess = int(input("Guess a number between 1 and 5: "))
        if lb <= guess <= ub:
            return guess
        else:
            print("Invalid input")

def check_guess(guess, senu):
    if guess == senu:
        return "correct"
    elif guess < senu:
        return "too low"
    else:
        return "too high"

def play_game():
    attempts = 0
    won = False

    while attempts < ma:
        attempts += 1
        guess = gg()
        result = check_guess(guess, senu)

        if result == "correct":
            print(f"Congratulations! You guessed the secret number {senu} in {attempts} attempts.")
            won = True
            break
        else:
            print(result)

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number was {senu}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()