from random import choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
isNot21 = True;

def initialCards():
    result = 0
    C1 = choice(cards)
    C2 = choice(cards)
    C1 + C2 == result
    return int(C1), int(C2)

while isNot21:
    print("BlackJack")
    player = initialCards()
    bot = initialCards()
    print(f"Player Cards: {player}")
    print(f"Bot Cards: {bot}")
    print(player)
    totalplayer = sum(player)
    totalBot = sum(bot)
    answer = input("You want one more card or stop here? [y or n]: ")
    if answer == "n":
        if totalplayer < 21:
            if totalplayer > totalBot :
                print("You win!!")
            else:
                print("You Lose!!")
                isNot21 = False
        else: print("You Lose!!")
        isNot21 = False
    else:
        totalplayer + choice(cards)


