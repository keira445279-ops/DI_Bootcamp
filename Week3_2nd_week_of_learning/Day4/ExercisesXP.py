# **********************************Exercise 1: Random Sentence Generator************************************

# Goal: Create a program that generates a random sentence of a specified length from a word list.

# Key Python Topics:

# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation

# Instructions:
# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.

import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

# Step 1: Create the get_words_from_file function
# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.

def get_words_from_file(dir_path):
    with open (dir_path + '\words.txt', 'r') as f:
        list_content = f.read()
        words_list = list_content.split()
        return words_list
    

# print(get_words_from_file(dir_path))


# Step 2: Create the get_random_sentence function
# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.

def get_random_sentence(sen_len):
    words = get_words_from_file(dir_path)
    sentence = ''
    for i in range(sen_len):
        chosen_word = random.choice(words)
        sentence += chosen_word + ' '
    sentence_low = sentence.lower()
    return sentence_low

# get_random_sentence(sen_len=2)

# Step 3: Create the main function
# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.

def main():
    print('The main goal of the programm - to generate a random sentence of a specified length from a word list')
    while True:
        try:
            sen_len = int(input('Please, enter the lenght of the sentence: '))
        except ValueError:
            print ('You should input only number')
            continue
        if not 2 <= sen_len <= 20:
            print('The number should be between 2 and 20 (inclusive)')
            continue
    
        print(get_random_sentence(sen_len))
        break

main()


# **********************************Exercise 2: Working with JSON*********************************
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.

# Key Python Topics:

# JSON parsing (json.loads())
# JSON serialization (json.dump())
# Dictionaries
# File handling (open())

# Instructions:
# Using the follow code:

import json
import os

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string

# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.

sampleJson2 = json.loads(sampleJson)
print(sampleJson2)


# Step 2: Access the nested “salary” key
# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.

print(sampleJson2["company"]["employee"]["payable"]["salary"])


# Step 3: Add the “birth_date” key
# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.

sampleJson2["company"]["employee"].update({"birth_date": "1990-05-24"})
print (sampleJson2["company"]["employee"])


# Step 4: Save the JSON to a file

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\sampleJson2.json', 'w') as f:
    json.dump(sampleJson2, f) # create a file
    print('file was created')
