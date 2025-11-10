#EXERCISE 1 : Use the terminal
#Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory

#PATH is an environment variable that stores a list of directories. 
#The directory that contains python3 is included in this PATH. 
#So the system can quickly find the python executable and run it, even if I’m not in its folder.

#EXERCISE 2 : Alias

#An alias is a short name or shortcut for a longer command. 
# It allows you to run the command without typing the full original command.


#EXERCISE 3 : Outputs
#Instructions
#Predict the output of the following code snippets:

3 <= 3 < 9 #True
3 == 3 == 3 #True
bool(0) #False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4") #FAlse
bool(bool(None)) #False

x = (1 == True) #True
y = (1 == False) #False
a = True + 4 #5, because True
b = False + 10 #10, because False

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


#EXERCISE 4 : How many characters in a sentence ?
#Instructions
#Use python to find out how many characters are in the following text, use a single line of code 
# (beyond the establishment of your my_text variable).

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print (len(my_text))


#EXERCISE 5: Longest word without a specific character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_length = 0

while True:
    sentence_without_a = input('Please, write the longest sentence that yoa can without the character \'a\': ')
    
    if 'a' in sentence_without_a and 'A' in sentence_without_a:
        print ('Your sentence containce \'a\'')
        continue
        
        
    if len (sentence_without_a) > longest_length:
        print ('Congratulations!')
        longest_length = len(sentence_without_a)
    


