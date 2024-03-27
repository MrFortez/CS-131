#########################################################
# Name: Brandon Fortes
# Date: January 30, 2024
# Description: Implements vehicle, truck and car, and Honda Civic and Dodge Ram classes using inheritance
#########################################################

# the vehicle class
# a vehicle has a year, make, and model
# a vehicle is instantiated with a make and model
class Vehicle:
    def __init__(self, make, model):
        self.year = 2000
        self.make = make
        self.model = model

    @property
    def year(self):
        return self._year

    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @year.setter 
    def year(self, value):
        value = self.year if value < 2000 else value
        value = self.year if value > 2018 else value
        self._year = value

    @make.setter 
    def make(self, value):
        self._make = value

    @model.setter 
    def model(self, value):
        self._model = value

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# the truck class
# a truck is a vehicle
# a truck is instantiated with a make and model
class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(self.make, self.model)
        self.make = make
        self.model = model

# the car class
# a car is a vehicle
# a car is instantiated with a make and model
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(self.make, self.model)
        self.make = make
        self.model = model

# the Dodge Ram class
# a Dodge Ram is a truck
# a Dodge Ram is instantiated with a year
# all Dodge Rams have the same make and model
class DodgeRam(Truck):
    make = "Dodge"
    model = "Ram"
    def __init__(self, year):
        super().__init__(self.make, self.model)
        self.year = year


# the Honda Civic class
# a Honda Civic is a car
# a Honda Civic is instantiated with a year
# all Honda Civics have the same make and model
class HondaCivic(Car):
    make = "Honda"
    model = "Civic"
    def __init__(self, year):
        super().__init__(self.make, self.model)
        self.year = year



# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print(ram)

civic1 = HondaCivic(2007)
print(civic1)

civic2 = HondaCivic(1999)
print(civic2)

