from menu import MENU, resources as rs

machine_power_on = True


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


def order_execution(order, resources_in_machine, money):

    water_rss = resources_in_machine['water']
    milk_rss = resources_in_machine['milk']
    coffee_rss = resources_in_machine['coffee']

    if order == 'espresso':
        milk = 0
        water, coffee, price = order_rq(order)
    else:
        water, coffee, milk, price = order_rq(order)

    if water_rss < water:
        print('Sorry, not enough water')
    elif coffee_rss < coffee:
        print('Sorry, not enough coffee')
    elif milk_rss < milk:
        print('Sorry, not enough milk')
    else:
        remain_water = water_rss - water
        remain_coffee = coffee_rss - coffee
        remain_milk = milk_rss - milk

    if money < price:
        print(f'Sorry, tha\'s not enough money. Money refunded.')
    else:
        if money > price:
            change = money - price
            print(f'Here is your ${change} in change.')
        print(f'Here is your {order}. Enjoy')

    return money, remain_water, remain_coffee, remain_milk



while machine_power_on:
    money_in_machine = 0

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice != 'report':
        print('Please insert coins.')
        quarters = int(input('How many quarters?: ')) * 0.25
        dimes = int(input('How many quarters?: ')) * 0.10
        nickles = int(input('How many quarters?: ')) * 0.5
        pennies = int(input('How many quarters?: ')) * 0.01

        user_money = quarters + dimes + nickles + pennies

        money_in_machine += order_execution(user_choice, rs, user_money)



    else:
        pass


    var = order_rq(user_choice)
    print(var)
