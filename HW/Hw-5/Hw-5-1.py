class Device:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.name}\n> Price: {self.price} $"
    
    def turnOn(self):
        print( f"{self.name} is working")

class CoffeeMachine(Device):
    def __init__(self, name: str, price: float, typesOfCoffee: list) -> None:
        super().__init__(name, price)
        self.__typesOfCoffee = typesOfCoffee
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n> Types of coffee supported: {self.__typesOfCoffee}"
    
    def turnOn(self):
        print( f"{self.name} is making a coffee")

class Blender(Device):
    def __init__(self, name: str, price: float, rotationsPerMinute: float, ingredients = []) -> None:
        super().__init__(name, price)
        self.__rotationsPerMinute = rotationsPerMinute
        self.__ingredients = ingredients
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n> Rotations per minute: {self.__rotationsPerMinute}\n> Ingredients: {self.__ingredients}"
    
    def clean(self):
        self.__ingredients = []

    def addIngredients(self, *ingredients: str):
        self.__ingredients.extend(ingredients)
    
    def turnOn(self):
        if len(self.__ingredients):
            print(f"{self.name} is blending ingredients")
        else:
            print(f"{self.name} has nothing to mix")
    
class MeatGrinder(Device):
    def __init__(self, name: str, price: float, power: float) -> None:
        super().__init__(name, price)
        self.__power = power
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n> Power: {self.__power} W"
    
    def turnOn(self):
        print( f"{self.name} is grinding whatever you placed")

    
coffeeMachine = CoffeeMachine("Machine A", 19.99, ["Latte", "Americano"])
blender = Blender("Blender B", 49.99, 400)
blender.addIngredients("Apple", "Lemon")
meatGrinder = MeatGrinder("Grinder C", 90, 4500)

print(coffeeMachine, '\n')
print(blender, '\n')
print(meatGrinder, '\n')

coffeeMachine.turnOn()
blender.turnOn()
meatGrinder.turnOn()

# Task - II
print("\nTASK - II\n")

class Ship:
    def __init__(self, name: str, enteredService: int, maxSpeed: float):
        self._name = name
        self._enteredService = enteredService
        self._maxSpeed = maxSpeed
    
    def __str__(self) -> str:
        return f"{self._name}\n> Entered service: {self._enteredService}\n> Max speed: {self._maxSpeed} kn"
    
    def sail(self):
        print(f"{self._name} set its sails")
    

class Frigate(Ship):
    def __init__(self, name: str, enteredService: int, maxSpeed: float, guns: int):
        super().__init__(name, enteredService, maxSpeed)
        self.__guns = guns
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n> Guns: {self.__guns} s"
    
    def sail(self):
        print(f"{self._name}'s captain gathered their crew")

class Destroyer(Ship):
    def __init__(self, name: str, enteredService: int, maxSpeed: float, fireDuration: int):
        super().__init__(name, enteredService, maxSpeed)
        self.__fireDuration = fireDuration
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n> Fire duration: {self.__fireDuration} s"
    
    def sail(self):
        print(f"{self._name} is on the move. The seas are doomed")

class Cruiser(Ship):
    def __init__(self, name: str, enteredService: int, maxSpeed: float, fate: str):
        super().__init__(name, enteredService, maxSpeed)
        self.__fate = fate
    
    def __str__(self) -> str:
       return f"{super().__str__()}\n> Fate: {self.__fate} s"
    
    def sail(self):
        print(f"{self._name} met its fate: {self.__fate}")

destroyer = Destroyer("Myogi", 1910, 28, 60)
frigate = Frigate("Magicienne", 1777, 10, 32)
cruiser = Cruiser("USS Cleveland", 1941, 32.5, "Sold for scrap 18 February 1960")

print(destroyer, '\n')
print(frigate, '\n')
print(cruiser, '\n')

destroyer.sail()
frigate.sail()
cruiser.sail()


# Task - III
print("\nTASK - III\n")
class Money:
    def __init__(self, currency: str, amount: float):
        self._currency = currency
        self._whole = int(amount)
        self._fractional = int((amount - int(amount)) * 100)

    @property
    def whole(self):
        return self._whole

    @whole.setter
    def whole(self, value):
        self._whole = value

    @property
    def fractional(self):
        return self._fractional
    
    @fractional.setter
    def fractional(self, value):
        self._fractional = value
    
    def __str__(self) -> str:
        return f"{self._currency}: {self._whole}.{self._fractional}"
    
class Product(Money):
    def __init__(self, name: str, currency: str, amount: float):
        super().__init__(currency, amount)
        self.__name = name

    def __str__(self) -> str:
        return f"{self.__name}\n> {super().__str__()}"

    def reduceBy(self, amount: float):
        self._whole -= int(amount)
        self._fractional -= int((amount - int(amount)) * 100)

    
money = Money("Pound Sterling", 19.9)
print(money)

money.whole = 25
money.fractional = 5
print(money)

product = Product("Vine", "Pound Sterling", 59.99)
print('\n', product)

product.reduceBy(15.35)
print('\n', product)