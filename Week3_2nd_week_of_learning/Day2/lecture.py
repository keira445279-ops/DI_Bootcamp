class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs

    def sleep(self):
        return f'{self.name} is sleeping - ANIMAL'
    
class Cat(Animal):
    def __init__(self, name, family, legs, friendly, indoor):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.indoor = indoor

cat1 = Cat('Funny', 'Felidae', 4, True, True)
print(cat1.indoor)
print(cat1.__dict__)