# Task - I
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def __str__(self) -> str:
        return f"R = {self.radius} unit(s)"
    
    def __eq__(self, other: Circle):
        return self.radius == other.radius
    
    def __lt__(self, other: Circle):
        return self.radius < other.radius
    
    def __gt__(self, other: Circle):
        return self.radius > other.radius
    
    def __le__(self, other: Circle):
        return self.radius <= other.radius
    
    def __ge__(self, other: Circle):
        return self.radius >= other.radius
    
    def __add__(self, other: float):
        return Circle(self.radius + other)
    
    def __radd__(self, other: float):
        return Circle(self.radius + other) 
    
    def __iadd__(self, other: float):
        self.radius += other
        return self
    
    def __sub__(self, other: float):
        result = self.radius - other
        return Circle(result if result > 0 else 0)
    
    def __rsub__(self, other: float):
        result = self.radius - other
        return Circle(result if result > 0 else 0)
    
    def __isub__(self, other: float):
        if self.radius - other >= 0:
            self.radius -= other
        return self
    
circle1 = Circle(5)
circle2 = Circle(5)
circle3 = Circle(10)

print(f"Circle I == Circle II: {circle1 == circle2}")
print(f"Circle I == Circle III: {circle1 == circle3}")

print(f"Circle I < Circle II: {circle1 < circle2}")
print(f"Circle I <= Circle II: {circle1 <= circle2}")
print(f"Circle I > Circle III: {circle1 > circle3}")

print(f"Circle I + 5: {circle1 + 5}")
print(f"Circle III - 5: {circle3 - 5}")
circle1 -= 4
print(f"Circle I -= 4: {circle1}", '\n')


# Task - II

class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        return f"{self.real} {'+' if self.imaginary > 0 else '-'} {abs(self.imaginary)}i"
    
    def __add__(self, other: Complex):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other: Complex):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other: Complex):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + other.real * self.imaginary)
    
    def __truediv__(self, other: Complex):
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / ((other.real ** 2) + (other.imaginary ** 2)), 
                       (self.imaginary * other.real - other.imaginary * self.real) / ((other.real ** 2) + (other.imaginary ** 2)))
    
z1 = Complex(2, -5)
z2 = Complex(5, 10)
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 - z2 = {z1 - z2}")
print(f"z1 * z2 = {z1 * z2}")
print(f"z1 / z2 = {z1 / z2}", '\n')


# Task - III
class Airplane:
    def __init__(self, type: str, capacity: int):
        self.type = type
        self.capacity = capacity
        self.current = 0

    def __str__(self) -> str:
        return f"{self.type}\n> Capacity: {self.capacity}\n> Current: {self.current}"
    
    def __eq__(self, other):
        return self.type == other.type

    def __add__(self, other: int):
        result = self.current + other
        return Airplane(self.type, result if result <= self.capacity else self.capacity)
    
    def __radd__(self, other: int):
        result = self.current + other
        return Airplane(self.type, result if result <= self.capacity else self.capacity)
    
    def __iadd__(self, other: int):
        result = self.current + other
        self.current += other if result <= self.capacity else self.capacity
        return self
    
    def __sub__(self, other: int):
        result = self.current - other
        return Airplane(self.type, result if result >= 0 else 0)
    
    def __rsub__(self, other: int):
        result = self.current - other
        return Airplane(self.type, result if result >= 0 else 0)
    
    def __isub__(self, other: int):
        result = self.current - other
        self.current = result if result >= 0 else 0
        return self
    
    def __lt__(self, other: Airplane):
        return self.capacity < other.capacity
    
    def __gt__(self, other: Airplane):
        return self.capacity > other.capacity
    
    def __le__(self, other: Airplane):
        return self.capacity <= other.capacity
    
    def __ge__(self, other: Airplane):
        return self.capacity >= other.capacity
    
airplane1 = Airplane("Antonov", 60)
airplane2 = Airplane("Antonov", 50)

print(f"Airplane I:\n", airplane1, '\n')
print(f"Airplane II:\n", airplane2, '\n')
print(f"Type check: {airplane1 == airplane2}")
print(f"Airplane I > Airplane II: {airplane1 > airplane2}")
print(f"Airplane I < Airplane II: {airplane1 < airplane2}")
airplane1 += 30
airplane2 += 10
print(f"Airplane I:\n", airplane1, '\n')
print(f"Airplane II:\n", airplane2, '\n')

# Task - IV
'''
Создайте класс Flat (Квартира). Реализуйте перегруженные операторы:
проверку на равенство площадей квартир (операция ==);
проверку на неравенство площадей квартир (операция !=);
сравнение двух квартир по цене (операции >, <, <=, >=).
'''

class Flat:
    def __init__(self, area: float, price: float):
        self.area = area
        self.price = price

    def __str__(self) -> str:
        return f"{self.area} m^2   |   ${self.price}"
    
    def __eq__(self, other: Flat):
        return self.area == other.area
    
    def __ne__(self, other: Flat):
        return self.area != other.area
    
    def __lt__(self, other: Flat):
        return self.price < other.price
    
    def __gt__(self, other: Flat):
        return self.price > other.price
    
    def __le__(self, other: Flat):
        return self.price <= other.price
    
    def __ge__(self, other: Flat):
        return self.price >= other.price
    
flat1 = Flat(15.5, 3200)
flat2 = Flat(15.5, 15500)
flat3 = Flat(10, 3400)

print(f"Flat I: {flat1}")
print(f"Flat II: {flat2}")
print(f"Flat III: {flat3}")

print(f"Area check == (I and II): {flat1 == flat2}")
print(f"Area check == (I and III): {flat1 == flat3}")
print(f"Area check != (I and III): {flat1 != flat3}")
print(f"Price check < (I and III): {flat1 < flat3}")
print(f"Price check > (II and III): {flat2 > flat3}")
