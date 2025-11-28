# Task - I
def fibonacci(begin, end):
    current = 0
    previous = 0
    
    while current <= end:
        if current >= begin:
            yield current
        if current == 0:
            current = 1
            yield current
        temp = current
        current += previous
        previous = temp

print(f"Fibonnaci numbers in range: {list(fibonacci(0, 144))}\n\n")

# Task - II
def sumOfLists(list1: list, list2: list):
    resultingList = []
    minLength = min(len(list1), len(list2))
    for i in range(0, minLength):
        resultingList.append(list1[i] + list2[i])
    resultingList.extend(list1[minLength:]) if len(list1) > len(list2) else resultingList.extend(list2[minLength:])
    return resultingList


list1 = [1, 3, 4, 2]
list2 = [8, 3, 5, 9]
list3 = [4, 6, 2, 8, 5, 7, 10, 5]

print(f"List1 + List2: {sumOfLists(list1, list2)}")
print(f"List1 + List3: {sumOfLists(list3, list1)}\n\n")

# Task - III
def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def calculate(lst: list, operation):
    for i in range(0, len(lst)):
        lst[i] = operation(lst[i])
    return lst

lstSquare = [4, 6, 2, 8, 5, 7, 10, 5]
lstCube = [4, 6, 2, 8, 5, 7, 10, 5]
print(f"Square: {calculate(lstSquare, square)}")
print(f"Cube: {calculate(lstCube, cube)}\n\n")

# Task - IV
from datetime import datetime

def decorator():
    def inner(func):
        def wrapper(expenses, companyName):
            positions = func(expenses)
            if companyName == "Company A":
                for i in range(0, len(positions)):
                    positions[i] += f"{'':10} Signed by director"
            elif companyName == "Company B":
                for i in range(0, len(positions)):
                    positions[i] += f"{'':10} Timestamp: {datetime.now()}"
            report = ""
            for i in range(0, len(positions)):
                report += f"{positions[i]}\n"
            return report
        return wrapper
    return inner

def generateReport(expenses: __dict__):
    points = []
    for key, value in expenses.items():
        points.append(f"{key:10} | {value}")
    return points

expenses = {"Equipment": 1100, "Decorations": 400, "Provision": 900}
print(f"Report for Company A:\n{decorator()(generateReport)(expenses, "Company A")}\n")
print(f"Report for Company B:\n{decorator()(generateReport)(expenses, "Company B")}")