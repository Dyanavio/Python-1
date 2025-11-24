# 1 Логічні операції

# and
competent = True
responsible = False
print(competent and responsible)

# or
print(competent or responsible)

# not
print(not competent)

# 2 Оператори розгалуження if …else
age = 12
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# elif
score = 85  
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# Вкладені умови
num = 15    
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
        print("Positive odd number")
else:
    print("Non-positive number")

# 3 Тернарний оператор
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

i = 1
match i:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Default")

# 4 Цикли

# чистом синтаксисе Python нет встроенного оператора do...while цикла, как в языках программирования C, C++ или Java.
# В Python есть только два основных типа циклов:
# for: для итерации по последовательностям (списки, строки, диапазоны и т.д.).
# while: для выполнения блока кода до тех пор, пока условие истинно.

# while
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# for
# Цикли типу «for», на відміну від «while», повторюються не залежно від виконання умови, для кожного елемента у списку, множині, кортежі або іншій сукупності елементів
for i in range(5):
    print("Iteration:", i)

#  Ітерація по рядку
for char in "Hello":
    print(char)

# Ітерація по списку
fruits = ["apple", "banana", "cherry"]  
for fruit in fruits:
    print(fruit)

# Використання break і continue
for i in range(10):
    if i == 5:
        break  # вихід з циклу, коли i дорівнює 5
    if i % 2 == 0:
        continue  # пропуск парних чисел
    print("Odd number:", i)

# Використання else з циклами. «else» в циклах виконується у разі, якщо цикл було успішно завершено.
for i in range(3):
    print("Iteration:", i)
    # if i == 2: 
    #     break
else:
    print("Loop completed without break.")