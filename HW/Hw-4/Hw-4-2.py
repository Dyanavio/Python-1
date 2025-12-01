import math

# Part - III
class Fraction:
    __count = 0

    def __init__(self, enumerator : int, denominator : int):
        self.__enumerator = enumerator
        self.__denominator = denominator
        Fraction.__count += 1

    @staticmethod
    def GetCount():
        return Fraction.__count

    def Add(self, fraction: Fraction):
        lcm = math.lcm(self.__denominator, fraction.GetDenominator())
        return Fraction((self.__enumerator * (lcm // self.__denominator)) + (fraction.GetEnumerator() * (lcm // fraction.GetDenominator())), lcm).Simplify()

    def Subtract(self, fraction: Fraction):
        lcm = math.lcm(self.__denominator, fraction.GetDenominator())
        return Fraction((self.__enumerator * (lcm // self.__denominator)) -(fraction.GetEnumerator() * (lcm // fraction.GetDenominator())), lcm).Simplify()

    def Multiply(self, fraction: Fraction):
        return Fraction(self.__enumerator * fraction.GetEnumerator(), self.__denominator * fraction.GetDenominator()).Simplify()

    def Divide(self, fraction: Fraction):
        return Fraction(self.__enumerator * fraction.GetDenominator(), self.__denominator * fraction.GetEnumerator()).Simplify()
    
    def Simplify(self):
        gcd = math.gcd(self.__enumerator, self.__denominator)
        if(gcd != 0):
            self.__enumerator /= gcd
            self.__denominator /= gcd
        return self
        


    def GetEnumerator(self):
        return self.__enumerator
    
    def GetDenominator(self):
        return self.__denominator
    
    def __str__(self):
        return f"{self.__enumerator}/{self.__denominator}"
    
fr1 = Fraction(4, 5)
print(f"Fraction 1: {fr1}   | Count: {Fraction.GetCount()}")
fr2 = Fraction(2, 9)
print(f"Fraction 2: {fr2}   | Count: {Fraction.GetCount()}")
fr3 = fr1.Add(fr2)
print(f"Fraction 3: {fr1} + {fr2} = {fr3}   | Count: {Fraction.GetCount()}")
fr4 = fr1.Subtract(fr2)
print(f"Fraction 4: {fr1} - {fr2} = {fr4}   | Count: {Fraction.GetCount()}")
fr5 = fr1.Multiply(fr2)
print(f"Fraction 5: {fr1} * {fr2} = {fr5}   | Count: {Fraction.GetCount()}")
fr6 = fr1.Divide(fr2)
print(f"Fraction 6: {fr1} / {fr2} = {fr6}   | Count: {Fraction.GetCount()}")


# Task - II
class Convert:
    __conversionCount = 0
    _TEMPERATURE_TERM = 32
    _TEMPERATURE_MULTIPLIER = 1.8
    _LENGTH_MULTIPLIER = 0.3048
    _MASS_MULTIPLIER = 0.4536

    # Temperature
    @staticmethod
    def CelsiusToFahrenheit(celsius : float):
        Convert.__conversionCount += 1
        return (celsius * Convert._TEMPERATURE_MULTIPLIER) + Convert._TEMPERATURE_TERM
    
    @staticmethod
    def FahrenheitToCelsius(fahrenheit : float):
        Convert.__conversionCount += 1
        return (fahrenheit - Convert._TEMPERATURE_TERM) / Convert._TEMPERATURE_MULTIPLIER
    
    # Length
    @staticmethod
    def FeetToMeter(feet: float):
        Convert.__conversionCount += 1
        return feet / Convert._LENGTH_MULTIPLIER

    @staticmethod
    def MeterToFeet(meter: float):
        Convert.__conversionCount += 1
        return Convert._LENGTH_MULTIPLIER * meter
    
    # Mass
    @staticmethod
    def KilogramToPound(kilogram : float):
        Convert.__conversionCount += 1
        return kilogram / Convert._MASS_MULTIPLIER

    @staticmethod
    def PoundToKilogram(pound : float):
        Convert.__conversionCount += 1
        return pound * Convert._MASS_MULTIPLIER

    @staticmethod
    def GetTotalConvesions():
        return Convert.__conversionCount

print('')
print(f"45 F = {Convert.FahrenheitToCelsius(45):.4f} C  | Count: {Convert.GetTotalConvesions()}")
print(f"32 C = {Convert.CelsiusToFahrenheit(32):.4f} F  | Count: {Convert.GetTotalConvesions()}")
print(f"1 m = {Convert.MeterToFeet(1):.4f} ft  | Count: {Convert.GetTotalConvesions()}")
print(f"1 ft = {Convert.FeetToMeter(1):.4f} m  | Count: {Convert.GetTotalConvesions()}")
print(f"1 kg = {Convert.KilogramToPound(1):.4f} lb  | Count: {Convert.GetTotalConvesions()}")
print(f"1 lb = {Convert.PoundToKilogram(1):.4f} kg  | Count: {Convert.GetTotalConvesions()}")