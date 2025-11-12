# Perfect number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers

# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False

user_num = int(input('Please, enter the number: '))

numbers_count = 0 

for i in range (1, user_num-1):
    if user_num % i == 0:
        numbers_count += i

if user_num == numbers_count:
    print (True)
else:
    print (False)


