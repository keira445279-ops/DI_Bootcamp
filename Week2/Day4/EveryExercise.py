# EXERCISE 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.

# Key Python Topics:
# Functions
# Conditionals (if / elif)
# Random numbers
# Floating-point numbers (Bonus)
# Handling seasons (Bonus)

# Step 1: Create the get_random_temp() Function
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.

# Step 2: Create the main() Function
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”

# Step 3: Provide Temperature-Based Advice
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”

# Step 4: Floating-Point Temperatures (Bonus)
# Modify get_random_temp() to return a random floating-point number using random.uniform() for more 
# accurate temperature values.

# Step 5: Month-Based Seasons (Bonus)
# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season 
# using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.

import random

def get_random_temp(season):
    if season == 'Winter':
        temp = random.uniform(-10, 5)
    elif season == 'Spring':
        temp = random.uniform(5, 20)
    elif season == 'Summer':
        temp = random.uniform(15, 35)
    elif season == 'Autumn':
        temp = random.uniform(10, 20)
    return temp

def main():
    user_input = int(input ('What is the month now. Print number from 1 to 12: '))
    season = ''
    if 3 <= user_input <= 5: 
        season = 'Spring'
    elif 6 <= user_input <= 8: 
        season = 'Summer'
    elif 9 <= user_input <= 11: 
        season = 'Autumn'
    else: 
        season = 'Winter'

    rand_temp = get_random_temp(season)
    print (f'The temperature right now is {rand_temp} degrees Celsius.')
    if rand_temp < 0:
        print ('Brrr, that\'s freezing! Wear some extra layers today.')
    elif 0 <= rand_temp < 16:
        print ('Quite chilly! Don\'t forget your coat.')
    elif 16 <= rand_temp <= 23:
        print ('Nice weather.')
    elif 24 <= rand_temp < 32:
        print ('A bit warm, stay hydrated.')
    elif 32 <= rand_temp <= 40:
        print ('It\'s really hot! Stay cool.')

main ()




# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

        

        






