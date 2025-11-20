# Key Python Topics:

# OOP (Classes, Methods)
# File I/O (Reading Files)
# String Manipulation (strip(), split(), isalpha()) +++++++++
# Algorithm Design (Anagram Checking)
# User Input and Validation
# Conditional Logic
# Loops

# An anagram checker program that takes user input, validates it, and finds anagrams from a word list.
# Instructions:
# Download the provided text file (word list).
# Create anagram_checker.py with the AnagramChecker class.
# Create anagrams.py for the user interface.
# anagram_checker.py:

# Step 1: Create the AnagramChecker Class
# Create a class called AnagramChecker.
# Implement the __init__ method:
# Load the word list file into a variable (e.g., a set or list).
# Store the words in lowercase for case-insensitive comparison.

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'sowpods.txt')

class AnagramChecker:
    def __init__(self, file_path):
        with open(file_path) as f:
            text = f.read().lower()
            self.words = text.split()

# Step 2: Implement is_valid_word Method
# Create a method called is_valid_word(word).
# Check if the given word exists in the loaded word list (case-insensitive).
# Return True if valid, False otherwise.

    def is_valid_word(self, word):
        word = word.lower()
        if word in self.words:
            return True
        else:
            return False

# Step 3: Implement is_anagram Method
# Create a method called is_anagram(word1, word2).
# Check if the sorted characters of word1 are equal to the sorted characters of word2.
# Return True if anagrams, False otherwise.

    def is_anagram(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if self.is_valid_word(word1) and self.is_valid_word(word2):
            return sorted(word1) == sorted(word2)
        else:
            return False
    
# Step 4: Implement get_anagrams Method
# Create a method called get_anagrams(word).
# Create an empty list to store anagrams.
# Iterate through the word list.
# For each word in the list, check if it’s an anagram of the given word using is_anagram.
# If it’s an anagram and not the same word, add it to the anagrams list.
# Return the list of anagrams.

    def get_anagrams(self, word):
        word = word.lower()
        anag_list = []
        for i in self.words:
            if i != word:
                if self.is_anagram(word,i):
                    anag_list.append(i)
        return anag_list

    
