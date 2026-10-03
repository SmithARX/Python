import random
from art import logo, VS
from gameData import Celebridades

def format_data(account):
    """Takes the account data and return the printable format."""
    account_name = account["name"]
    account_desc = account["Description"]
    return f"{account_name} a {account_desc}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and return if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_countinue = True
account_b = random.choice(Celebridades)
    
while game_should_countinue:
    account_a = account_b
    account_b = random.choice(Celebridades)

    if account_a == account_b:
        account_b = random.choice(Celebridades)

    print(f"Compare A: {format_data(account_a)}.")
    print(VS)
    print(f"Agaist B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)
    
    a_follower_account = account_a["followers_counter"]
    b_follower_account = account_b["followers_counter"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}.")
        game_should_countinue = False


