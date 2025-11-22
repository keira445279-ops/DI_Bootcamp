# Your goal is to create a program to help a city with the vaccination of its citizens.

# Part 1
# You will have to create two classes:
# Human
# Queue

# Human
# Represents a citizen of the city, it has the following attributes: 
# id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.
# This class has no methods.

# Create an attribute family for the Human class.
# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.

class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def __repr__(self):
        return f"{self.name} has a blood type {self.blood_type}"

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)

# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.

class Queue:
    def __init__(self, humans = None):

        blood_type = ['A', 'B', 'AB', 'O']

        if humans is None:
            humans = []
        
        self.humans = humans
        
        
# This class is useful to manage who will get vaccinated in priority. It has the following methods:

# add_person(self, person) : 
# Adds a human to the queue, if he is older than 60 years old or a priority person,
#  put him at the beginning of the list (at index 0) before every other.

    def add_person(self, person):
        if person.age > 60 or person.priority is True:
            self.humans.insert(0,person)
        else:
            self.humans.append(person)

# find_in_queue(self, person) : Returns the index of a human in the queue.

    def find_in_queue(self, person):
        return self.humans.index(person)

# swap(self, person1, person2): Swaps person1 with person2.

    def swap(self, person1, person2):
        index1 = self.humans.index(person1) 
        index2 = self.humans.index(person2)
        self.humans[index1] = person2
        self.humans[index2] = person1
        return self.humans

# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        return None

# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.

    def get_next_blood_type(self, blood_type):
        for i,h in enumerate(self.humans):
            if h.blood_type == blood_type:
                return self.humans.pop(i)
        return None

# Add the rearrange_queue(self) method to the Queue class, 
# so that there won’t be two members of the same family one after the other in the line.

    def rearrange_queue(self):
        for i in range(len(self.humans) -1):
            if self.humans[i+1] in self.humans[i].family:
                for j in range(i+2,len(self.humans)):
                    if self.humans[j] not in self.humans[i].family:
                        self.humans[i+1], self.humans[j] = self.humans[j], self.humans[i+1]
                        break



# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people
# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).

    def sort_by_age(self):
        self.humans.sort(key = lambda h: (not -h.priority, -h.age))


# ****************** outputs **************************************

per1 = Human(1, 'Emma', 25, True, 'A')
per2 = Human(2, 'Liam', 72, False, 'B')
per3 = Human(3, 'Olga', 45, False, 'O')


fam1 = Human (1, 'Frodo', 47, True, 'AB')
per1.add_family_member(fam1)
print([f.name for f in per1.family])

# queue = Queue()

# queue.add_person(per1)
# queue.add_person(per2)
# queue.add_person(per3)

# result = queue.find_in_queue(per2)

# queue.swap(per1,per2)

# result2=queue.get_next_blood_type('O')

# print([h.name for h in queue.humans])
# print(result)
# print(result2)





