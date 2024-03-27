#########################################################
# Name: Brandon Fortes
# Date: February 23, 2024
# Description: WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#########################################################

from random import *

# Perform two coin toss simulations and return the results added together
def coinToss():
    coin1 = randint(0, 1)
    coin2 = randint(0, 1)

    return coin1 + coin2

# Perform the inputed number of coin tosses, and depending on the result each cycle, add 1 to the corrosponding score, then return the scores
def runGame(cycles): 
    groupA = 0
    prof = 0
    groupB = 0
    for i in range(0, cycles):
        result = coinToss()
        if (result == 0):
            groupA += 1
        elif (result== 1):
            prof += 1
        else:
            groupB += 1
    
    return groupA, prof, groupB



## MAIN CODE ##

numOfGames = int(input("How many games? "))
coinTosses = int(input("How many coin tosses per game? "))
wins = [0, 0, 0]

for i in range(0, numOfGames):
    print(f"Game {i}:")
    result = runGame(coinTosses)
    print(f" Group A: {result[0]} ({(result[0] / coinTosses) * 100}%); Group B: {result[2]} ({(result[2] / coinTosses) * 100}%); Prof: {result[1]} ({(result[1] / coinTosses) * 100}%)")
    
    # Catch Ties, randomly select winner
    if (result[1] == result[0]):
        wins[randint(0, 1)] += 1

    elif (result[1] == result[2]):
        wins[randint(1, 2)] += 1

    elif (result[0] == result[2]):
        if (randint(0, 1) == 0):
            wins[0] += 1
        else:
            wins[2] += 1

    # Determine Winner
    if (result[1] > result[0] and result[1] > result[2]):
        wins[1] += 1

    elif (result[0] > result[2]):
        wins[0] += 1

    elif (result[2] > result[0]):
        wins[2] += 1

print(f"Wins: Group A={wins[0]} ({(wins[0] / numOfGames) * 100}); Group B={wins[2]} ({(wins[2] / numOfGames) * 100}); Prof={wins[1]} ({(wins[1] / numOfGames) * 100}%)")
