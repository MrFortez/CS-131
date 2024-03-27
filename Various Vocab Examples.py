from random import *

def method(variable):  # formal parameter
    return variable * 2

method(7)  # actual parameter
method(100000000)  # actual parameter


def f():
    a = 7   # local variable (python will prioritize the local variable "a")
    # print(a)

a = 0  # global variable
f()
# print(a)

# In Python, you cannot mutate a global variable within a function
# def f():
#     a += 7  <- this line will cause an error
#     print(a)

# a = 0  
# f()

# The index is the location of a value in the list, the value is the data stored at each index, together they are an item
numList = []
i = 0
for i in range(0, 100):
    numList.append(randint(0, 9))
# print(numList)

def getMin(list):
    min = list[0]
    for x in list:
        if (min > x):
            min = x
    return min

# print(getMin(numList))

def findValue(list, target):
    for x in list:
        if (x ==  target):
            return True
    return False

# print(findValue(numList, 7))



class Dog:
    kind = "canine"

    def __init__(self, dogName):
        self.name = dogName
        self.tricks = []
        self.age = 0
        self.friends = []

    def speak(self):
        print("AMONG US!")
    
    def getName(self):
        return self.name
    
    def learn(self, trick):
        self.tricks.append(trick)

    def increaseAge(self):
        self.age += 1
        
    def getAge(self):
        return self.age

    def befriend(self, other):
        self.friends.append(other.name)

    def __str__(self):
        return (f"This is {self.name}")

dogOne = Dog("billy bob")
dogTwo = Dog("Sally sob")
# dogOne.speak()
dogOne.getName()
# dogTwo.speak()
dogTwo.getName()
# print(dogTwo)
# print(dogOne)
dogOne.learn("play flute")
dogTwo.learn("Rob a bank")
dogOne.increaseAge()
dogOne.increaseAge()
dogOne.increaseAge()
# print(dogOne.getAge())
dogOne.befriend(dogTwo)
# print(dogOne.friends)

class Vehicle:
    purpose = "to go"

    def __init__(self, numOfTires, haveEngine, noise):
        self.numOfTires = numOfTires
        self.hasEngine = haveEngine
        self.noise = noise

    def go(self):
        print(self.noise)
    
    def setNumOfTires(self, num):
        self.numOfTires = num
    
    def getNumOfTires(self):
        return self.numOfTires

    def setHasEngine(self, hasEngine):
        self.hasEngine = hasEngine
    
    def getHasEngine(self):
        return self.hasEngine
    
paraglider = Vehicle(0, False, "Woosh")
car = Vehicle(4, True, "Vroom")
jetski = Vehicle(0, True, "splish splash")


class Fraction:

    def __init__(self, numerator = 0, denominator = 1):
        self.setNum(numerator)
        self.setDen(denominator)

    def setDen(self, value):
        if (value != 0):
            self.den = value
        else:
            raise Exception("Denominator cannot be 0!")
        
    def setNum(self, value):
        self.num = value

    def getDen(self):
        return self.den
    
    def getNum(self):
        return self.num
        
    def getDecimal(self):
        return self.num / self.den
    
    def add(self, other):
        newNum = (self.getNum() * other.getDen()) + (self.getDen() * other.getNum())
        newDem = (self.getDen() * other.getDen())
        return Fraction(newNum, newDem)
    
    def __add__(self, other):       # The basic operators have magic functions (see example below)
        newNum = (self.getNum() * other.getDen()) + (self.getDen() * other.getNum())
        newDem = (self.getDen() * other.getDen())
        return Fraction(newNum, newDem)
    
    def subtract(self, other):
        newNum = (self.getNum() * other.getDen()) - (self.getDen() * other.getNum())
        newDem = (self.getDen() * other.getDen())
        return Fraction(newNum, newDem)
    
    def __sub__(self, other):
        newNum = (self.getNum() * other.getDen()) - (self.getDen() * other.getNum())
        newDem = (self.getDen() * other.getDen())
        return Fraction(newNum, newDem)
    
    def multiply(self, other):
        newNum = (self.getNum() * other.getNum())
        newDem = (self.getDen() * other.getDen())
        return Fraction(newNum, newDem)

    def __mul_(self, other):
        newNum = (self.getNum() * other.getNum())
        newDem = (self.getDen() * other.getDen())
        return Fraction(newNum, newDem)
    
    def divide(self, other):
        newNum = (self.getNum() * other.getDen())
        newDem = (self.getDen() * other.getNum())
        return Fraction(newNum, newDem)
    
    def __trueDiv__(self, other):
        newNum = (self.getNum() * other.getDen())
        newDem = (self.getDen() * other.getNum())
        return Fraction(newNum, newDem)
    
    def simplify(self):
        i = 2
        divisor = 1
        while (i < (self.getNum() / 2) and i < (self.getNum() / 2)):
            if (self.getNum() % i == 0 and self.getDen() % i == 0):
                divisor = i
            i += 1
        self.setNum(int(self.getNum() / divisor))
        self.setDen(int(self.getDen() / divisor))


    def __str__(self):
        return f"{self.getNum()}/{self.getDen()}   ({self.getDecimal()})"
    
  

        
f1 = Fraction(3, 2)
f2 = Fraction(7, 8)

print(f1.getDecimal())
print(f1)
print(f2)
f3 = f1.add(f2)
print(f3)
f6 = f1 + f2
print(f6)
f4 = f2.subtract(f1)
print(f4)
f5 = f1.multiply(f2)
print(f5)
f5 = f1.divide(f2)
print(f5)
f5.simplify()
print(f5)
print("")

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a

    def getB(self):
        return self.b
    
    def setA(self, val):
        self.a = val

    def setB(self, val):
        self.b = val

    def __str__(self):
        return f"{self.a} + {self.b}i"
    
    def __add__(self, other):
        newA = (self.a + other.a)
        newB = (self.b + other.b)
        return ComplexNumber(newA, newB)
    
    def __mul__(self, other):
        newA = (self.a * other.a) - (self.b * other.b)
        newB = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(newA, newB)
    
comNum1 = ComplexNumber(2, 5)
comNum2 = ComplexNumber(4, 7)
comNum3 = ComplexNumber(3, 0)
print(comNum1)
comNum4 = comNum1 + comNum2
print(comNum4)
comNum5 = comNum1 * comNum3
print(comNum5)


# Half Adder

def halfAdder(a, b):
    s = (a and (not b)) or ((not a) and b)
    c = a and b 
    return s, c 

def bitwiseHalfAdder(a, b):
    s = a ^ b
    c = a & b
    return s, c

print(halfAdder(0, 1))
print(bitwiseHalfAdder(0, 0))


# Coin flip #

print("Group A wins by one of each \nGroup B wins by both heads \nGroup C wins by both tails")
groupA = 0
groupB = 0
groupC = 0
for i in range(0, 1000):
    coin1 = randint(0, 1)
    coin2 = randint(0, 1)

    if (coin1 + coin2 == 0):
        groupC += 1
    elif (coin1 + coin2 == 2):
        groupB += 1
    else:
        groupA += 1

print("the scores were:")
print(f"Group A: {groupA}")
print(f"Group B: {groupB}")
print(f"Group C: {groupC}")

## 2 d6 rolls
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trials =  9
total = 0
for i in range(0, trials):
    diceOne = randint(1, 6)
    diceTwo = randint(1, 6)
    scores[(diceOne + diceTwo) - 2] += 1
    total += diceOne + diceTwo

print(scores)
print(total / trials)

coolString = "Hello World"
print(coolString[:-1])