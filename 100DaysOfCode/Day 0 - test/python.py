import random
#imports behind 
# print('Welcome to the Tip Calculator')
# total = float(input('What as the total of the bill? '))
# tip = int(input('How much tip would you like to give? 10, 12, 15? '))
# peoples = int(input('How many people to split the bill? '))
# result = float(((tip / 100 * total) + total) / peoples)
# print(f"Each person should pay ${round(result , 2)}")

# Number = float(input("Digit a number: "))
# Number_per_two = Number/2
# isFloat = Number_per_two % 2
# if isFloat == 0 :
#     print("This number is even")
# else: 
#     print("This number is odd")

# print("Welcome to the Python Pizza Deliveris!!")
# bill = 0
# size = input("What Size of pizza do you want? [S] [M] [L]: ")
# peperoni = input("Do you want Peperoni? y ou n: ")
# extra_cheese = input("Do you want extra chesee? y or n: ")

# if size == "s":
#     bill = 15
# elif size == "m":
#     bill = 20
# elif size == "l":
#     bill = 25
# if peperoni == "y":
#     if size == "s":
#         bill += 2
#     else: 
#         bill += 3 
# if extra_cheese == "y":
#     bill += 1

# print(f"your final bill is ${bill}.")

#Day 5
# student_score = [100, 120, 156, 265, 129, 205, 97, 78, 254, 158, 301, 260, 222, 154, 116, 117, 185, 214, 300]
# finalScore = 0

# for score in student_score: 
#     if score > finalScore:
#         finalScore = score
        
# print(finalScore)

#Gauss Chalenger day 5
# print("Gauss Calculator")
# sum = 0
# n = int(input("Vamos calcular de qual numero? "))

# for i in range(1, n+1):
#     sum += i 

# print(sum)
# for number in range(1, 101):
    
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# simbols = ["#", "!", "$", "@", "~"]

# numLet = int(input("How many letter you want?\n "))
# numNum = int(input("How many number you want?\n " ))
# numSim = int(input("How many simbols you want?\n "))

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
# password_list = []
# for let in range(0 , numLet):
#     password_list.append(random.choice(letter))

# for let in range(0 , numNum):
#     password_list.append(random.choice(number))

# for let in range(0 , numSim):
#     password_list.append(random.choice(simbols))

# random.shuffle(password_list)

# password = ""

# for char in password_list:
#     password += char

# print(f"your password is: {password}")

# Word_List = ["advogado", "banana", "computador"]
# lives = 6
# stages = ["1", "2", "3", "4", "5", "6"]

# Word = random.choice(Word_List)
# print(Word)

# placeholder = ""
# word_Leng = len(Word)
# for position in range(word_Leng):
#     placeholder += "_"
# print (placeholder)

# correct_letter = []
# game_over = False
# while not game_over:
#     print(f"******************You have {lives}/6 Lives remaning*******************")
#     guess = input("Escolha uma letra: ").lower()

#     if guess in correct_letter:
#         print(f"You already type this letter{guess}.")
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("*************************** You lose ************************************")
#     display = ""

#     for letter in Word:
#         if letter == guess:
#             display += letter
#             correct_letter.append(letter)
#         elif letter in correct_letter:
#             display += letter
#         else:
#             display += "_"
    
#     print(display)          
    
#     if guess not in Word:
#         print(f"Your guessed {guess}, that's not in the word. You lose a life")
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print(f"*************************** It was{Word}, You lose ************************************")
    
  
              
#     if "_" not in display:
#         game_over = True
#         print("*************************** You Win ************************************")
#Day 8
# def greet_with_name(name):
#     print(f"hello {name}")


# greet_with_name("eric")

    

# def calculate_love_score(name1, name2):
#     letter_name1 = list(name1)
#     letter_name2 = list(name2)
#     confirm1 = letter_name1.count(["t", "r", "u", "e", "l", "o", "v", "e"])
#     print(confirm1)
    
# calculate_love_score("ANGELA YU", "JACK BAUER")
# Day 9 
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(original_text, shift_amount):
#     cipher_text = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) 
#         cipher_text += alphabet[shifted_position]

#     print(f"here is the encode result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)

# def caeser(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount  *= -1
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#     print(f"here is the encoded result: {output_text}")

# should_Continue = True

# while should_Continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your mensage:\n") .lower()
#     shift = int(input("Type the shift number:\n "))

#     caeser(text, shift, direction)

#     restart =input("Type 'yes' if you want to go again. Otherwise, type no.\n").lower()
#     if restart == "no":
#         should_Continue = False
#         print("Good Bye")
    


# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0

#     max(bidding_dictionary)

#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder

#     print(f"The winner is {winner} with a bid of ${highest_bid}.")

# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What's your name: ")
#     price = int(input("What is your bid: $"))
#     bids[name] = price
#     Should_Continue = input("more bids yes/no:\n").lower
#     if Should_Continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif Should_Continue == "yes":
#         print("\n" * 20)


year = int(input("What year would you like to verify? "))
isLeap = False
if (year / 4):
    year = ...
elif(year / 100):
    isLeap = False
elif (year / 400):
    isLeap = True

print(isLeap)