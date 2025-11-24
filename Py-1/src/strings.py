# Рядок — незмінна послідовність символів
# Рядок (str) є незмінним (immutable) типом даних.
s = "Hello, World!"
print(s[0])      # Перший символ
# s[0] = 'h'  # Це викличе помилку, оскільки рядки незмінні

# Також можна вказувати «багаторядкові» літерали, використовуючи потрійні лапки (""" або ''').
multi_line = """This is a
multi-line
string."""
print(multi_line)

# Методи рядків

text = "  Hello, ItStep! Welcome to Python programming.  "
print(text.lower())        # Всі символи в нижньому регістрі    
print(text.upper())        # Всі символи в верхньому регістрі
print(text.strip())       # Видалення пробілів з початку і кінця рядка
print(text.replace("ItStep", "World"))  # Замінити підрядок
print(text.split())       # Розбиття рядка на список слів
print("ItStep" in text)   # Перевірка наявності підрядка
print(text.find("Python")) # Пошук підрядка, повертає індекс або -1
print(len(text))          # Довжина рядка
print(text.index("Python")) # Пошук підрядка, повертає індекс або викликає помилку
print(text.count("o"))    # Підрахунок кількості входжень підрядка
print(text.startswith("  Hello"))  # Перевірка початку рядка
print(text.endswith("programming.  "))  # Перевірка кінця рядка
print(text.capitalize())  # Перша літера велика, інші малі
print(text.title())       # Перша літера кожного слова велика
print(text.center(300, '-'))  # Вирівнювання по центру з заповненням
# Форматування рядків
name = "Alice"
age = 30
# Старий спосіб форматування
print("Name: %s, Age: %d" % (name, age))
# Новий спосіб форматування
print("Name: {}, Age: {}".format(name, age))
# Форматування з f-рядками (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# Форматування з вирівнюванням і точністю
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
name = "Alice"
age = 30
print(f"Left aligned: {name:<10} Age: {age}")
print(f"Right aligned: {name:>10} Age: {age}")

# Зріз рядка
s = "Hello, World!"
print(s[0:5])    # Перші 5 символів
print(s[7:])     # Від 7-го символу до кінця
print(s[:5])     # Від початку до 5-го символу  
print(s[-6:-1])  # Останні 6 до останнього символу
print(s[::2])    # Кожен другий символ
print(s[::-1])   # Рядок у зворотньому порядку

# «Сирі» рядки
raw_string = r"C:\new_folder\test.txt"
print(raw_string)  # Виведе: C:\new_folder\test.txt

# Форматування рядків з використанням f-рядків
user = "Bob"
balance = 1234.5678 
print(f"User: {user}, Balance: ${balance:,.2f}")  # Виведе: User: Bob, Balance: $1,234.57

# Регулярні вирази
import re   
pattern = r'\b\w{3}\b'  # Знайти всі слова з трьох літер
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches)  # Виведе: ['The', 'cat', 'sat', 'the', 'mat']

