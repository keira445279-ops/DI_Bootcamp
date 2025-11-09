## Daily Challenge: Build up a string

### What You Will Learn:
#Python Basics
#Conditionals
#Loops


### Instructions:

#1. **Ask for User Input:**
   #The string **must be exactly 10 characters long**.

#2. **Check the Length of the String:**
   #If the string is **less than 10 characters**, print: `"String not long enough."`
   #If the string is **more than 10 characters**, print: `"String too long."`
   #If the string is **exactly 10 characters**, print: `"Perfect string"` and proceed to the next steps.

#3. **Print the First and Last Characters:**
   #Once the string is validated, print the **first** and **last** characters.


user_inpute = input ('Please, write something, that you want, but it shoul contain 10 chatacters: ')

if len(user_inpute) < 10:
    print ("String not long enough.") 
elif len(user_inpute) > 10:
    print ("String too long.") 
else:
    print ("Perfect string.") 
     
print (user_inpute[0], user_inpute [9])

#4. **Build the String Character by Character:**
   #Using a `for` loop, construct and print the string **character by character**. Start with the first character, 
   # then the first two characters, and so on, until the entire string is printed.
   
   #**Hint:** You can create a loop that goes through the string, adding one character at a time, and print it progressively.

   #Example:
   
   #![Alt text](./example-dc-w1d1.png)

user_input_counter = ''

for i in user_inpute:
    user_input_counter +=i
        
    print (user_input_counter)

#5. **Bonus: Jumble the String (Optional)**
   #As a bonus, try **shuffling** the characters in the string and print the newly jumbled string.
   #**Hint:** You can use the `random.shuffle` function to shuffle a list of characters.

import random
user_inpute_list = list (user_inpute)
random.shuffle(user_inpute_list) #this function only shuffle, but not collect th string
shuffled = ''.join(user_inpute_list) #this function collect the shiffled string

print (shuffled)




