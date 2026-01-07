from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

while is_on:
    print("What would you like?")
    m = Menu()
    c = CoffeeMaker()
    monmac = MoneyMachine()
    print(m.get_items())
    choice = input()
    if choice == 'off':
        break
    elif choice == 'report':
        c.report()
    else:
        drink = m.find_drink(choice)
        if c.is_resource_sufficient(drink):
            payment = monmac.make_payment(drink.cost)
            c.make_coffee(drink)
