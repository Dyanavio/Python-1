# Task - I
def odds(begin, end):
    while begin < end:
        if begin % 2 != 0:
            yield begin
        begin += 1

print(f"All odd numbers in range: {list(odds(2, 21))}")

# Task - II
def notIncluded(begin, end, values):
    while begin < end:
        if not values.__contains__(begin):
            yield begin
        begin += 1

print(f"Not included in list: {list(notIncluded(2, 21, [5,6,8,11,19]))}")

# Task - III
def horizontalLine(symbol):
    print(symbol * 10)

def verticalLine(symbol):
    for i in range(0, 10):
        print(symbol)

def showLine(symbol, outputType):
    outputType(symbol)

showLine('=', horizontalLine)
showLine('+', verticalLine)

#Task IV - V
import time

def decorator():
    def inner(counterFunction):
        def wrapper(begin, end):
            beginTimestamp = time.time()
            result = list(counterFunction(begin, end))
            endTimestamp = time.time()
            print(f"Duration: {endTimestamp - beginTimestamp} s\nEven numbers in range [{begin}, {end}]: {result}")
        return wrapper
    return inner

def evens(begin, end):
    while begin < end:
            if begin % 2 == 0:
                yield begin
            begin += 1
    
decorator()(evens)(1, 1000)