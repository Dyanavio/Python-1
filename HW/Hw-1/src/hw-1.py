import random

def output(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])

def transpose(matrix):
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def swapDiagonals(matrix):
    for i in range(0, len(matrix)):
        matrix[i][i], matrix[i][len(matrix) - i - 1] = matrix[i][len(matrix) - i - 1], matrix[i][i]

def sumInBetween(matrix):
    minIndice = minInMatrix(matrix)
    maxIndice = maxInMatrix(matrix)
    start = []
    end = []
    sum = 0

    if minIndice[0] == maxIndice[0]:
        if(minIndice[1] < maxIndice[1]): 
            start = minIndice
            end = maxIndice
        else: 
            start = maxIndice
            end = minIndice
    else:
        if minIndice[0] < maxIndice[0]: 
            start = minIndice
            end = maxIndice
        else: 
            start = maxIndice
            end = minIndice

    for i in range(start[0], end[0] + 1):
        for j in range(start[1] + 1, end[1]):
            sum += matrix[i][j]

    return sum

def minInMatrix(matrix):
    min = matrix[0][0]
    index1 = 0
    index2 = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] < min: 
                min = matrix[i][j]
                index1 = i
                index2 = j
    return [index1, index2]
    

def maxInMatrix(matrix):
    max = matrix[0][0]
    index1 = 0
    index2 = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] > max: 
                max = matrix[i][j]
                index1 = i
                index2 = j
    return [index1, index2]

#1) Дано двомірний масив розміром 5х5, заповнений випадковими числами з діапазону від 0 до 100. Поміняти місцями елементів масиву, розташовані симетрично відносно головної діагоналі.\n
size = 5
matrix = [[random.randint(0, 100) for i in range(0, size)] for j in range(0, size)]
print("Task I\nInitial:")
output(matrix)

transpose(matrix)
print("After transposition:")
output(matrix)

#2) Дано двомірний масив розміром 5х5, заповнений випадковими числами з діапазону від 0 до 100. Поміняти місцями елементи масиву, розташовані по головній діагоналі, з елементами масиву, розташовані по боковій діагоналі.
matrix = [[random.randint(0, 100) for i in range(0, size)] for j in range(0, size)]
print("\n\nTask II\nInitial:")
output(matrix)

swapDiagonals(matrix)
print("After swapping diagonals:")
output(matrix)


#3) Дано двомірний масив розміром 5х5, заповнений випадковими числами з діапазону від -100 до 100. Визначити суму елементів масиву, розташованих між мінімальними та максимальними елементами.
matrix = [[random.randint(-100, 100) for i in range(0, size)] for j in range(0, size)]
print("\n\nTask III\nInitial:")
output(matrix)

print(f"Min: ({minInMatrix(matrix)[0]}, {minInMatrix(matrix)[1]}) {matrix[minInMatrix(matrix)[0]][minInMatrix(matrix)[1]]}")
print(f"Max: ({maxInMatrix(matrix)[0]}, {maxInMatrix(matrix)[1]}) {matrix[maxInMatrix(matrix)[0]][maxInMatrix(matrix)[1]]}")
print(f"\nSum of all elements between min and max: {sumInBetween(matrix)}")
