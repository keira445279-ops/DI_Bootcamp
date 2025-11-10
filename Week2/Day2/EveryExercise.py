# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

allowed_teenagers = []

while True:
    
    teenager_name = input ('What is your name: ')
    if teenager_name == 'any':
        break

    teenager_age = int(input(f'{teenager_name} what is your age: '))
    
    if 16 <= teenager_age <= 21:
        allowed_teenagers.append(teenager_name)

print (allowed_teenagers)

 

        
         
    

