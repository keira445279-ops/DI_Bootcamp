#my_name = 'Kira'
#upper_name = my_name.upper()

#print (upper_name)

description = "strings are text in Python, enclosed in quotsation marks, sequence of chars"
upper_description = description.upper()
print (upper_description)

description_is = description.replace ('strings are', 'string is')
print (description_is)


x=1
y=2

temp = y #variable that helps to save meaning to swap to variables
y = x
x = temp
print (x, y)


#Ask the user for their age using the input() function and store it in a variable age.
#Convert the inputted age into an integer and calculate the number of years until they turn 100.
#Display a message: "You will turn 100 in X years", where X is the number of years calculated.

age = int(input('What is your age?'))
calculated_years = 100 - age
print (f'You will turn 100 in {calculated_years} years')
print (f'You will turn 100 in {100 - age} years')