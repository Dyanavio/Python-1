# Parts - I and II

class Book:
    def __init__(self, name, year: int, publisher, genre, author, price: float):
        self.__name = name
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def GetName(self):
        return self.__name
    def SetName(self, name):
        self.__name = name
    
    def GetYear(self):
        return self.__year
    def SetYear(self, year: int):
        self.__year = year

    def GetPublisher(self):
        return self.__publisher
    def SetPublisher(self, publisher):
        self.__publisher = publisher

    def GetGenre(self):
        return self.__genre
    def SetGenre(self, genre):
        self.__genre = genre
    
    def GetGenre(self):
        return self.__author
    def SetGenre(self, author):
        self.__author = author
    
    def GetGenre(self):
        return self.__price
    def SetGenre(self, price: float):
        self.__price = price
    
    def __str__(self):
        return f"> Name: {self.__name}\n> Year: {self.__year}\n> Publisher: {self.__publisher}\n> Genre: {self.__genre}\n> Author: {self.__author}\n> Price: {self.__price}\n"

crimesAndPunishment = Book("Crimes & Punishment", 1866, "Old Publishing Company", "Thriller", "Fyodor Dostoevsky", 19.99)
cSharpInNutshell = Book("C# in a nutshell", 2023, "O'reilly", "Scientific", "Joseph Albahari", 29.99)
print(crimesAndPunishment)
print(cSharpInNutshell)


class Stadium:
    def __init__(self, name, date: int, country, city, capacity:int):
        self.__name = name
        self.__date = date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def GetName(self):
        return self.__name
    def SetName(self, name):
        self.__name = name
    
    def GetDate(self):
        return self.__date
    def SetDate(self, date: int):
        self.__date = date

    def GetCountry(self):
        return self.__country
    def SetCountry(self, country):
        self.__country = country

    def GetCity(self):
        return self.__city
    def SetCity(self, city):
        self.__city = city

    def GetCapacity(self):
        return self.__capacity
    def SetCapacity(self, capacity: int):
        self.__capacity = capacity
    
    def __str__(self):
        return f"> Name: {self.__name}\n> Opened: {self.__date}\n> Country: {self.__country}\n> City: {self.__city}\n> Cap: {self.__capacity}\n"

stadiumOfLight = Stadium("Stadium of Light", 1997, "England", "Sunderland", 49000)
print(stadiumOfLight)