from menu import MENU, resources as rs


def order_rq(info):
    if info == 'espresso':
        water = MENU[info]['ingredients']['water']
        coffee = MENU[info]['ingredients']['coffee']
        price = MENU[info]['cost']
        return water, coffee, price
    elif info == 'latte' or info == 'cappuccino':
        water = MENU[info]['ingredients']['water']
        coffee = MENU[info]['ingredients']['coffee']
        milk = MENU[info]['ingredients']['milk']
        price = MENU[info]['cost']
        return water, coffee, milk, price


def order_check(order, rss):
    water_rss = rss['water']
    milk_rss = rss['milk']
    coffee_rss = rss['coffee']

    if order == 'espresso':
        milk = 0
        water, coffee, price = order_rq(order)
    else:
        water, coffee, milk, price = order_rq(order)

    if water_rss < water:
        print('Sorry, not enough water. Money refunded.')
        return False
    elif coffee_rss < coffee:
        print('Sorry, not enough coffee. Money refunded.')
        return False
    elif milk_rss < milk:
        print('Sorry, not enough milk. Money refunded.')
        return False
    else:
        remain_water = water_rss - water
        remain_coffee = coffee_rss - coffee
        remain_milk = milk_rss - milk

        return remain_water, remain_coffee, remain_milk


def order_execution(order, money):
    if money < MENU[order]['cost']:
        print(f'Sorry, that\'s not enough money. Money refunded.')
    else:
        if money > MENU[order]['cost']:
            change = round(money - MENU[order]['cost'], 2)
            print(f'Here is your ${change} in change.')
        print(f'Here is your {order}. Enjoy!')

    return MENU[order]['cost']


def coffee_machine():
    machine_power_on = True
    total_money = 0
    while machine_power_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == 'power off':
            machine_power_on = False
            print('Turning off...')
        elif user_choice == 'report':
            print(f"Water: {rs['water']}ml\n"
                  f"Milk: {rs['milk']}ml\n"
                  f"Coffee: {rs['coffee']}g\n"
                  f"Money: ${total_money}")
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':

            if order_check(user_choice, rs):
                print('Please insert coins.')
                quarters = float(input('How many quarters?: ')) * 0.25
                dimes = float(input('How many dimes?: ')) * 0.10
                nickles = float(input('How many nickles?: ')) * 0.05
                pennies = float(input('How many pennies?: ')) * 0.01

                user_money = quarters + dimes + nickles + pennies

                total_money += order_execution(user_choice, user_money)
                rs['water'], rs['coffee'], rs['milk'] = order_check(user_choice, rs)
        else:
            print('Invalid command. Please try again.')


coffee_machine()
