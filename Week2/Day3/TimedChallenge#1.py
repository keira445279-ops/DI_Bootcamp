# maybe i have to reverse index from positive to negative for each item in string

# Reverse the Sentence
# Write a program to reverse the sentence wordwise.
# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You

raw_input = input('Please, type a sentence: ') 

raw_input_list = raw_input.split() #string to list, because list has indexes

raw_reversed = list(reversed(raw_input_list)) #reverse the list

raw_input_reversed = ' '.join(raw_reversed) #list to string

print (raw_input_reversed)
