import random
choose = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
PcChoose = random.randint(0, 2)
print(PcChoose)
if choose == 0:
    if PcChoose == 0:
        print("Draw!")
    elif PcChoose == 1:
        print("You Lose!!")
    else:
        print("You Win!!!")
elif choose == 1:
    if PcChoose == 0:
        print("You Win!!!")
    elif PcChoose == 1:
        print("Draw!")
    else:
        print("You lose!!")
elif choose == 2:
    if PcChoose == 0:
        print("You Lose!!")
    elif PcChoose == 1:
        print("You Win!!!")
    else:
        print("Draw!")
else:
    print("number invalid")