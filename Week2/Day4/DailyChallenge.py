# Daily Challenge: Coffee Shop Menu Manager
# You were hired to help a small coffee shop manage their product menu using Python.

# Write a program that:
# 1. Stores the coffee shop menu in memory
# 2. Lets the user:
# Create a new item
# Read (view) all items
# Update an item’s price
# Delete an item
# Exit

# Your program must be organized with functions.
# Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.

# 1. DATA  STRUCTURE
# We will represent the menu using a dictionary called menu.

##### The key is the drink name (string)
##### The value is the price (float)
# Example starting data (you MUST start with this so tests are consistent):

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

# menu = {}

# 2. REQUIRED FUNCTIONS
# You must implement the following functions.

# a) show_menu(menu_dict)
# Input: the dictionary
# Output: prints all items in the format drink - price₪
# If the menu is empty, print: "The menu is empty."
# Example:

# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
# This function only prints. It does not return anything.

def show_menu(menu):
    for key, value in menu.items():
        if menu:
            print (f'{key} - {value} NIS')
    if menu == {}:
        print ('The menu is empty')



# b) add_item(menu_dict)
# Ask the user for:
# drink name
# price
# Add it to the dictionary.
# If the drink already exists, print "Item already exists!" and do not change the price.
# Example interaction:

# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
# This function mutates the dictionary. It does not return anything.

def add_item(menu):
    user_drink_name = input ('Enter new drink name: ')
    user_price = float(input('Enter price: '))
    if user_drink_name not in menu.keys():
        menu.update({user_drink_name : user_price})
        print (f'"{user_drink_name}" added')
    else:
        print ('Item already exists!')

# c) update_price(menu_dict)
# Ask the user which drink they want to update.
# If it exists:
# ask for the new price
# update it
# print: "Price updated!"
# If it doesn’t exist:
# print: "Item not found."
# + Validation: Don’t allow negative prices. If the user enters -5, print "Invalid price." and don’t change anything.

def update_price(menu):
    user_drink_update = input('Which drink do you want to update: ')
    if user_drink_update in menu:
        while True:
            user_price_update = float(input('Enter NEW price: '))
            if user_price_update < 0:
                print ('Invalid price')
            else:
                menu.update({user_drink_update : user_price_update})
                print('Price updated!')
                break
    else:
        print('Item not found.')

# d) delete_item(menu_dict)
# Ask the user which drink to remove.
# If it exists:
# delete it from the dict
# print: "Item deleted."
# Otherwise:
# print: "Item not found."

def delete_item(menu):
    user_drink_remove = input('Which drink would you like to remove: ')
    if user_drink_remove in menu:
        del menu[user_drink_remove]
        print('Item deleted')
    else:
        print('Item not found')

# 2. Search function:
# Add a function search_item(menu_dict) that asks for a drink name and:
# prints the price if found
# else prints "Not in the menu."
# Then add it as option 6 in the menu.

def search_item(menu):
    drink_name = input('Type the name of the drink: ')
    if drink_name in menu:
        print (f'{menu[drink_name]} NIS')
    else:
        print('Not in the menu')

# e) show_options()
# Prints the main menu of actions for the user:
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Search item
# 6. Exit
# Only prints. Doesn’t return anything.

def show_option():
    print('What would you like to do?')
    print('1. Show menu')
    print('2. Add item')
    print('3. Update price')
    print('4. Delete item')
    print('5. Search item')
    print('6. Exit')

# f) run_coffee_shop()
# This is the main controller of the program.
# Behavior:
# Keep running in a loop.
# Show options.
# Ask the user to choose (1-5).
# Depending on the choice, call the correct function.

# Rules:
# Invalid choice → print "Invalid choice, try again."
# Choice 5 stops the loop and prints "Goodbye!"

def run_coffee_shop():
    option_choice_count = 0

    while True:
       
        show_option()
        
        print(option_choice_count) #check up

        user_option_choice = int(input('Print the number of option, that you would like to choose (from 1 to 6): '))
        if user_option_choice == 1:
            show_menu(menu)
            option_choice_count +=1
        elif user_option_choice == 2:
            add_item(menu)
            option_choice_count +=1
        elif user_option_choice == 3:
            update_price(menu)
            option_choice_count +=1
        elif user_option_choice == 4:
            delete_item(menu)
            option_choice_count +=1
        elif user_option_choice == 5:
            search_item(menu)
            option_choice_count +=1
        elif user_option_choice == 6:
            print('You\'ve decided to exit. See you next time.')
            break
        elif user_option_choice > 6:
            print('Invalid choice, try again.')
            option_choice_count +=1
            continue
        if option_choice_count >= 5:
            print('Goobuy!')
            break

run_coffee_shop()




        