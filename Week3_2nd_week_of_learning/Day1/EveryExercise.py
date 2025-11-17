# ************************EXERCISE 4 : Afternoon at the Zoo********************************************8
# Goal:

# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, 
# and organizing them into alphabetical groups.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation

# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.

    def add_animals(self, new_animal):
        #new_animal = input('Enter an animal: ')
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f'{new_animal} is already in the list')


# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.

    def get_animals(self):
        for animal in self.animals:
            print(animal)

# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.

    def sell_animal(self, animal_sold):
        #animal_sold = input('Enter an animal, that has been sold: ')
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f'{animal_sold} is not in the list')

# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# Example output:

# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }

    def sort_animals(self):
        sorted_list = sorted(self.animals)
        sorted_list_dict = {}
        for animal in sorted_list:
            if animal[0] not in sorted_list_dict:
                sorted_list_dict.update({animal[0]: [animal]})
            else:
                sorted_list_dict[animal[0]] += [animal]
        return sorted_list_dict

# 7. Add a method get_groups():

# This method prints the grouped animals as created by sort_animals().
# Example output:

# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...

    def get_groups(self):
        groups = self.sort_animals()
        for key,value in groups.items():
            print (f'{key}: {value}')
        
# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

brooklyn_safari.add_animals("Giraffe")
brooklyn_safari.add_animals("Horse")
brooklyn_safari.add_animals("Bear")
brooklyn_safari.add_animals("Baboon")
brooklyn_safari.add_animals("Lion")
brooklyn_safari.add_animals("Hipopotam")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()