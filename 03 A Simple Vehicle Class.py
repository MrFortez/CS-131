######################################################################################################################
# Name: Brandon Fortes 
# Date: December 18, 2023
# Description: A program with a vehicle class that defines several different objects of said class with differing attributes
######################################################################################################################

# the vehicle class
# a vehicle has a year, make, and model
class Vehicle:
    def __init__(self, make, model):
        self._year = 2000
        self._make = make
        self._model = model

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




# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
print("v1={} {}".format(v1.make, v1.model))
print("v2={} {}".format(v2.make, v2.model))
print()

v1.year = 2016
v2.year = 2016
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))
print()

v1.year = 1999
v2.model = "Civic"
v2.year = 2007
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))

