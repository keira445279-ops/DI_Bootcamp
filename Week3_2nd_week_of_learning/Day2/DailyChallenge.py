# *****************************************Daily Challenge : Pagination*******************************************
# Step 1: Create the Pagination Class
# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.

# Step 2: Implement the __init__ Method
# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page

# Behavior:
# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.

import math

class Pagination:
    def __init__(self, items = None, page_size = 10):
        if items is None:
            items = []

        self.items = items
        self.page_size = page_size
        self.current_ind = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)



# Step 3: Implement the get_visible_items() Method
# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.
    def get_visible_items(self):
        start = self.page_size * self.current_ind # 10*0 we are making indexes of items from 0 to 10
        end = start + self.page_size # 0+10
        return self.items[start:end]
        

# Step 4: Implement Navigation Methods
# These methods should help navigate through pages:
# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError
        else:
            self.current_ind = page_num - 1 # we have dofferent start positions: for current_ind it is 0 and for page_num it is 1
            return self.get_visible_items()

# first_page()
# → Navigates to the first page.

    def first_page(self):
        return self.go_to_page(1)
         
# last_page()
# → Navigates to the last page.

    def last_page(self):
        return self.go_to_page (self.total_pages)

# next_page()
# → Moves one page forward (if not already on the last page).

    def next_page(self):
        if self.current_ind < self.total_pages-1:
            return self.go_to_page (self.current_ind +2) # because current_ind = 0, we print 1

# previous_page()
# → Moves one page backward (if not already on the first page).

    def previous_page(self):
        if self.current_ind > 0:
            return self.go_to_page (self.current_ind)
        else:
            print ('There is no previous page')
            return self.get_visible_items() 

# Note:
# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.

# Step 5: Add a Custom __str__() Method
# This magic method should return a string displaying the items on the current page, each on a new line.

    def __str__(self):
        return '\n'.join(self.get_visible_items())


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.go_to_page(3)
print(p.get_visible_items())


p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError:
    print("Page 10 is out of range")
    #print(p.current_ind + 1)
    # Output: ValueError

try:
    p.go_to_page(0)
except ValueError:
    print("Page 0 is out of range")
# Raises ValueError
