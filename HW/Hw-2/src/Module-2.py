#Task - I
def create(dictionary, key, value):
    dictionary[key] = value

def read(dictionary):
    for key, value in dictionary.items():
        print(f"  -  {key:20} | {value}")

def update(dictionary, key, newValue):
    if dictionary.__contains__(key):
        dictionary[key] = newValue
    else:
        print("Not found")

def delete(dictionary, key):
    if dictionary.__contains__(key):
        del dictionary[key]
    else:
        print("Not found")

def find(dictionary, key):
    if dictionary.__contains__(key):
        return (key, dictionary[key])
    else:
        return ()
    
def replace(dictionary, oldKey, newKey):
    if dictionary.__contains__(oldKey):
        dictionary[newKey] = dictionary.pop(oldKey)
    else:
        print("Not found")
        

# Task - 1
basketballPlayers = {"Gheorghe Muresan": 2.31, "Manute Bol": 2.31, "Bol Bol": 2.21}
print("Task - I\n")
read(basketballPlayers)

create(basketballPlayers, "Player A", 2.45)
print("\nAfter create:")
read(basketballPlayers)

update(basketballPlayers, "Gheorghe Muresan", 2.30)
print("\nAfter update:")
read(basketballPlayers)

delete(basketballPlayers, "Manute Bol")
print("\nAfter delete:")
read(basketballPlayers)

replace(basketballPlayers, "Bol Bol", "Bol Bol Bol")
print("\nAfter replace:")
read(basketballPlayers)

print(f"Find Bol Bol: {find(basketballPlayers, "Bol Bol Bol")}")

# Task - 2
angloFranc = {"calculator": "calculatrice", "Cartesian plane": "plan cartésien", "object": "solide", "Venn diagram": "diagramme de Venn", "vertex": "sommets", "tails(coin)": "pile"}
print("\n\nTask - II\n")
read(angloFranc)

create(angloFranc, "row", "rangée")
print("\nAfter create:")
read(angloFranc)

update(angloFranc, "tails(coin)", "pile (pièce de monnaie)")
print("\nAfter update:")
read(angloFranc)

delete(angloFranc, "calculator")
print("\nAfter delete:")
read(angloFranc)

replace(angloFranc, "vertex", "vertices")
print("\nAfter replace:")
read(angloFranc)

print(f"Find 'object': {find(angloFranc, "object")}")

# Task - 3
tomorrowCorporation = {
                "Worker A": ["+0111", "workerA@gmail.com", "Deputy Director", "Office 1", "worker-A"], 
                "Worker B": ["+0222", "workerB@gmail.com", "Director", "Office 10", "worker-B"], 
                "Worker C": ["+0333", "workerC@gmail.com", "Employee", "Office 99", "worker-C"] }

print("\n\nTask - III\n")
read(tomorrowCorporation)

create(tomorrowCorporation, "Worker D", ["+0444", "workerD@gmail.com", "Employer", "Office 0", "worker-D"])
print("\nAfter create:")
read(tomorrowCorporation)

update(tomorrowCorporation, "Worker C", ["+0333", "workerC@gmail.com", "Manager", "Office 99", "worker-C"])
print("\nAfter update:")
read(tomorrowCorporation)

delete(tomorrowCorporation, "Worker A")
print("\nAfter delete:")
read(tomorrowCorporation)

replace(tomorrowCorporation, "Worker B", "Worker X")
print("\nAfter replace:")
read(tomorrowCorporation)

print(f"Find 'Worker D': {find(tomorrowCorporation, "Worker D")}")

# Task - IV
books = {
                "ISBN13 978-0-8759-2433-5": ["Общий курс физики том III Электричество", "Д.В. Сивухин", "Техническое", "2003", "730", "Физматлит"], 
                "ISBN13 978-2-2574-3984-0": ["Общий курс физики том II Термодинамика", "Д.В. Сивухин", "Техническое", "2001", "560", "Физматлит"], 
                "ISBN13 978-4-1831-0421-2": ["Курс общей физики том I Механика", "Д.В. Сивухин", "Техническое", "2001", "520", "Физматлит"] }

print("\n\nTask - IV\n")
read(books)

create(books, "ISBN13 978-9-7889-7179-5", ["Общий курс физики том IV Оптика", "Д.В. Сивухин", "Техническое", "2003", "780", "Физматлит"])
print("\nAfter create:")
read(books)

update(books, "ISBN13 978-4-1831-0421-2", ["Общий курс физики том I Механика", "Д.В. Сивухин", "Техническое", "2003", "525", "Физматлит"])
print("\nAfter update:")
read(books)

delete(books, "ISBN13 978-4-1831-0421-2")
print("\nAfter delete:")
read(books)

replace(books, "ISBN13 978-0-8759-2433-5", "ISBN13 978-4-7527-7125-8")
print("\nAfter replace:")
read(books)

print(f"Find 'ISBN13 978-9-7889-7179-5': {find(books, "ISBN13 978-9-7889-7179-5")}")