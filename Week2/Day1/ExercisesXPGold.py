#EXERCISE 1 : Hello World-I love Python
#Instructions
#Print the following output in one line of code:
#Hello world
#Hello world
#Hello world
#Hello world
#I love python
#I love python
#I love python
#I love python

print ('Hello World\t' * 4, 'I love python\t' * 4)


#EXERCISE 2 : What is the Season ?
#Instructions
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

month = int(input('Please enter any number of month from 1 to 12: '))
if 3 <= month <= 5:
    print ('The season of the month {month} is Spring')
elif 6 <= month <= 8:
    print ('The season of the month {month} is Summer')
elif 9 <= month <= 11:
    print ('The season of the month {month} is Autumn')
else:
    print ('The season of the month {month} is Winter')