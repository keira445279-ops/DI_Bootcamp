# EXERCISE 1: Converting Lists into Dictionaries
# Key Python Topics:
# Creating dictionaries
# Zip function or dictionary comprehension
# Instructions
# You are given two lists. 
# Convert them into a dictionary where the first list contains the keys and 
# the second list contains the corresponding values.
# Lists:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_values = dict(zip(keys, values))

print (keys_values)


# EXERCISE 2: Cinemax #2
# Key Python Topics:
# Looping through dictionaries
# Conditionals
# Calculations
# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

tickets_cost = 0

while True:
    new_member = input ('What is your name: ')
    
    if new_member =='quit':
        break
    else:
        new_age = int(input('How old are you: '))
        family.update ({new_member : new_age})


for value in family.values():
    if value < 3:
        tickets_cost += 0
    elif 3 <= value <= 12:
        tickets_cost +=10
    elif value > 12:
        tickets_cost +=15

print (family) #check up
print (tickets_cost)


# EXERCIZE 3: Zara
# Key Python Topics:
# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.

# Brand Information:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# Create a dictionary called brand with the provided data.

brand = {'name' : 'Zara', 
         'creation_date' : 1975, 
         'creator_name' : 'Amancio Ortega Gaona', 
         'type_of_clothes' : ('men', 'women', 'children', 'home'),
         'international_competitors': ['Gap', 'H&M', 'Benetton'],
         'number_stores': 7000,
         'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']}}

# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.

brand['number_stores'] = 2
print (brand['number_stores'])

# Print a sentence describing Zara’s clients using the type_of_clothes key.

print ("Zara is the brand which makes product for", ', '.join (brand['type_of_clothes']))

# Add a new key country_creation with the value Spain.

brand.update({'country_creation' : 'Spain'})
print(brand)

# Check if international_competitors exists and, if so, add “Desigual” to the list.

print(brand['international_competitors'])
brand['international_competitors'].append ('Desigual')
print(brand['international_competitors'])

# Delete the creation_date key.

del brand['creation_date']
print (brand)

# Print the last item in international_competitors.

print (brand ['international_competitors'] [-1])

# Print the major colors in the US.

print (brand['major_color']['US'])

# Print the number of keys in the dictionary.

print (len(brand))

# Print all keys of the dictionary.

print (brand.keys())

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. 
# Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = { 'creation_date' : '1975',
                'number_stores' : 7000
}

brand.update(more_on_zara)

print (brand)


# EXERCISE 4: Disney Characters
# Key Python Topics:
# Looping with indexes
# Dictionary creation
# Sorting
# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
# Character List:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

users_chr_to_ind = {item: i for i, item in enumerate(users)}
print (users_chr_to_ind)

# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

users_ind_to_chr = {i: item for i,item in enumerate(users)}
print (users_ind_to_chr)

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users_alp = sorted(users)
users_alp_chr_to_ind = {item: i for i, item in enumerate(users_alp)}
print (users_alp_chr_to_ind)