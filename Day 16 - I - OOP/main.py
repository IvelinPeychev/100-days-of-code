import coffee_maker
import menu
import money_machine

# # ---------------------------------------------------------------- Turtle
# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('DarkGreen')
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# my_screen.exitonclick()

# # ---------------------------------------------------------------- Pretty Table
#
# table = prettytable.PrettyTable()
#
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type',['Electric', 'Water', 'Fire'])
#
# # attribute manipulation
# table.align = 'l'
#
# print(table)

# ---------------------------------------------------------------- Coffee machine OOP


coffee_machine = coffee_maker.CoffeeMaker()
menu = menu.Menu()
money_machine = money_machine.MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} : ")
    if choice == 'report':
        coffee_machine.report()
        money_machine.report()
    elif choice == 'turn off':
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            break
        elif coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
