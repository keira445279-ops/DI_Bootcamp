# CGALLENGE 1: Sorting
# Instructions:
# Write a Python program that takes a single string of words as input, where the words are separated 
# by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, 
# with the sorted words also separated by commas.

# Step 1: Get Input
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.

user_words = input('Type several words separated by commas: ')

# Step 2: Split the String

user_words_to_list = user_words.split(',')

# Step 3: Sort the List

user_words_to_list_sort = sorted (user_words_to_list)

# Step 4: Join the Sorted List

user_words_sort_to_string = ','.join (user_words_to_list_sort)

# Step 5: Print the Result
# Print the resulting comma-separated string.

print(user_words_sort_to_string)

# Expected Output:
# If the input is without,hello,bag,world, the output should be bag,hello,without,world.



# CHALLENGE 2: Longest Word
# Instructions:
# Write a function that takes a sentence as input and returns the longest word in the sentence. 
# If there are multiple longest words, return the first one encountered. Characters like apostrophes, 
# commas, and periods should be considered part of the word.

# Step 1: Define the Function
# Define a function that takes a string (the sentence) as a parameter.

# Step 2: Split the Sentence into Words

# Step 3: Initialize Variables

# Step 4: Iterate Through the Words

# Step 5: Compare Word Lengths

# Step 6: Return the Longest Word

def longest_word(sentence):
    sentence_to_words = sentence.split()
    longest = ''
    for word in sentence_to_words:
        if len(word) > len(longest):
            longest = word
    print(longest)

longest_word(sentence = 'Margaret\'s toy is a pretty doll')

# Expected Output:

# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".
