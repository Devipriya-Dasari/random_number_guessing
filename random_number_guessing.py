import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1
            if guess < number:
                print("Too low. Try a higher number.")
            elif guess > number:
                print("Too high. Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Oops! Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
