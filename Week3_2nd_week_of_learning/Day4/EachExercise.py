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