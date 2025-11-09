# EXERCISE 1: Hello World
# Print the following output using one line of code

print ('Hello World\n' * 4)


#EXERCISE 2: Some Math
#Write code that calculates the result of: #(99^3)*8 (meaning 99 to the power of 3, times 8)

x = (99**3)*8
print (x)


#EXERCISE 3: What is the output?
#Predict the output of the following code snippets:
#Coment what is your guess, then run the code and compare

print (5 < 3) #False, 5 is greater than 3
print (3 == 3) #True
print (3 == "3") #False, int and str
#print ("3" > 3) #False, str and int
print ("Hello" == "hello") #False, different font size


#EXERCISE 4: Your computer brand
#Instructions
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

computer_brand = input ('Type the brand of the computer: ')
print (f'I have a {computer_brand} computer.')


#EXERCISE 5: Your information
#Instructions
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. 
#The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.

name = 'Kira'
age = 34
shoe_size = 38
info = f"My name is {name} and I'm {age} years old. My shoe size is {shoe_size} and sometimes it's hard to find this shoe size in shops."
print (info)


#EXERCISE 6: A & B
#Instructions
#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".

a = 25
b = 13
if a > b:
    print ("Hello World")



#EXERCISE 7: Odd or Even
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.

num = int (input('Print your number, please: '))
if num % 2 == 0:
    print (f'Your number {num} is even')
else:
    print (f'Your number {num} is odd')


#EXERCISE 8: What’s your name?
#Instructions
#Write code that asks the user for their name and determines whether or not you have the same name. 
#Print out a funny message based on the outcome.

user_name = input('What is your name: ')
if user_name == 'Kira':
    print ('Wow! We have the same name. It\'s so cute!')
else:
    print ('Sorry! It\'s not a match')


#EXERCISE 9: Tall enough to ride a roller coaster
#Instructions
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

user_height = int(input('What\'s you height in cm: '))
if user_height > 145:
    print ('Great! You are tall enough to ride')
else:
    print ('Sorry! You need to grow some more to ride')