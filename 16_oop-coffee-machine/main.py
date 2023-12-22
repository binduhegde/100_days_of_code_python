'''Read the pdf file to know what each of these classes do'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# here, we're creating objects(money_machine, coffee_maker, menu) 
# from the classes(MoneyMachine, CoffeeMaker, Menu) we imported
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# coffee machine is on
is_on = True


while is_on:
    options = menu.get_items() #“latte/espresso/cappuccino”
    choice = input(f"What would you like? ({options}): ")
    
    # breaks out of the loop if the input is 'off'
    if choice == 'off':
        is_on = False
    
    # prints the report
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    
    else:
        # drink returns a menu item if it exists else None
        drink = menu.find_drink(choice)
        # to see if we have enough resource
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        # to see if the payment is successful
        if not money_machine.make_payment(drink.cost):
            continue
        # goes ahead and make the coffee if there's enough resources and the payment is successful
        coffee_maker.make_coffee(drink)
    