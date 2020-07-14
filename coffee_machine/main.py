from coffee_machine import CoffeeMachine
import json

config_location=input("Enter the location of the config file:\n")
with open(config_location,'r') as f:
    config=json.loads(f.read())
print('Getting your coffee machine ready...')

#creating the coffee machine with the given input configurations
outlets = config['machine']['outlets']['count_n']
ingredients_list = config['machine']['total_items_quantity']
beverage_list = config['machine']['beverages']
coffee_machine = CoffeeMachine()
coffee_machine.outlet=outlets
for name,quantity in ingredients_list.items():
    coffee_machine.addIngredient(name,quantity)
for name,recipe in beverage_list.items():
    coffee_machine.addBeverage(name,recipe)

#working of the coffee machine - user is allowed to choose from the following options
# 1.Show Menu - shows the list of beverages in the coffee machine
# 2.Show Inventory - shows the list of ingredients and their inventory in the coffe machine at any point in time
# 3.Refill Ingredient - allows for refilling/filling an ingredient into the coffee machine
# 4.Quit - option to exit the program
while(1):
    runner=0
    print('1. Show Menu')
    print('2. Show Inventory')
    print('3. Refill Ingredient')
    print('4. Quit')
    cmd=int(input('Input: '))
    if cmd == 1:
        orders=[]
        #taking orders till the outlet is available.
        #if orders are less than the number of outlets available, user needs to press 'q'
        while(runner<=coffee_machine.outlet):
            print('Enter q to complete orders')
            coffee_machine.getMenu()
            menu=input('Input: ')
            if(menu == 'q'):
                break
            else:
                orders.append(menu)
            runner+=1
        for order in orders:
            print(coffee_machine.makeBeverage(order))

    elif cmd == 2:
        coffee_machine.getStock()
    elif cmd == 3:
        ingredient=input('Enter ingredient name: ')
        fill_value=int(input('Enter ingredient quantity: '))
        coffee_machine.fillIngredient(ingredient,fill_value)
    elif cmd == 4:
        break
