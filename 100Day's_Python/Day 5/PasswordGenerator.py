import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbols = ["#", "!", "$", "@", "~"]

numLet = int(input("How many letter you want?\n "))
numNum = int(input("How many number you want?\n " ))
numSim = int(input("How many simbols you want?\n "))

#jeito simples de fazer
# password = ""
# for let in range(0 , numLet):
#     password += random.choice(letter)

# for let in range(0 , numNum):
#     password += random.choice(number)

# for let in range(0 , numSim):
#     password += random.choice(simbols)

# print(password)

#jeito um pouco mais complexo
password_list = []
for let in range(0 , numLet):
    password_list.append(random.choice(letter))

for let in range(0 , numNum):
    password_list.append(random.choice(number))

for let in range(0 , numSim):
    password_list.append(random.choice(simbols))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"your password is: {password}")