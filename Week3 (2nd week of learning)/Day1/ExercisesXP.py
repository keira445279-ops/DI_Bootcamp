# *****************EXERCISE 1: Cats*******************************
# Key Python Topics:
# Classes and objects
# Object instantiation
# Attributes
# Functions

# Instructions:
# Use the provided Cat class to create three cat objects.
# Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('Kapa', 12)
cat2 = Cat('Funny', 10)
cat3 = Cat('Topa', 15)

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

def oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    for cat in (cat1,cat2,cat3):
        if cat.age > oldest.age:
            oldest = cat
    return oldest

oldest = oldest_cat(cat1, cat2, cat3)

# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

print(f'The oldest cat is {oldest.name}, and is {oldest.age} years old.')

# Example:*

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# # Step 1: Create cat objects
# # cat1 = create the object

# # Step 2: Create a function to find the oldest cat
# def find_oldest_cat(cat1, cat2, cat3):
#     # ... code to find and return the oldest cat ...

# Step 3: Print the oldest cat's details


# *****************************EXERCISE 2 : Dogs**********************************
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)

# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print (f'{self.name} goes woof!')
    
    def jump(self): 
        print (f'{self.name} jumps {self.height * 2} cm high!')

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

davids_dog = Dog('Tonya', 50)
sarahs_dog = Dog('Winnie', 32)

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

print(davids_dog.name)
print(sarahs_dog.name)

print(davids_dog.height)
print(sarahs_dog.height)

print(davids_dog.__dict__)
print(sarahs_dog.__dict__)

davids_dog.bark()
sarahs_dog.bark()

davids_dog.jump()
sarahs_dog.jump()

# # Step 4: Compare Dog Sizes
def dog_sizes(davids_dog, sarahs_dog):
    highest = davids_dog
    for dog in (davids_dog,sarahs_dog):
        if dog.height > highest.height:
            highest = dog
    return highest

highest = dog_sizes(davids_dog, sarahs_dog)

print(f'{highest.name} is the highest, because her height is {highest.height} cm')


# ***********************8Exercise 3 : Who’s the song producer?************************************
# Goal: Create a Song class to represent song lyrics and print them.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists

# Instructions:
# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for element in self.lyrics:
            print (element)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])  

stairway.sing_me_a_song()

# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven


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