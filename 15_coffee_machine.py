menu = {
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

profit = 0

# takes a valif integer input. parameter is the prompt message
def take_int_inp(message):
    while True:
        inp = input(message)
        try:
            inp = int(inp)
            return inp
        except ValueError:
            print("Please enter a valid number")

# prints the report whenever called
def print_report():
    for key, value in resources.items():
        print(f"{key} : {value}")
    print(f"profit : ${profit}")

# goes throufh each ingredient needed and returns false if it's not enough
def is_resource_enough(item):
    ingredients = menu[item]['ingredients']
    available = resources
    for key, value in ingredients.items():
        if available[key] < value:
            return False
    return True 

# take coins from input and outputs the total amount in  $
def take_coins():
    print("Please insert coins.")
    denominations = {'quarters': 0.25, 'dimes':0.1, 'nickles':0.05, 'pennies':0.01}
    money_received = [take_int_inp(f"How many {key}?: ")*value for key, value in denominations.items()]
    return sum(money_received)

# outputs the change the store has to give. 
# it can be negative also in which case it means that the user didn't pay enough
def get_change(item):
    money = take_coins()
    cost = menu[item]['cost']
    return money - cost

# checks if resources are enough, and if the money received is enough
# if all of it is enough, returns true, else False
def can_prepare_order(item):
    if not is_resource_enough(item):
        print("Sorry! there are't enough resources.")
        return False
    change = get_change(item)
    if change < 0:
        print("Sorry! The money isn't sufficient.")
        return False
    elif change > 0: # doesn't get executed if customer paid exaactly what it costs
        print(f"Here is ${change:.2f} in change.")
    return True

# after the order is given to the customer, this deducts how much we used to make that order from the resources we have
def deduct_resources(item):
    needed = menu[item]['ingredients']
    for key, value in needed.items():
        resources[key] -= value
    return resources

# adds profit to the profit variable
def add_profit(item):
    global profit
    profit += menu[item]['cost']

# does the whole execution of the program. keeps taking orders till the order input is 'off'. In this case, the function breaks out of the while loop and stops
def take_order():
    while True:
        order = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        
        if order in ['espresso', 'latte', 'cappuccino']:
            if can_prepare_order(order):
                print("Here is your espresso ☕️. Enjoy!")
                deduct_resources(order)
                add_profit(order)
        elif order == 'report':
            print_report()
        elif order == 'off':
            return
        
        # gets executed if the customer puts invalid ipnut 
        else: print("Please enter a valid order.")
take_order()