import random

# Program selects a random number between 1 and 100
random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

# Loop until the user guesses correctly
while True:
    try:
        # User inputs their guess
        guess = int(input("Enter your guess: "))

        # Provide feedback
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {random_number}.")
            break  # Exit the loop when the guess is correct
    except ValueError:
        print("Please enter a valid integer!")

print("Thanks for playing!")
