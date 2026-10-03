from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(users_guess, actual_answer):
    """Checks answer against guess, return the number of turns remaning."""
    if users_guess > actual_answer: 
        print("Too high.")
        return turns - 1
    elif users_guess < actual_answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You Got it! The answer was{actual_answer}")

def set_dificulty():
    level = input("Chose a dificulty. Type \"easy\" or \"hard\": ")     
    if level  == "easy": 
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("i'm Thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_dificulty()
    guess = 0
    while guess != answer: 
        print(f"You Have {turns} attempts remaning to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

