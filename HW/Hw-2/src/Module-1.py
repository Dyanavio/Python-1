import random

# Task - I
length = 10
tuple1 = tuple(random.randint(0,10) for x in range(length))
tuple2 = tuple(random.randint(0,10) for x in range(length))
tuple3 = tuple(random.randint(0,10) for x in range(length))

print("Tuple 1: ", tuple1)
print("Tuple 2: ", tuple2)
print("Tuple 3: ", tuple3)

set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)

elementsInAllTuples = set1.intersection(set2).intersection(set3)
print(f"Elements that are in all tuples: {elementsInAllTuples}")

# Task - II
uniqueForEach = set1.symmetric_difference(set2).difference(set1.intersection(set3)).difference(set2.intersection(set3)).union(set3.difference(set1).intersection(set3.difference(set2)))
print(f"Elements that are unique for each set: {uniqueForEach}")


# Task - III
samePositionElements = set()
for i in range(length):
    if(tuple1[i] == tuple2[i] == tuple3[i]):
        samePositionElements.add(tuple1[i])
print(f"Elements with same value and position: {samePositionElements}")