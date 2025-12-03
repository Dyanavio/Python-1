# Task - I and II
import math

'''
Создайте базовый класс Shape с методом вычисления площади. Создайте произ­водные классы: прямоугольник, круг, правильный треугольник, трапеция с собственными методами вычисления площади.

Переопределите методы int (возвращает площадь) и str (возвращает информацию о фигуре) из задания 1.
'''

class Shape:
    def __init__(self):
        self._type = 'Geometrical figure'

    def __str__(self) -> str:
        return f"{self._type}\n> Area: {self.area()}"
    
    def __int__(self) -> int:
        return self.area()

    def area(self) -> float:
        return None
    
class Rectangle(Shape):
    def __init__(self, side: float):
        self._type = 'Rectangle'
        self._side = side

    def __str__(self) -> str:
        return f"{self._type}\n> Side: {self._side}\n> Area: {self.__int__()}"


    def area(self) -> float:
        return self._side ** 2

class Circe(Shape):
    def __init__(self, radius: float):
        self._type = 'Circle'
        self._radius = radius
    
    def __str__(self) -> str:
        return f"{self._type}\n> Radius: {self._radius}\n> Area: {self.__int__()}"

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

class RightTriangle(Shape):
    def __init__(self, sideA: float, sideB: float):
        self._type = 'Right Triangle'
        self._sideA = sideA
        self._sideB = sideB

    def __str__(self) -> str:
        return f"{self._type}\n> Side A: {self._sideA}\n> Side B: {self._sideB}\n> Area: {self.__int__()}"

    def area(self) -> float:
        return (self._sideA * self._sideB) / 2

class Trapezoid(Shape):
    def __init__(self, baseA: float, baseB: float, height: float):
        self._type = 'Trapezoid'
        self._baseA = baseA
        self._baseB = baseB
        self._height = height

    def __str__(self) -> str:
        return f"{self._type}\n> Base A: {self._baseA}\n> Base B: {self._baseB}\n> Height: {self._height}\n> Area: {self.__int__()}"

    def area(self) -> float:
        return ((self._baseA + self._baseB) / 2) * self._height


abstractShape = Shape()
circle = Circe(5)
rectangle = Rectangle(5)
triangle = RightTriangle(3, 4)
trapezoid = Trapezoid(5, 7, 4)

print(abstractShape)
print('\n', circle)
print('\n', rectangle)
print('\n', triangle)
print('\n', trapezoid)

