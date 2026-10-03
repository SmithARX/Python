import Main
askAgain = True
money = 0

while askAgain:
    todo = input("What would you like? (espresso/latte/cappuccino):​").lower()
    if todo == "off":
        askAgain = False

    elif todo == "report":
        print(f"Water: {Main.resources['water']}ml")
        print(f"Milk: {Main.resources['milk']}ml")
        print(f"Coffee: {Main.resources['coffee']}g")
        print(f"Money: ${money}")


    elif todo in Main.MENU :
        drink = Main.MENU[todo]
        if Main.is_resource_sufficient(drink['ingredients']):
            price = drink['cost']
            money += price
            Main.remove_quantiy(drink)
            print(f"Here is your {todo}. Enjoy")
    else:
        print("invalid option. Please try again.")



