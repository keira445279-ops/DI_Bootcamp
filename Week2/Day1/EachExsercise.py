#EXERCISE 7: Odd or Even
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.

num = int (input('Print your number, please: '))
if num % 2 ==0:
    print (f'Your number {num} is even')
else:
    print (f'Your number {num} is odd')