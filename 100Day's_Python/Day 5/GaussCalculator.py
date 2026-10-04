#Gauss Chalenger day 5
print("Gauss Calculator")
sum = 0
n = int(input("Vamos calcular de qual numero? "))

for i in range(1, n+1):
    sum += i 

print(sum)
for number in range(1, 101):
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)