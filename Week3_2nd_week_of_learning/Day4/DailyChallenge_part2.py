# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

import os
from DailyChallenge import Text

class From_File(Text):

    @classmethod
    def from_file(cls, dir_path):
        with open(dir_path + '\DailyChallenge.py', 'r') as f:
            content = f.read()
        return cls(content)
    
dir_path = os.path.dirname(os.path.realpath(__file__))

str1 = Text('I love love love love love pizza')
print(str1.most_common_word())