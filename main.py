MENU = {
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

# user_choice_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")

penny_value = 0.01
nickle_value = 0.05
dime_value = 0.10
quarter_value = 0.25

total_money_collected = 0

machine_active = True

remaining_water = 300
remaining_coffee = 200
remaining_milk = 100

while machine_active:
    user_choice_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice_of_coffee == "report":
        print(f"I have {remaining_water} water, {remaining_milk} milk, {remaining_coffee} coffee left.")

    elif user_choice_of_coffee == "off":
        print("See You Tomorrow, bye!")
        break
    elif user_choice_of_coffee == "espresso":
        if remaining_water > MENU[user_choice_of_coffee]['ingredients']['water'] and remaining_coffee > MENU[user_choice_of_coffee]['ingredients']['coffee']:
            print(f"Your cost is {MENU[user_choice_of_coffee]['cost']}")
            print('I only accept coins, please pay now')
            user_paying_in_pennies = int(input("Pennies: "))
            user_paying_in_dimes = int(input("Dimes: "))
            user_paying_in_nickles = int(input("Nickles: "))
            user_paying_in_quarters = int(input("Quarters: "))
            user_paying_total = (user_paying_in_pennies * penny_value) + (user_paying_in_nickles * nickle_value) + (user_paying_in_quarters * quarter_value) + (user_paying_in_dimes * dime_value)
            print(f"You have entered a total of ${user_paying_total}")

            if user_paying_total == MENU[user_choice_of_coffee]['cost']:
                total_money_collected += user_paying_total
                remaining_water -= MENU[user_choice_of_coffee]['ingredients']['water']
                remaining_coffee -= MENU[user_choice_of_coffee]['ingredients']['coffee']
                print("\nEnjoy your coffee ☕")

            elif user_paying_total > MENU[user_choice_of_coffee]['cost']:
                return_changed = user_paying_total - MENU[user_choice_of_coffee]['cost']
                print(f"Your change is ${return_changed}")
                total_money_collected += user_paying_total - return_changed
                remaining_water -= MENU[user_choice_of_coffee]['ingredients']['water']
                remaining_coffee -= MENU[user_choice_of_coffee]['ingredients']['coffee']
                print("\nEnjoy your coffee ☕")

            elif user_paying_total != MENU[user_choice_of_coffee]['cost']:
                print("Insufficient Funds, your money has been refunded")

        elif remaining_water > MENU[user_choice_of_coffee]['ingredients']['water'] or remaining_coffee > MENU[user_choice_of_coffee]['ingredients']['coffee']:
            print('Not Enough Ingredients')

    elif user_choice_of_coffee == "latte":
        if remaining_water > MENU[user_choice_of_coffee]['ingredients']['water'] and remaining_coffee > MENU[user_choice_of_coffee]['ingredients']['coffee']:
            if remaining_milk > MENU[user_choice_of_coffee]['ingredients']['milk']:
                print(f"Your cost is {MENU[user_choice_of_coffee]['cost']}")
                print('I only accept coins, please pay now')
                user_paying_in_pennies = int(input("Pennies: "))
                user_paying_in_dimes = int(input("Dimes: "))
                user_paying_in_nickles = int(input("Nickles: "))
                user_paying_in_quarters = int(input("Quarters: "))
                user_paying_total = (user_paying_in_pennies * penny_value) + (user_paying_in_nickles * nickle_value) + (user_paying_in_quarters * quarter_value) + (user_paying_in_dimes * dime_value)
                print(f"You have entered a total of ${user_paying_total}")

                if user_paying_total == MENU[user_choice_of_coffee]['cost']:
                    total_money_collected += user_paying_total
                    remaining_water -= MENU[user_choice_of_coffee]['ingredients']['water']
                    remaining_coffee -= MENU[user_choice_of_coffee]['ingredients']['coffee']
                    remaining_milk -= MENU[user_choice_of_coffee]['ingredients']['milk']
                    print("\nEnjoy your coffee ☕")

                elif user_paying_total > MENU[user_choice_of_coffee]['cost']:
                    return_changed = user_paying_total - MENU[user_choice_of_coffee]['cost']
                    print(f"Your change is ${return_changed}")
                    total_money_collected += user_paying_total - return_changed
                    remaining_water -= MENU[user_choice_of_coffee]['ingredients']['water']
                    remaining_coffee -= MENU[user_choice_of_coffee]['ingredients']['coffee']
                    remaining_milk -= MENU[user_choice_of_coffee]['ingredients']['milk']
                    print("\nEnjoy your coffee ☕")

                elif user_paying_total != MENU[user_choice_of_coffee]['cost']:
                    print("Insufficient Funds, your money has been refunded")

        elif remaining_water < MENU[user_choice_of_coffee]['ingredients']['water'] or remaining_coffee < MENU[user_choice_of_coffee]['ingredients']['coffee']:
            print('Not Enough Ingredients')

    elif user_choice_of_coffee == "cappuccino":
        if remaining_water > MENU[user_choice_of_coffee]['ingredients']['water'] and remaining_coffee > MENU[user_choice_of_coffee]['ingredients']['coffee']:
            if remaining_milk > MENU[user_choice_of_coffee]['ingredients']['milk']:
                print(f"Your cost is {MENU[user_choice_of_coffee]['cost']}")
                print('I only accept coins, please pay now')
                user_paying_in_pennies = int(input("Pennies: "))
                user_paying_in_dimes = int(input("Dimes: "))
                user_paying_in_nickles = int(input("Nickles: "))
                user_paying_in_quarters = int(input("Quarters: "))
                user_paying_total = (user_paying_in_pennies * penny_value) + (user_paying_in_nickles * nickle_value) + (user_paying_in_quarters * quarter_value) + (user_paying_in_dimes * dime_value)
                print(f"You have entered a total of ${user_paying_total}")

                if user_paying_total == MENU[user_choice_of_coffee]['cost']:
                    total_money_collected += user_paying_total
                    remaining_water -= MENU[user_choice_of_coffee]['ingredients']['water']
                    remaining_coffee -= MENU[user_choice_of_coffee]['ingredients']['coffee']
                    remaining_milk -= MENU[user_choice_of_coffee]['ingredients']['milk']
                    print("\nEnjoy your coffee ☕")

                elif user_paying_total > MENU[user_choice_of_coffee]['cost']:
                    return_changed = user_paying_total - MENU[user_choice_of_coffee]['cost']
                    print(f"Your change is ${return_changed}")
                    total_money_collected += user_paying_total - return_changed
                    remaining_water -= MENU[user_choice_of_coffee]['ingredients']['water']
                    remaining_coffee -= MENU[user_choice_of_coffee]['ingredients']['coffee']
                    remaining_milk -= MENU[user_choice_of_coffee]['ingredients']['milk']
                    print("\nEnjoy your coffee ☕")

                elif user_paying_total != MENU[user_choice_of_coffee]['cost']:
                    print("Insufficient Funds, your money has been refunded")

        elif remaining_water < MENU[user_choice_of_coffee]['ingredients']['water'] or remaining_coffee > MENU[user_choice_of_coffee]['ingredients']['coffee']:
            print('Not Enough Ingredients')

print(f"We have made a total of ${total_money_collected} today")
