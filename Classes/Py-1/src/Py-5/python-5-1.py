'''
class Car:
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    def __init__(self, model = None, year = None, vin = None):
        self.__model = model
        self.__year = year
        self.__vin = vin
    
    def __str__(self) -> str:
        return f"Model: {self.__model}  |  Year: {self.__year}  |  Vin: {self.__vin}"
    
car1 = Car()
car1.model = "Tesla"
#print(car1.model)

class Country:

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def continent(self):
        return self.__continent
    
    @continent.setter
    def continent(self, value):
        self.__continent = value
    
    @property
    def population(self):
        return self.__population
    
    @property
    def code(self):
        return self.__code
    
    @property
    def capital(self):
        return self.__capital
    
    @property
    def cities(self):
        return self.__cities

    def __init__(self, name = None, continent = None, population = None, code = None, capital = None, cities = None):
        self.__name = name
        self.__continent = continent
        self.__population = population
        self.__code = code
        self.__capital = capital
        self.__cities = cities
    
    def __str__(self) -> str:
        return f"{self.__name}:\n> Continent: {self.__continent}\n> Population: {self.__population}\n> Code: {self.__code}\n> Capital: {self.__capital}\n> Cities: {self.__cities}"

    @classmethod
    def fromDictionary(cls, dict: dict):
        name = dict["name"] if "name" in dict else None
        population = dict["population"] if "population" in dict else None
        continent = dict["continent"] if "continent" in dict else None
        code = dict["code"] if "code" in dict else None
        capital = dict["capital"] if "capital" in dict else None
        cities = dict["cities"] if "cities" in dict else None
        return cls(name, continent, population, code, capital, cities)
    
japan = Country.fromDictionary({"name": "Japan", "population": 123100000, "continent": "Asia", "code": "+81", "capital": "Tokyo", 
                                "cities": ["Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kawasaki", "Kobe", "Kyoto", "Saitama", "Hiroshima", "Sendai", "Chiba", "Kitakyushu"  	]})


print(japan)
japan.continent = "East Asia"
print('')
print(japan)


class Animal():
    def __init__(self, name) -> None:
        self.name = name
        print("Animal Base Class Contructor")

    def voice(self) -> str:
        pass

class Feline:
    def meow(sel):
        return "Mew"
    
class Cat(Animal, Feline):
    def voice(self) -> str:
        return f"Cat: {self.meow()}"
    
cat = Cat("Kutuzov")
print(cat.name, cat.voice())


class A:
    def voice(self):
        print("I am class A")

class B:
    def voice(self):
        print("I am class B")

class C(A, B): # D -> A -> B -> object : search order
    pass

obj = C()
obj.voice()
print(C.mro())
'''

class A:
    def voice(self):
        print("I am class A")

class B(A):
    def voice(self):
        print("I am class B")

class C(A):
    def voice(self):
        print("I am class C")

class D(B, C):
    pass

print(D.mro())