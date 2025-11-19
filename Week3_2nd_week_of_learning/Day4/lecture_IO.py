
import os

# Python - I/O

# Old shcool way - you need to explicity close the file after using it - using close() method

# file_obj = open('file-name.txt', 'w')
# # code
# file_obj.close()


# New way: use with statement
# The main issue that python can not find a file, thats why we need os module to give the full path to the file

# with open ('secrets.txt', 'r') as file_obj:
#     print(file_obj.read())

# this code you need to use everytime when you`re working with files`
dir_path = os.path.dirname(os.path.realpath(__file__))

# with open (dir_path + r'\secrets.txt', 'r') as file_obj:
#     content = file_obj.read()
#     print(content)

# with open (dir_path + '\starwars.txt', 'r') as f:
#     # Read the file line by line
#     txt_list = f.readlines()
#     for line in txt_list:
#         print(line)
#     print ('end of document')

# # Read only the 5th line of the file
#     print(txt_list[4])

# # Read only the 5 first characters of the file
#     print(txt_list[:5])
   
# # Read all the file and return it as a list of strings. Then split each word into letters
#     temp = [] # step 1
#     for name in txt_list: # step 2
#         temp.append(list(name)) # step 3
#     print(temp)

    # list comprehension
    # temp = [list(name) for name in txt_list if name == 'Darth\n']
    # print(temp)

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
    
    # counts = {'Darth': 0, 'Luke': 0, 'Lea': 0}
    # for name in txt_list:
    #     if name == 'Darth':
    #         counts['Darth'] +=1
    #     if name == 'Luke':
    #         counts['Luke'] +=1
    #     if name == 'Lea':
    #         counts['Lea'] +=1

    # print(counts)

    # better to use count()

#     ful_txt_str = ''.join(txt_list)
#     counts = {'Derth': ful_txt_str.count('Darth'),
#               'Luke': ful_txt_str.count('Luke'),
#               'Lea': ful_txt_str.count('Lea')
#     }

#     print(counts)

# # Append your first name at the end of the file
# with open (dir_path + '\starwars.txt', 'a+') as f:
#     f.seek(0, os.SEEK_END) # checking the cursor at thr end of the file
#     f.write('\nKira')
#     print('successfully added')

# Append "SkyWalker" next to each first name "Luke"
with open (dir_path + '\starwars.txt', 'r+') as f:
    txt_list = f.readlines()
    modified_comtent = []
    for name in txt_list:
        if name == 'Luke\n':
            # txt_list[name] = 'Luke Skywalker'
            modified_comtent.append('Luke Skywalker\n')
        else:
            modified_comtent.append(name)
    
    print(txt_list)

with open (dir_path + '\starwars.txt', 'w+') as f:
    f.seek(0)
    f.writelines(modified_comtent)
    print ('Skywalker was added')