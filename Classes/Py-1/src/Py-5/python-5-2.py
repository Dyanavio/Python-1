from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name) -> None:
        self.name = name
        print("Animal base class constructor")
    
    @abstractmethod
    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        return f"{self.name}: Mew"

class Dog(Animal):
    def voice(self):
        return f"{self.name}: Rvoof"

class Bird(Animal):
    def __init__(self, name, wingsSpan) -> None:
        super().__init__(name)
        self.wingsSpan = wingsSpan
        print("Bird constructor")

    def voice(self):
        return f"{self.name}: Kar"

dog = Dog("Sharick")
cat = Cat("Nefer")
bird = Bird("Crow", 20)

#print(dog.voice())
#print(cat.voice())
print(bird.name, bird.wingsSpan)
print(bird.voice())

print("\nLoop:")
animals = [dog, cat]
for animal in animals:
    print(animal.voice())

animal = Animal("Noname")