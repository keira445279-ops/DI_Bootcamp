
import re
from datetime import datetime as dt

class Person:

    def __init__(self, first_name, last_name, birth_day):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_day = birth_day
        self._full_name = None # protected atribute, used by developers - incapsulation
        self.__salary = 35000 # privet 

    @staticmethod #a method without self - usually used for unternal formzting
    def format_name(name):
        name = name.strip().capitalize()
        name = re.sub(r'[^a-zA-Z]', '', name)
        return name
    
    @staticmethod
    def parse_birth_date():
        pass
        
    @classmethod
    def from_age(cls, first_name, last_name, age):
        current_year = dt.today().year # current date and time, if we wanna specify we should put .year
        birth_year = current_year - age
        birth_date = f'1-1-{(birth_year)}'
        return cls (first_name, last_name, birth_date)

    # @staticmethod #a method without self - usually used for unternal formzting
    # def format_full_name(first, last):
    #     return f'{first} {last}'
    
    @property # without setter impossible to call the method, need to use the setter
    def full_name(self):
        self._full_name = f'{self.first_name} {self.last_name}'
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name

    def presentation(self):
        print(f'Hello, my name is {self.full_name}')

# DUNDER METHODS OR MAGIC METHODS

    def __str__(self): # the string everitime as we print the object
        return f'Hello, my name is {self.full_name}, my birth-date is {self.birth_day}'

    def __repr__(self):
        return f'{self.__dict__}' # если str нет, то напечатается repr

    def __eq__(self, other): # compare two objects, return true or false
        return len(self.first_name) == len(other.first_name)

p1 = Person('john', 'snow', '05-12-1980')
p2 = Person('ARIA', 'STARK', '30-07-2000')

# print(p1.first_name, p1.last_name)
# print(p2.first_name, p2.last_name)

# print(dt.today().year)

#creating an object using our classmethod
# p3 = Person.from_age('Sansa', 'Stark', 30)
# print(p3.birth_day)

p4 = Person('Daenerys', 'Targaryen', 32)
print(p4.full_name) # as we have setter, call without underscore


#print(p4.__salary) - 'the traditional way' gives errors, but there is a special way that we can access a privet attribute:
print(p2._Person__salary) # 'the not traditional way' to access privet information


p2.presentation() # calling the method

print(p1)
print(p1 == p4)