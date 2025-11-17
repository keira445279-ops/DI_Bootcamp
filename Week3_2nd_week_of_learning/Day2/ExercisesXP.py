# ************************************Exercise 1: Pets**************************************************
# Key Python Topics:
# Inheritance
# Class instantiation
# Lists
# Polymorphism

# Instructions:
# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, 
# and use the Pets class to manage them.
# See the example below, before diving in.

# Step 1: Create the Siamese Class
# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.

# Step 2: Create a List of Cat Instances
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [Bengal('Fluffy', 5), Chartreux('Poly', 3), Siamese('Crocky', 7)]

# Step 3: Create a Pets Instance
# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.

sara_pets = Pets(all_cats)

# Step 4: Take Cats for a Walk
# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.

sara_pets.walk()

# Step 1: Create the Siamese class
# Step 2: Create a list of cat instances
# Step 3: Create a Pets instance of the list of cat instances
# sara_pets = Pets(all_cats)
# Step 4: Take cats for a walk
# sara_pets.walk()


# ********************************************Exercise 2: Dogs*******************************************
# Goal: Create a Dog class with methods for barking, running speed, and fighting.
# Key Python Topics:
# Classes and objects
# Methods
# Attributes


# Instructions:
# Step 1: Create the Dog Class
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, 
# based on run_speed * weight.

# Step 2: Create Dog Instances
# Create three instances of the Dog class with different names, ages, and weights.

# Step 3: Test Dog Methods
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        counts = self.weight / (self.age *10)
        return counts

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            print (f"The winner is {self.name}")
            return self
        else:
            print (f"The winner is {other_dog.name}")
            return other_dog
        
# Step 2: Create dog instances
dog1 = Dog('Murphy', 5, 3.5)
dog2 = Dog('Monty', 2, 3)
dog3 = Dog('Leo', 3, 6.5)

# Step 3: Test dog methods
print(dog2.bark())
print(dog3.run_speed())
dog1.fight(dog3)


# **********************************Exercise 3: Dogs Domesticated****************************************************
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.
# Key Python Topics:
# Inheritance
# super() function
# *args
# Random module

# Instructions:
# Step 1: Import the Dog Class
# In a new Python file, import the Dog class from the previous exercise.

# Step 2: Create the PetDog Class
# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.

# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.

from Dog_Class import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False

    def train(self): 
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print (f'{self.name}, {(', ').join(args)} all play together')
        
    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
            if random.choice(tricks) in tricks:
                return True
            else:
                return False


# Step 3: Test PetDog Methods
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


# *************************************Exercise 4: Family and Person Classes****************************************
# Goal:
# Practice working with classes and object interactions by modeling a family and its members.

# Key Python Topics:
# Classes and objects
# Instance methods
# Object interaction
# Lists and loops
# Conditional statements (if/else)
# String formatting (f-strings)

# Instructions:
# Step 1: Create the Person Class
# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

class Person:
    def __init__(self, first_name, age, last_name = ''):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name 

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False


# Step 2: Create the Family Class
# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)

class Family:
        def __init__(self, last_name = ''):
            self.last_name = last_name
            self.members = []

# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.

        def born(self, first_name, age):
            person1 = Person(first_name, age, self.last_name)
            self.members.append(person1)
            return person1
    
# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."

        def check_majority(self, first_name):
            for member in self.members:
                if member.first_name == first_name:
                    if member.is_18():
                        print('You are over 18, your parents Jane and John accept that you will go out with your friends.')
                    else:
                        print('Sorry, you are not allowed to go out with your friends.')
          

# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.

        def family_presentation(self):
            print(self.last_name)
            for member in self.members:
                print (f'{member.first_name} - {member.age}')

# Expected Behavior:
# Once implemented, your program should allow you to:
# Create a family with a last name.

my_family = Family('Swift')
print(my_family.last_name)

# Add members to the family using the born() method.

my_family.born('Taylor', 35)
my_family.born('Austin', 15)

# Use check_majority() to see if someone is allowed to go out.

my_family.check_majority('Taylor')
my_family.check_majority('Austin')

# Display family information with family_presentation().

my_family.family_presentation()

# Don’t forget to test your classes by creating an instance of Family, adding members, 
# and calling each method to see the expected output.