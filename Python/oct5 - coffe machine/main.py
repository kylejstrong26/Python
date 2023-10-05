# Coffee machine - start to order! #

# Menu
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Starting quantities 
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# Check for sufficient resources in the coffee machine
def sufficient_resources(order):
    if (MENU[order]['ingredients']['water'] > resources['water'] or MENU[order]['ingredients']['milk'] > resources['milk']
            or MENU[order]['ingredients']['coffee'] > resources['coffee']):
        print("Insufficient ingredients, please come back later after we refill our machine...")
        return False
    else:
        return True

# Process the order
def accounting(order,resources):
    print("Please Insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*(0.25) + dimes*(0.1) + nickles*(0.05) + pennies*(0.01)
    if MENU[order]['cost'] > total:
        print("Insufficient funds, there's an ATM in the corner.")
        return 0
    else:
        resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
        change = total - MENU[order]['cost']
        print(f"Your change is ${change}")
        print(f"Here is your {order} ☕️. Enjoy!")
        return MENU[order]['cost']

# Main operations
is_on = True
while is_on:
    # turn off = "off", report = "report"
    order = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        print("Turning Off...")
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffe: {resources['coffee']}")
        print(f"Money: ${profit}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        ingredients = sufficient_resources(order)
        if not ingredients:
            is_on = False
        else:
            profit += accounting(order, resources)

