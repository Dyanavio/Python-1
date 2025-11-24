# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
# python -m venv venv

print('hello world')
print('one', 'two', 'three', sep='---', end='!!!\n')

# Літерали — це дані, значення яких визначаються самим літералом.
print(42)          # Ціле число (integer literal)
print(3.14)       # Дійсне число (floating-point literal)   
print("Hello")    # Рядок (string literal) або 'Hello'
print(True)      # Булеве значення (boolean literal)
print('University \"ItStep\"')  # Екранування лапок всередині рядка
print('University "ItStep"')  # Або можна так

# Основні оператори
print(2 ** 3) # піднесення до степеня
print(2 * 3) # множення
print(7 / 2) # ділення
print(7 // 2) # цілочисельне ділення
print(7 % 2) # остача від ділення
print(5 + 3) # додавання
print(5 - 3) # віднімання

# Змінні
# Python є динамічно типізованою мовою програмування, а це означає, що вам не потрібно оголошувати змінні.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

i=1
# i++  # Це не працює в Python
i+=1  # Правильний спосіб збільшити i на 1

# Функція введення input() 3 
# code-runner.runInTerminal встановлено в true в налаштуваннях VS Code для підтримки введення користувача.
name = input("Enter your name: ")
print("Hello,", name)

a=input("Enter a: ")
b=input("Enter b: ")
# результат функції input() — це рядок.
print("a + b =", a + b)  # Це конкатенація рядків

# Щоб виконати арифметичне додавання, потрібно перетворити рядки в числа.
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("a + b =", a + b)  # Це додавання чисел
