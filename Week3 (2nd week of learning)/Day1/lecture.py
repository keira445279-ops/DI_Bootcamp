class Dog:
    def __init__(self, name, color, breed, age, is_trained): #the constructor function 
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        self.is_trained = is_trained

    def bark():
        pass

    def run(self):
        if self.age > 5:
            print (f'{self.name} prefers to walk')
        else:
            print (f'{self.name} is running')

dog1 = Dog('Rex', 'black', 'german shephard', 8, True)
dog1.guidance_dog = True

dog2 = Dog('Umka', 'white cream', 'pomeranian', 5, True)

print(dog2.name)

dog1.run()
dog2.run()


#create a class called BankAccount, with 3 attributes:
#- account houlder = name + last name of a person
#- account number = random number
#- balance which starts with 50.00 (float)

class BankAccount:
    def __init__(self, account_houlder, account_number, balance = 50): #или можно написать 50.00 - автоматический float
        self.account_houlder = account_houlder
        self.account_number = account_number
        self.balance = float(balance)

# def view_balance(self):
#     report = f '''account holder: {self.account_houlder}
#             account number: {self.account_number}
#             balance: {self.balance}'''
#     print(report)

def deposit(self, amount):
    self.balance += amount
    return self.balance

acc1 = BankAccount('Taylor Swift', 2345234, 1000000000000000)

acc1.transactions = []

print(acc1.__dict__)