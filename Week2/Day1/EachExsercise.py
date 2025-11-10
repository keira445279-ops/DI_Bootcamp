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