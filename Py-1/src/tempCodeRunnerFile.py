# Функції map(), filter(), zip()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map():", squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped lists using zip():", zipped)