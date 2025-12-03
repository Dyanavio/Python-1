class Car:
    def __init__(self, model = None, year = None, vin = None):
        self.model = model
        self.year = year
        self.vin = vin
    
    def __str__(self) -> str:
        return f"Model: {self.model}  |  Year: {self.year}  |  Vin: {self.vin}"
    
    @classmethod
    def fromString(cls, string): # cls - is a reference to the class itself
        model, year, vin = string.split('-')
        return cls(model, year, vin)
    
    @classmethod
    def fromVin(cls, vin):
        return cls("", 0 , vin)
    
    @classmethod
    def fromDictionary(cls, dict: dict):
        model = dict["model"] if "model" in dict else None
        year = dict["year"] if "year" in dict else None
        vin = dict["vin"] if "vin" in dict else None
        return cls(model, year, vin)
    
car1 = Car("Toyota", 2020, "17")
car2 = Car(vin="0000")
#print(car1)
#print(car2)

carString = "Honda-2022-0000"
car3 = Car.fromString(carString)
#print(car3)

parameters = {"model": "Nissan", "year": 2024, "vin": "AAAA0000"}
car4 = Car.fromDictionary(parameters)
print(car4)