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

longest_word(sentence = 'I do not like rude people')

# Expected Output:

# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".


# Key Python Topics:
# Functions
# Strings
# .split() method
# Loops (for)
# Conditional statements (if)
# String length (len())
