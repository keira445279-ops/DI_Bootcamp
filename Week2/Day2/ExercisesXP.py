#EXERCISE 1: Favorite Numbers
#Key Python Topics:
#Sets
# Adding/removing items in a set
# Set concatenation (using union)
# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.

my_fev_numbers = {17,13,25,37,53}
my_fev_numbers.add (107)
my_fev_numbers.add (97)
print (my_fev_numbers)

# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.

friend_fev_numbers = {16, 54, 32, 105, 37}

# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.

all_fav_numbers = my_fev_numbers.union(friend_fev_numbers)
print (all_fav_numbers)

# Note: Sets are unordered collections, so ensure no duplicate numbers are added.


# EXERCISE 2: Tuple
# Key Python Topics:
# Tuples (immutability)
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. 
# Think about why you can’t add more integers to a tuple.

my_tuple = (32, 45, 67, 29, 180)
my_tuple.add (60)
print (my_tuple) # I can`t add more integers to the tuple, because it cannot be changed after creation


# EXRCISE 3: List Manipulation
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove "Banana" from the list.
basket.remove ("Banana")
print (basket)

# Remove "Blueberries" from the list.
basket.remove ("Blueberries")
print (basket)

# Add "Kiwi" to the end of the list.
basket.append ("Kiwi")
print (basket)

# Add "Apples" to the beginning of the list.
basket.insert (0, "Apples")
print (basket)

# Count how many times "Apples" appear in the list.
count_apples = basket.count ("Apples")
print (count_apples)

# Empty the list.
basket.clear()
count_apples

# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print (basket [-1])


# EXERCISE 4: Floats
# Key Python Topics:
# Lists
# Floats and integers
# Range generation
# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

number_list = []

for i in range (1,11):
    number_list.append(i/2)

print (number_list)


# EXERCISE 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.

for i in range (1,21):
    print (i)

# Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range (1,21):
    if i % 2 == 0:
        print (i)


# EXERCISE 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals
# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

while True:
    user_name = input ('Please, enter your name: ')
    if not user_name. isdigit() and len (user_name) >= 3:
        print ('Thank you')
        break
    else:
        print ('Invalid input. Try again')



# EXERCISE 7: Favorite Fruits
# Key Python Topics:
# Input/output
# Strings and lists
# Conditionals
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).

user_fav_fruit = input ('What are your favorite fruites. Please, enter several fruites: ')

# Store these fruits in a list.

fruits = [user_fav_fruit]

# Ask the user to input the name of any fruit.

any_fruit = input ('Please, type any fruit from your list: ')

# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

if any_fruit in fruits:
     print ("You chose one of your favorite fruits! Enjoy!")
else:
    print ("You chose a new fruit. I hope you enjoy it!")


# EXERCISE 8: Pizza Toppings
# Key Python Topics:
# Loops
# Lists
# String formatting
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

all_toppings = []

while True:
    topping = input ('Add a toping to your pizza: ')

    if topping.lower() == 'quit':
        break
    else:
        print (f'Adding {topping} to your pizza.')
        all_toppings.append(topping)

final_price = 10 + len(all_toppings)*2.5

print (f'Your toppings are: {', '.join(all_toppings)} and the final price of your pizza is {final_price}$')


# EXERCISE 9: Cinemax Tickets
# Key Python Topics:
# Conditionals
# Lists
# Loops

# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

all_family_members = []
tickets_cost = 0

while True:
    
    family_member = input ('What kind of family member you are (mother, father, daughter, son, etc.): ')
    if family_member == 'quit':
        break

    all_family_members.append(family_member)
    member_age = int(input(f'{family_member} what is your age: '))
    
    if member_age <3:
        tickets_cost += 0
    elif 3 <= member_age <= 12:
        tickets_cost += 10
    elif member_age > 12:
        tickets_cost += 15

print (f'The total ticket cost is {tickets_cost}$')

# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

allowed_teenagers = []

while True:
    
    teenager_name = input ('What is your name: ')
    if teenager_name == 'quit':
        break

    teenager_age = int(input(f'{teenager_name} what is your age: '))
    
    if 16 <= teenager_age <= 21:
        allowed_teenagers.append(teenager_name)

print (allowed_teenagers)