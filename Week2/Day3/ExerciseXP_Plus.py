# Exercise 1 : Student Grade Summary
# Instructions
# You are given a dictionary containing student names as keys and lists of their grades as values. 
# Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, 
# and determines the class average.

# Initial Data:
# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }

# Requirements:
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
# Calculate the class average (the average of all students’ averages) and print it.
# Print the name of each student, their average grade, and their letter grade.
# Hints:
# Use loops to iterate through the student_grades dictionary.
# You may use sum() and len() functions to help calculate averages.
# Initialize empty dictionaries for student_averages and student_letter_grades before filling them with data.

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = student_grades.copy()

for key, value in student_averages.items():
    student_averages[key] = round ((sum (value) / len(value)), 2)
    student_averages.update({key : student_averages[key]})

letter_grades = student_averages.copy()

for key, value in letter_grades.items():
    if student_averages[key] >= 90:
        letter_grades.update({key: 'A'}) 
    elif 80 <= student_averages[key] <= 89:
        letter_grades.update({key: 'B'})
    elif 70 <= student_averages[key] <= 79:
        letter_grades.update({key: 'C'})
    elif 60 <= student_averages[key] <= 69:
        letter_grades.update({key: 'D'})
    else:
        letter_grades.update({key: 'F'})

class_average = round ((sum (student_averages.values()) / len(student_averages.values())), 2)   

#разобраться с принт ---  нужно создать отдельную переменную с циклом


print (student_grades)
print (student_averages)
print (class_average)
print (letter_grades)