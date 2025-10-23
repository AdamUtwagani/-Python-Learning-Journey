# Coffee Machine Program

# Initial resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

# Menu with ingredients and cost
menu = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

# Coin values
coin_values = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def is_resource_sufficient(drink):
    for item in menu[drink]["ingredients"]:
        if resources[item] < menu[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = 0
    for coin in coin_values:
        count = int(input(f"How many {coin}? "))
        total += count * coin_values[coin]
    return total

def is_transaction_successful(payment, cost):
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment > cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
    resources["money"] += cost
    return True

def make_coffee(drink):
    for item in menu[drink]["ingredients"]:
        resources[item] -= menu[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")

# Main loop
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print_report()
    elif choice in menu:
        if is_resource_sufficient(choice):
            payment = process_coins()
            if is_transaction_successful(payment, menu[choice]["cost"]):
                make_coffee(choice)
    else:
        print("Invalid input. Please choose from espresso, latte, cappuccino.")
