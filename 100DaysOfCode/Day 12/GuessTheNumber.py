import random
from art import logo

num = random.choice(range(1, 100))
print(logo)
print("Welcome to the Number Guess Game")
print("i'm Thinking of a number between 1 and 100")
dificulty = input("Choose a difficulty \"easy\" or \"hard\": ")
life = 5

if dificulty == "easy":
    life = 10

game = True
while game:
    print(f"You Have {life} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    life -= 1

    if guess < num:
        print("too low")
        print("guess again")
        print("\n" * 5)
    elif guess > num : 
        print("too high")
        print("guess again")
        print("\n" * 5)
    elif guess == num:
        print("You Win")
        game = False

    if life <= 0:
        print("You Lose")
        game = False
