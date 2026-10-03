import art
from random import randint
print(art.logo)
Celebridades = [
{"name" : "Max",
 "followers_counter" : 500,
 "Description": "Musicant"
},
{
    "name" : "Steveen",
    "followers_counter" : 100000,
    "Description" : "Actor"
},
{
    "name" : "Scarlet",
    "followers_counter" : 1570,
    "Description" : "Apresenter" 
},
{
    "name" : "Lebrown James",
    "followers_counter" : 999999,
    "Description" : "Basket"
},
{
    "name" : "Cristiano Ronaldo",
    "followers_counter" : 550000,
    "Description" : "footballer" 
},
]
def GameRunning():
    ShouldContinue = True
    player1 = (Celebridades[randint(0, 4)])
    player2 = (Celebridades[randint(0, 4)])
    score = 0

    while player1 == player2:
        player2 = Celebridades[randint(0, 4)]

    while ShouldContinue: 
        print(f"\nCompare A: {player1['name']} a {player1['Description']},")
        print(art.VS)
        print(f"Compare B: {player2['name']} a {player2['Description']},")
        print(f"Your Score is: {score}")
        response = input("Who has more followers? Type 'A' or 'B':").upper()
        if int(player1['followers_counter']) > int(player2['followers_counter']):
                if response == "A":
                    print("You Win!!")
                    player1 = player2
                    player2 = Celebridades[randint(0, 4)]
                    score += 1
                    while player1 == player2:
                        player2 = Celebridades[randint(0, 4)]
                else:
                    print("\nYou Lose!!")
                    ShouldContinue = False
        elif int(player2["followers_counter"]) > int(player1["followers_counter"]):
            if response == "B":
                print("You Win")
                score += 1
                player1 = player2
                player2 = Celebridades[randint(0, 4)]
                while player1 == player2:
                    player2 = Celebridades[randint(0, 4)]
            else:
                print("\nYou Lose!!")
                ShouldContinue = False
GameRunning()