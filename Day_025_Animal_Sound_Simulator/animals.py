class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError
    

class Dog(Animal):
    def speak(self):
        return "Wolf!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    def speak(self):
        return "Moo!"
    
animals = [Dog("Tommy"),Cat("Pony"),Cow("Daisy")]

for animal in animals:
    print(f"{animal.name} says {animal.speak()}")