# Функції в Python
# Функції дозволяють організувати код у блоки, які можна повторно використовувати.
# Вбудовані функції
print("Hello, World!")  # Виведення тексту на екран
length = len("Hello")   # Отримання довжини рядка
print("Length of 'Hello':", length)
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)     # Обчислення суми елементів списку
print("Sum of numbers:", total)
# функція type()
print("Type of 42:", type(42))
print("Type of 3.14:", type(3.14))
print("Type of 'Hello':", type("Hello"))
print("Type of [1, 2, 3]:", type([1, 2, 3]))
# Визначення власної функції
def greet(name):
    """Функція для привітання користувача за ім'ям."""
    return f"Hello, {name}!"
message = greet("Alice")
print(message)

# Математичні функції та випадкові числа
import math
import random
print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))
# Функція randrange()
print("Random even number between 0 and 20:", random.randrange(0, 21, 2))
# Функція choice()
colors = ["red", "green", "blue", "yellow"]
print("Random color:", random.choice(colors))
# Функції з кількома аргументами та значеннями за замовчуванням
def power(base, exponent=2):
    """Піднесення числа base до степеня exponent."""
    return base ** exponent
print("3 squared is:", power(3))
print("2 to the power of 3 is:", power(2, 3))
# Функції з довільною кількістю аргументів
def summarize(*args):
    """Повертає суму всіх переданих аргументів."""
    return sum(args)
print("Sum of 1, 2, 3, 4 is:", summarize(1, 2, 3, 4))
# Лямбда-функції (анонімні функції) можна використовувати для коротких функцій, що складаються з одного виразу.
square = lambda x: x ** 2
print("Square of 5 using lambda:", square(5))

# Python функції — це об'єкти першого класу
# Функція називається функцією вищого порядку, якщо вона приймає іншу функцію (функції) в якості аргументів та (або) повертає функцію в результаті своєї роботи.
def apply_function(func, value):
    """Застосовує функцію func до значення value."""
    return func(value)
result = apply_function(lambda x: x + 10, 5)
print("Result of applying function:", result)

# Функції map(), filter(), zip()

# Вбудована функція map() дозволяє застосовувати потрібну функцію до кожного елемента колекції (об'єкта, що ітерується, наприклад, списку). Результат, що повертається — новий ітератор (об'єкт map), який потім можна передати, наприклад, у вбудовану функцію list() для створення списку результатів.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map():", squared)
# Функція filter() приймає два аргументи: функцію, яка реалізує (описує) умову фільтрації і повертає логічні значення (true або false), і об'єкт, що ітерується, кожен елемент якого буде перевірятися умовою фільтра. Якщо в результаті такої перевірки елемента функція-перевірка поверне true, він буде включений в результат роботи фільтра.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)
# Функція zip() приймає колекції, що ітеруються, як аргументи і повертає ітератор. Цей ітератор генерує серію кортежів, які містять елементи кожного об'єкта-аргументу функції zip()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped lists using zip():", zipped)
