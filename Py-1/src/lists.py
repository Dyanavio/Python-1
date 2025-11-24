# Списки
# Створення списку
fruits = ["apple", "banana", "cherry"]
print(fruits)
# функція конструктор списку list()
numbers = list(range(5))  # Створює список [0, 1, 2, 3, 4]
print(numbers)

# Доступ до елементів списку
print(fruits[0])  # Перший елемент
print(fruits[-1]) # Останній елемент
# Зміна елементів списку
fruits[1] = "blueberry"
print(fruits)
# Додавання елементів до списку
fruits.append("date")
print(fruits)
fruits.insert(1, "orange")  # Вставка на позицію 1
print(fruits)
# Видалення елементів зі списку
fruits.remove("cherry")  # Видалення за значенням
print(fruits)
del fruits[0]  # Видалення за індексом
print(fruits)
popped_fruit = fruits.pop()  # Видалення останнього елемента
print(popped_fruit)
print(fruits)
# Перевірка наявності елемента  
print("banana" in fruits)
# Довжина списку
print(len(fruits))
# Ітерація по списку
for fruit in fruits:
    print(fruit)
# Сортування списку
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# Зворотній порядок списку
fruits.reverse()
print(fruits)
# Копіювання списку. Тут створюється новий список з тими ж елементами.
new_fruits = fruits.copy()
print(new_fruits)
# Але якщо просто присвоїти список іншій змінній, обидві змінні будуть посилатися на один і той же список.
another_fruits = fruits
# Очищення списку
fruits.clear()
print(fruits)
print(new_fruits)
# Зрізи списку
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])    # Елементи з індексами від 2 до 4
print(numbers[:4])     # Перші 4 елементи       
print(numbers[5:])     # Від 5-го елемента до кінця
print(numbers[-5:])    # Останні 5 елементів
print(numbers[::2])    # Кожен другий елемент
print(numbers[::-1])   # Список у зворотньому порядку   
# Вкладені списки
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # Доступ до елемента 2
print(matrix[2])     # Доступ до третього рядка
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

# Списки можуть містити елементи різних типів
mixed_list = [1, "two", 3.0, True, [5, 6]]
print(mixed_list)
# Перетворення рядка в список
s = "Hello, World!"
char_list = list(s)
print(char_list)
# Перетворення списку в рядок
joined_string = ''.join(char_list)
print(joined_string)

# Для роботи зі списками можна використовувати такі вбудовані функції Python:
numbers = [5, 2, 9, 1, 5, 6]
print(min(numbers))    # Мінімальне значення
print(max(numbers))    # Максимальне значення
print(sum(numbers))    # Сума елементів
print(sorted(numbers)) # Відсортований список
print(list(reversed(numbers))) # Список у зворотньому порядку

# Генератори списків
squares = [x ** 2 for x in range(10)]
print(squares)
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)