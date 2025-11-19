# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.



# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'This is a circle with radius {self.radius}'
    
    def __repr__(self):
        return f'Circle ({self.radius})'
    
    def __add__(self,other):
        return Circle(self.radius + other.radius)
    
    def __gt__(self,other):
        return self.radius > other.radius

    def __eq__(self,other):
        return self.radius == other.radius  

    def __lt__(self,other):
        return self.radius < other.radius  
    

cir1 = Circle(10)
cir2 = Circle(15)

print(str(cir1))
 
print(repr(cir1))

print(cir1 + cir2)

print(cir1 > cir2)

print(cir1 == cir2)

circles = [cir1, cir2, Circle(26)]
circles.sort()



