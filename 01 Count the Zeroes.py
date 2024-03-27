################################################################################
# Name:  Brandon Fortes
# Date:  December 1, 2023
# Description: A program that calculates the total number of zeros between 1 and a user given upper bound, as well as the time it takes to calculate the result
################################################################################

from time import time

# a fuction that returns a user-inputed integer that represents the upper bound of numbers to check for zeros.
def getRange():
    return int(input("What number do you want to count zeros to? "))

# a function that takes in an integer greater than 0 as an argument and returns the number of zeros in the number.
def countZeros(num):
    count = 0
    while (num > 0):
        if (num % 10 == 0):
            count += 1
        num //= 10
    return count

# a function that takes an upper bound and calculates the total number of zeros from 1 to said upper bound
def calculateTotalZeros(max):
    count = 0
    for i in range(1, max + 1):
        count += countZeros(i)

    return count

upperBound = getRange()
startTime = time()
zeroTotal = calculateTotalZeros(upperBound)
stopTime = time()
print(f"The number of zeros written from 1 to {upperBound} is {zeroTotal}.")
print(f"This took {stopTime - startTime} seconds.")