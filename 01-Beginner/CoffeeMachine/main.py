from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
machine_maker = CoffeeMaker()
machine_cashier = MoneyMachine()

is_on = True
while is_on:
    options = machine_menu.get_items()
    user_order = input(f"What would you like? ({options}): ").lower()

    if user_order == "off":
        is_on = False

    elif user_order == "report":
        machine_maker.report()
        machine_cashier.report()

    elif machine_menu.find_drink(user_order):
        user_drink = machine_menu.find_drink(user_order)
        if machine_maker.is_resource_sufficient(user_drink):
            if machine_cashier.make_payment(user_drink.cost):
                machine_maker.make_coffee(user_drink)
