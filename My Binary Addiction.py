#########################################################
# Name: Brandon Fortes
# Date: January 31, 2024
# Description: A program that displays the truth table for the full adder function
#########################################################

# a half adder function, taking in two binary inputs and returning the sum and carry
def halfAdder(a, b):
    sum = a ^ b
    cOut = a & b
    return sum, cOut

# a full adder function, taking in 3 binary inputs (two bits and a carry in) and returning the sum and the carry out
def fullAdder(a, b, cIn):
    sum1, c1 = halfAdder(a, b)
    sumOut = halfAdder(sum1, cIn)[0]
    cOut = halfAdder(sum1, cIn)[1] | c1
    return sumOut, cOut



# MAIN CODE #
# prints the truth table for the full adder
print(" a b cin  sum cout")
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            print(f"[{i} {j} {k}]    {fullAdder(i, j, k)}")
