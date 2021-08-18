MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. to print a report of all the resources
def report():
    print(f"Water left: {resources['water']}")
    print(f"Milk left: {resources['milk']}")
    print(f"Coffee left: {resources['coffee']}")


# TODO: 2. to calculate the price of a coffee
def calculate(x):
    coffee_name = MENU[x]
    print(f"Cost of {x} is {coffee_name['cost']}")
    # print(coffee_name['cost'])
    while True:
        try:
            one_coin = int(input("Enter the no. of 1 rupee coins: "))
            two_coin = int(input("Enter the no. of 2 rupees coins: "))
            five_coin = int(input("Enter the no. of 5 rupees coins: "))
            ten_coin = int(input("Enter the no. of 10 rupees coins: "))
            break
        except ValueError:
            print("Not a valid input try, again")
    total = one_coin + two_coin * 2 + five_coin * 5 + ten_coin * 10
    # print(total)
    if total >= coffee_name['cost']:
        change = total - coffee_name['cost']
        print(" ")
        print("Enjoy your hot coffee ☕ ")
        print(f"Here is your change: {change}\n")
        update_resources(x)
    else:
        print("Sorry, not enough coins")
    return


# TODO: 3. to check if there are sufficient resources in the coffee machine
def check_resource(x):
    coffee_ing = MENU[x]['ingredients']
    if coffee_ing['water'] <= resources['water'] and coffee_ing['coffee'] <= resources['coffee']:
        if x != 'espresso':
            return coffee_ing['milk'] <= resources['milk']
        else:
            return True
    else:
        print("Sorry we are short of", end=" ")
        if coffee_ing['water'] > resources['water']:
            print("water", end=", ")
        if x != 'espresso':
            if coffee_ing['milk'] > resources['milk']:
                print("milk", end=", ")
        if coffee_ing['coffee'] > resources['coffee']:
            print("coffee")
        return False


# TODO: 4. to update the resources
def update_resources(x):
    coffee_ing = MENU[x]['ingredients']
    resources['water'] -= coffee_ing['water']
    resources['coffee'] -= coffee_ing['coffee']
    if x != 'espresso':
        resources['milk'] -= coffee_ing['milk']


def main():
    coffee = input("""Which coffee you want, espresso or latte or cappuccino or do you want to print a 'report'? """)
    while coffee != "espresso" and coffee != 'latte' and coffee != 'cappuccino' and coffee != 'report':
        print("You entered the wrong choice")
        coffee = input("Enter again: ")
    if coffee == 'report':
        report()
        return 'report'
    if coffee == "espresso" or coffee == 'latte' or coffee == 'cappuccino':
        if check_resource(coffee):
            calculate(coffee)


choice = input("Do you want a coffee?(y/n): ")
while choice != 'y' and choice != 'n':
    choice = input("Enter a valid choice: ")
while choice == 'y':
    val = main()
    if val == 'report':
        continue
    choice = input("Do you want a coffee?(y/n): ")
    while choice != 'y' and choice != 'n':
        choice = input("Enter a valid choice: ")
print("Bye Bye")
