from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

machineOn = True
while machineOn:
    print(f'---- MENU:{menu.get_items()}  MACHINE OPTIONS:|report|off| ----')
    userAction = input("What would you like?: ")

    if userAction == "off":
        print("Goodbye.")
        machineOn = False
    elif userAction == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(userAction)
        if drink != "None":
            if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                maker.make_coffee(drink)
