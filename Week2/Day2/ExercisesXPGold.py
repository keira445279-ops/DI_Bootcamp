# EXERCISE 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

my_list = ["dog", "cat", "bear", "horse"]
my_list.extend (["yellow", "green", "violet"])
print (my_list)


# EXERCISE 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for i in range (1500, 2501):
    if i % 5 ==0 and i % 7 == 0:
        print (i)


# EXERCISE 3: Check the index
# Instructions
# Using this variable
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

while True:
    user_name = input ('What is your name: ')

    if user_name in names:
        print (names.index(user_name))
        break
    else:
        print ('The name is not in the list. Try again')


# EXERCISE 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87

numbers = []

user_num_1 = int(input("Please, enter the 1st number: "))
user_num_2 = int(input("Please, enter the 2nd number: "))
user_num_3 = int(input("Please, enter the 3d number: "))

numbers.append(user_num_1)
numbers.append(user_num_2)
numbers.append(user_num_3)

print (max(numbers))



# EXERCISE 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant

vowels = 'aeiou'

for i in range (97,123):
    if chr(i) in vowels:
        print (f'The character {chr(i)} is vowel')
    else:
        print (f'This character {chr(i)} is consonant')



# EXERCISE 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words = []

while True:
    user_word = input ('Please, type a word: ')
    words.append(user_word)
    if len(words) == 7:
        break

while True:
    letter = input ('Please, type any character: ')
    if len(letter) > 1:
        print ('You need to type only one character. Try again.')
    else:
        break

for word in words:
    if letter in word:
        print (f'The letter {letter} is in the word {word} and the index of this letter is {word.index(letter)}')
    else:
        print (f'Unfortunately the letter {letter} is not in the word {word}')


# EXERCISE 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your 
# list actually starts at one and ends at one million. Use the sum() function to see how quickly 
# Python can add a million numbers.
         
numbers = [i for i in range (1, 1000001)]  
print (max(numbers))
print (min(numbers))
print (sum (numbers))

# it takes a lot of memery, to optimize it's better to use another code:

print (min(range(1, 1000001)))
print (max(range(1, 1000001)))
print (sum(range(1, 1000001)))