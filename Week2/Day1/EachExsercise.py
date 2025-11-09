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