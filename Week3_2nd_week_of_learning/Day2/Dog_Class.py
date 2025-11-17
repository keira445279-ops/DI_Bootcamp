class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        counts = self.weight / (self.age *10)
        return counts

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            print (f"The winner is {self.name}")
            return self
        else:
            print (f"The winner is {other_dog.name}")
            return other_dog