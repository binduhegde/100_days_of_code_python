import random

def print_logo():
    print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\ | |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|""")

# takes the user's input about the level. 
# easy has 10 attempts and hard has only 5 attempts
def choose_level():
    while True:
        level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy': 
            return 10
        elif level == 'hard':
            return 5
        print("Please type 'easy' or 'hard'")

# Takes guesses from the user and makes sure it's an int
def take_int_input():
    while True:
        inp = input("\nMake a guess: ")
        try:
            inp = int(inp)
            break
        except ValueError:
            print("Please enter a valid number")
    return inp

# prints feedback about the user's guess
# returns false if the guess is wrong. true otherwise
def feedback(num, guess):
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    else:
        print(f"You got it! The answer was {num}.")
        return True
    return False

# executes the game
def game():
    print_logo()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    lives = choose_level()
    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = take_int_input()

        # exits game if the user guessed correctly
        if feedback(number, guess):
            return ''
        lives -= 1
    # if the function comes to this line, it only means the user lost. 
    # otherwise the function would have stooped after its return 
    print(f"\nYou're out of guesses. \nThe number was {number}. You lose!")

game()       


    