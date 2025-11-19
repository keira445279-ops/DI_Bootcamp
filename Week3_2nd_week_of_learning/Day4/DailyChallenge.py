# **********************************************Daily challenge : Text Analysis**********************************

# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques


# Key Python Topics:
# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)

# Instructions:
# Create a Text class to analyze text data, either from a string or a file. 
# Then, create a TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String

# Step 1: Create the Text Class
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).




class Text:
    def __init__(self, text = ''):
        self.text = text

# Step 2: Implement word_frequency Method
# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

    def word_frequency(self, word):
        text_to_words = self.text.split()
        if word not in text_to_words:
            # return None
            return f'There is no word {word}'
        else:
            w_count = 1
            each_word = ''
            for word in text_to_words:
                if word != each_word:
                    each_word = word
                elif each_word == word:
                    w_count += 1
            return w_count

# Step 3: Implement most_common_word Method
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

    def most_common_word(self):
        text_to_words = self.text.split()
        counts_dict = {}
        for word in text_to_words:
            w_count = text_to_words.count(word)
            if word != counts_dict:
                counts_dict.update({word: w_count})
            elif counts_dict[word] == word:
                counts_dict[w_count]
            ser_key = [(w_count, word) for word, w_count in counts_dict.items()]
            result = max(ser_key)[1]
        return result

# Step 4: Implement unique_words Method
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

    def unique_words(self):
        text_to_words = self.text.split()
        w_uniq = set(text_to_words)
        set_to_list = [i for i in w_uniq]
        return set_to_list

    @classmethod
    def from_file(cls, file_path):
        # with open(dir_path + '\for_DC.txt', 'r') as f:
        with open(file_path) as f:
            content = f.read()
        return cls(content)

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
# file_path = os.path.join(dir_path, 'for_DC.txt')
file_path = os.path.join(dir_path, 'for_DC.txt')

# txt_obj = Text.from_file(dir_path)
txt_obj = Text.from_file(file_path)

print(txt_obj.word_frequency('love'))
print(txt_obj.most_common_word())
print(txt_obj.unique_words())


# Bonus: Text Modification
# Step 6: Create the TextModification Class
# Create a class called TextModification that inherits from Text.

import string 
import re

class TextModification(Text):
    def __init__(self, text=''):
        super().__init__(text)
    
# Step 7: Implement remove_punctuation Method
# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.

    def remove_punctuation(self):
        punct = string.maketrans("","",string.punctuation)
        clean_text = self.text.translate(punct)
        return clean_text
    
# Step 8: Implement remove_stop_words Method
# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.

    def remove_stop_words(self):
        stop_words = ['a', 'the', 'is']
        self.text = (' ').join([i for i in self.text.split() if i.lower() not in stop_words])
        return self.text
        # text_to_lt = self.text.split()
        # rem_list = []
        # for i in text_to_lt:
        #     if i.lower() not in stop_words:
        #             rem_list.append(i)
        
        
# Step 9: Implement remove_special_characters Method
# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.  

    def remove_special_characters(self):
        clean_text = re.sub(r'[^A-Za-z0-9 ]+', '', self.text)
        return clean_text