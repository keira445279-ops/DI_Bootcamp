# EXERCISE 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

random_num = random.randint(1,9)
print (random_num) #check up

result_win=0
result_lost=0

while True:
    user_number = int(input('Please, enter the number from 1 to 9: '))
    if user_number == random_num:
        print ('Winner')
        result_win += 1
    else:
        print ('Better luck next time')
        result_lost +=1

    choise = input ('Do you want to quit (yes/no): ')
    if choise == 'yes':
        print ('Get ASAP')
        break
    elif choise == 'no':
        print ('You are a fighter')
    else:
        print ('You have to enter yes or no. Try again')

print (f'You won {result_win} times')
print (f'You lost {result_lost} times')



