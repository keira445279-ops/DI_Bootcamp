# ***************************************************Exercise 1: Currencies********************************************
# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, 
# and in-place addition.

# Key Python Topics:
# Dunder methods (__str__, __repr__, __int__, __add__, __iadd__)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s' #dollar - dollars
    
    def __int__(self):
        return int(self.amount) #add int

    def __repr__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'

    def __add__(self,other):
        if type(other) != int:
            return self.amount + other.amount
        else:
            return self.amount + other
    
    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __iadd__(self,other):
        if type(other) != int:
            result = self.amount + other.amount
            self.amount = result
            return self
        else:
            result = self.amount + other
            self.amount = result
            return self

    def __add__(self,other):
        if self.currency != other.currency:
            return f'Cannot add between Currency type {self.currency} and {other.currency}'
    
    # def __add__(self,other):
    #     if type(other) != int and self.currency == other.currency:
    #         return self.amount + other.amount
    #     elif type(other) == int:
    #         return self.amount + other
    #     else:
    #         raise TypeError (f'Cannot add between Currency type {self.currency} and {other.currency}')


# Using the code above, implement the relevant methods and dunder methods which will output the results below.

# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# the comment is the expected output


print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

# print(c1 + 5)
# # 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# ***************************************Exercise 3: String module********************************************
# Goal: Generate a random string of length 5 using the string module.

# Instructions:
# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.

# Key Python Topics:
# string module
# random module
# String concatenation

# Step 1: Import the string and random modules
# Import the string and random modules.

#import string
from string import ascii_lowercase
import random

# Step 2: Create a string of all letters
# Read about the strings methods HERE to find the best methods for this step

# Step 3: Generate a random string
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.

result = ascii_lowercase
rand_char = ''.join(random.choice(result) for i in range (5))
print (rand_char)


# ***************************************Exercise 4: Current Date***************************************8
# Goal: Create a function that displays the current date.
# Key Python Topics:
# datetime module

# Instructions:
# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module

from datetime import datetime as dt

# Step 2: Get the current date

cur_date = dt.today().date()

# Step 3: Display the date

print(cur_date)


# ***************************Exercise 5: Amount of time left until January 1st***************************************
# Goal: Create a function that displays the amount of time left until January 1st.

# Key Python Topics:
# datetime module
# Time difference calculations

# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

from datetime import datetime as dt

# Step 2: Get the current date and time
# Step 3: Create a datetime object for January 1st of the next year
# Step 4: Calculate the time difference
def time_to_jan():
    cur_date = dt.now()
    jan_date = dt(2026,1,1,0,0,0,0)
    rem_time = jan_date - cur_date
    return rem_time

# Step 5: Display the time difference
print(time_to_jan())


# *************************************Exercise 6: Birthday and minutes***************************************************
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method


# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

from datetime import datetime as dt

def birth_date(b_date): 
    new_date = dt.strptime(b_date, '%d.%m.%Y')
    dif = dt.now() - new_date
    dur_min = dif.total_seconds() * 60
    return f'You are living in this crazy world already {dur_min} minutes'


print(birth_date(b_date = '10.03.1991'))


# *****************************************Exercise 7: Faker Module****************************************
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Read more about this module HERE

# Key Python Topics:
# faker module
# Dictionaries
# Lists
# Loops

# Instructions:
# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.
# Step 1: Install the faker module
# Step 2: Import the faker module

from faker import Faker
fake = Faker()

# Step 3: Create an empty list of users

users = []

# Step 4: Create a function to add users
# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.

def add_user(user_num):
    for i in range(user_num):
        user_info= {
            'name': fake.name(), 
            'address': fake.address(), 
            'language_code': fake.language_code()
            }
        users.append(user_info)

# Step 5: Call the function and print the users list

add_user(30)
for user in users:
    print(user)