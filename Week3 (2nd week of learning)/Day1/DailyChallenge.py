# ******************************Daily challenge: Old MacDonald’s Farm*************************************
# Key Python Topics:
# Classes and Objects
# Dictionaries
# String Formatting
# Methods
# List manipulation (sorted())
# Conditional logic (if)
# String concatenation

# Instructions: Old MacDonald’s Farm
# You are given example code and output. Your task is to create a Farm class that produces the same output.

# Step 1: Create the Farm Class
# Create a class called Farm.
# This class will represent a farm and its animals.

# Step 2: Implement the __init__ Method
# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name 
# and animals to store the animals (initialize as an empty dictionary).

class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

# Step 3: Implement the add_animal Method
# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). 
# Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

# Step 8: upgrade the add_animal Method
# use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
# Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)

    # def add_animals(self, animal_type, count=1):
    #     if animal_type not in self.animals:
    #         self.animals.update({animal_type: count})
    #     else:
    #         self.animals[animal_type] += count

    def add_animals(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type not in self.animals:
                self.animals.update({animal_type: count})
            else:
                self.animals[animal_type] += count

# Step 4: Implement the get_info Method
# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.

    def get_info(self):
        result = f'{self.farm_name}\'s farm\n'
        for animal_type,count in self.animals.items():
            result += f'{animal_type}: {count}\n'
        
        result += f'E-I-E-I-0!'
        return result
    
# Bonus: Expand The Farm
# Step 6: Implement the get_animal_types Method
# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.

    def get_animal_types(self):
        animal_types = []
        for animal_type in self.animals.keys():
            animal_types.append(animal_type)
        animal_types_sorted = sorted(animal_types)
        return animal_types_sorted
    
# Step 7: Implement the get_short_info Method
# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.

    def get_short_info(self):
        types = self.get_animal_types()
        types_plural = []
        for animal_type,count in self.animals.items():
            if count > 1:
                plural = animal_type + 's'
                types_plural.append(plural)
            else:
                plural = animal_type
                types_plural.append(plural)
        if len(types_plural) > 1:
            result = f'{(', ').join (types_plural[:-1])} and {types_plural[-1]}'
        else:
            types_plural[0]

        return f'{self.farm_name}\'s farm has {result}'




# Step 5: Test Your Code
# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.


# Example:
# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...

#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...

#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...


macdonald = Farm("McDonald")
# macdonald.add_animals('cow', 5)
# macdonald.add_animals('sheep')
# macdonald.add_animals('sheep')
# macdonald.add_animals('goat', 12)
# macdonald.add_animals('horse', 3)
# macdonald.add_animals('duck')
macdonald.add_animals(cow= 5, sheep = 2, goat = 12)
print(macdonald.get_info())

print(macdonald.get_animal_types())
print(macdonald.get_short_info())

# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!


