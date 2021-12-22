MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

#TODO2 print report of current resource value
def report():
    print(f"Water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"Water: {resources['coffee']}gr")
    print(f"Money: ${money}")

working = True
while working:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        report()
    #TODO1 make a turn off button by typing "off"
    elif user_choice == "off":
        working = False
    #TODO3 check if resources are sufficient 
    elif user_choice =="espresso" or "latte" or "cappuccino" :
        sufficient_resources = True
        for key in resources:
            if resources[key] < MENU[user_choice]["ingredients"][key]:
                print(f"Sorry there is not enough {key}.")
                sufficient_resources = False
        if sufficient_resources:
            # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            total_coins = 0
            quarters = int(input("how many quarters?: ")) * 0.25
            dimes = int(input("how many dimes?: ")) * 0.1
            nickles = int(input("how many nickles?: ")) * 0.05
            pennies = int(input("how many pennies?: ")) * 0.01
            total_coins = quarters + dimes + nickles + pennies
            if total_coins < MENU[user_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${total_coins - MENU[user_choice]['cost'] } dollars in change.")
                for key in resources:
                    resources[key] -= MENU[user_choice]["ingredients"][key]
                money += MENU[user_choice]["cost"]
                print(f"Here is your {user_choice}. Enjoy!")