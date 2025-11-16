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

print (student_grades)
print (student_averages)
print (f'Class average score is {class_average}')
print (letter_grades)

max_name_length = max(len(key) for key in student_grades.keys())

for key in student_grades.keys():
    spaces = ' ' * (max_name_length - len(key))
    print(f"{key}:{spaces} Average Grade = {student_averages[key]:.2f}, Letter Grade = {letter_grades[key]}")


# EXERCISE 2 : Advanced Data Manipulation and Analysis
# Instructions
# In this exercise, you will analyze data from a hypothetical online retail company to gain insights 
# into sales trends and customer behavior. The data is represented as a list of dictionaries, 
# where each dictionary contains information about a single purchase.

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Tasks:
# Total Sales Calculation: Calculate the total sales for each product category 
# (i.e., the total revenue generated from each type of product). 
# Use a loop to iterate through the data and a dictionary to store the total sales for each product.

sales_calculation = {}
for item in sales_data:
    revenue = item['price'] * item ['quantity']
    if item['product'] not in sales_calculation:
        sales_calculation.update({item["product"] : revenue})
    else:
        sales_calculation [item["product"]] += revenue

print (sales_calculation)

# Customer Spending Profile: Determine the total amount spent by each customer. 
# Use a dictionary to maintain the sum of amounts each customer has spent.

total_spent_amount = {}

for item in sales_data:
    total_amount = item["price"] * item["quantity"]
    if item['customer_id'] not in total_spent_amount:
        total_spent_amount.update({item["customer_id"] : total_amount})
    else:
        total_spent_amount[item["customer_id"]] += total_amount

print(total_spent_amount)

# Sales Data Enhancement:
# Add a new field to each transaction called “total_price” that represents the total price 
# for that transaction (quantity * price).
# Use a loop to modify the sales_data list with this new information.

for item in sales_data:
    revenue = item["price"] * item["quantity"]
    item.update({'total_price' : revenue})

print(sales_data)

# High-Value Transactions:
# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.

transactions = []

for item in sales_data:
    if item['total_price'] > 500:
        transactions.append(item["total_price"])

for item in sales_data:
    print(item['total_price'])
print(transactions)

# Customer Loyalty Identification:
# Identify any customer who has made more than one purchase, suggesting potential loyalty.
# Use a dictionary to count purchases per customer, then use a loop or comprehension 
# to identify customers meeting the loyalty criterion.

loyal_customers = {}

for item in sales_data:
    if item["customer_id"] not in loyal_customers:
        loyal_customers[item["customer_id"]] = 1
    else:
        loyal_customers[item["customer_id"]] += 1

for key,value in loyal_customers.items():
    if value > 1:
        print (f'Customer {key} is loyal, because he made {value} purchases')
    else:
        print (f'Customer {key} is not loyal, because he made only {value} purchase')


# Bonus: Insights and Analysis:
# Calculate the average transaction value for each product category.
# Identify the most popular product based on the quantity sold.
# Provide insights into how these analyses could inform the company’s marketing strategies.

average_transaction = {}

for item in sales_data:
    average_price = (item["price"] * item["quantity"])
    if item["product"] not in average_transaction:
        average_transaction.update({item["product"] : [average_price, item["quantity"]]})
    else:
        average_transaction[item["product"]][0] += average_price
        average_transaction[item["product"]][1] += item["quantity"]

for key, value in average_transaction.items():
    average_transaction.update({key : (value[0]/value[1])})

print(average_transaction)


# # Key Python Topics:
# # Functions
# # Strings
# # .split() method
# # Loops (for)
# # Conditional statements (if)
# # String length (len())