import art
from random import randint

print(art.logo)

Celebridades = [
    {"name": "Max", "followers_counter": 500, "Description": "Musicant"},
    {"name": "Steveen", "followers_counter": 100000, "Description": "Actor"},
    {"name": "Scarlet", "followers_counter": 1570, "Description": "Apresenter"},
    {"name": "Lebrown James", "followers_counter": 999999, "Description": "Basket"},
    {"name": "Cristiano Ronaldo", "followers_counter": 550000, "Description": "footballer"}
]

def GameRunning():
    ShouldContinue = True
    player1 = Celebridades[randint(0, 4)]
    player2 = Celebridades[randint(0, 4)]
    score = 0

    while player1 == player2:
        player2 = Celebridades[randint(0, 4)]

    while ShouldContinue: 
        print(f"\nCompare A: {player1['name']} a {player1['Description']},")
        print(art.VS)
        print(f"Compare B: {player2['name']} a {player2['Description']},")
        print(f"Your Score is: {score}")
        
        response = input("Who has more followers? Type 'A' or 'B': ").upper()

        # 1. Descobre qual é a resposta certa ANTES
        if player1['followers_counter'] > player2['followers_counter']:
            correct_answer = "A"
        else:
            correct_answer = "B"

        # 2. Faz uma ÚNICA verificação para Win/Lose
        if response == correct_answer:
            score += 1
            print(f"\nYou Win!! Current score: {score}")
            
            # Prepara a próxima rodada
            player1 = player2
            player2 = Celebridades[randint(0, 4)]
            while player1 == player2:
                player2 = Celebridades[randint(0, 4)]
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            ShouldContinue = False

GameRunning()