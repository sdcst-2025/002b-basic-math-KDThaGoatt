#!python3

'''
##### Task 8
Read through the file **example2.py** for information on using the math module.
Calculate the length of a hypotenuse given 2 variables
Set the value of a to 5
Set the value of b to 8

Determine the length of the hypotenuse and store it into a variable called c
print the value of c

You may use either the ** operator or math.pow(x,y) for your exponents
You may use either math.sqrt(x) or the exponent to the power of 0.5 for your square root

 '''
import math

a = 5

b = 8

c = math.sqrt(a**2 + b**2)

print (c)